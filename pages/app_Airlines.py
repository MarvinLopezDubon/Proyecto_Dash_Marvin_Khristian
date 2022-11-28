import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar
import os
from pandasql import sqldf
import plotly.graph_objs as go

dash.register_page(__name__)



os.chdir('D:\\OneDrive - Universidad Galileo\\Galileo\\Product Development\\Proyecto\\assets\\Datasets')
airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
flights = pd.read_csv('flights.csv')
planes = pd.read_csv('planes.csv')
weather = pd.read_csv('weather.csv')


DModel = sqldf('''SELECT f.flight, A.name, AI.lat, AI.lon, AI.alt, AI.tz, AI.dst, AI.tzone, P.year, P.type, P.manufacturer, P.model, P.engines, P.seats, P.speed, P.engine,
                    W.month, W.day, W.hour, W.temp, W.dewp, W.humid, W.wind_dir, W.wind_speed, W.wind_gust, W.precip, W.pressure, W.visib, f.origin as origin, F.carrier as Carrier
                    FROM flights F
                    LEFT JOIN airlines A ON A.carrier = F.carrier
                    LEFT JOIN airports AI on AI.faa = F.origin
                    LEFT JOIN planes P on P.tailnum = F.tailnum
                    LEFT JOIN weather W on W.time_hour = F.time_hour and W.origin = F.origin''')

DModel2 = sqldf('''select Carrier as Carrier, a.month as Month, count(flight) as Flight from DModel a
                    where Year is not null and Carrier is not null and Flight is not null and Month is not null
                    group by Month, Carrier
                    order by 1 desc''')

DModel3 = [go.Heatmap(x=DModel2['Carrier'], y=DModel2['Month'], z=DModel2['Flight'].values.tolist())]
layout = go.Layout(title = ' ')
fig = go.Figure(data=DModel3, layout=layout)


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
                    html.H3('Cantidad de Vuelos por Mes', style={'textAlign':'center'}),
                    html.Hr(),
                    dcc.Graph(id='Heat_map', figure=fig),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

        
@callback(
    Output("Heat_map", "figure"),
    Input("Carrier", "value"), 

)   

def update_graph_card(Carrier):
    if len(Carrier) == 0:
        return dash.no_update
    else:
        df_filtered = DModel3[DModel3["Carrier"].isin(Carrier)]
        #df_filtered = df_filtered.groupby(["year", "origin"])[['month']].median().reset_index()
        #fig = px.imshow(df_filtered[Carrier],
                     # labels={"Carrier": "Carrier"}).update_traces(mode='lines+markers')
        return fig