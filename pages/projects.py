import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar
import os
from pandasql import sqldf

dash.register_page(__name__, title='App1', order=1)



os.chdir('D:\\OneDrive - Universidad Galileo\\Galileo\\Product Development\\Proyecto\\assets\\Datasets')
airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
flights = pd.read_csv('flights.csv')
planes = pd.read_csv('planes.csv')
weather = pd.read_csv('weather.csv')

DModel = sqldf('''SELECT f.flight, A.name, AI.lat, AI.lon, AI.alt, AI.tz, AI.dst, AI.tzone, P.year, P.type, P.manufacturer, P.model, P.engines, P.seats, P.speed, P.engine,
                    W.month, W.day, W.hour, W.temp, W.dewp, W.humid, W.wind_dir, W.wind_speed, W.wind_gust, W.precip, W.pressure, W.visib, f.origin as origin
                    FROM flights F
                    LEFT JOIN airlines A ON A.carrier = F.carrier
                    LEFT JOIN airports AI on AI.faa = F.origin
                    LEFT JOIN planes P on P.tailnum = F.tailnum
                    LEFT JOIN weather W on W.time_hour = F.time_hour and W.origin = F.origin''')

DModel2 = sqldf('''select origin as Origin, a.year as Year, count(flight) as Flight from DModel a
                    where year is not null
                    group by year, origin
                    order by 1 desc''')


fig = px.line(DModel2, x='Year', y='Flight')
fig.update_traces(marker_color='#78c2ad')

    


def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('Cantidad De Vuelos En El Tiempo', style={'textAlign':'center'}),
                    dcc.Dropdown(id='Origin',
                                 options=DModel2['Origin'].unique(),
                                 value=['EWR'],
                                 multi=True,
                                 style={'color':'black'}
                                 ),
                    html.Hr(),
                    dcc.Graph(id='line_chart', figure=fig),

                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])
        
@callback(
    Output("line_chart", "figure"),
    Input("Origin", "value"), 

)   

def update_graph_card(Origin):
    if len(Origin) == 0:
        return dash.no_update
    else:
        df_filtered = DModel2[DModel2["Origin"].isin(Origin)]
        fig = px.line(df_filtered, x="Year", y="Flight", color="Origin",
                      labels={"Origin": "Origin"}).update_traces(mode='lines+markers')
        return fig