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
# DModel = sqldf(''' SELECT * FROM flights F
#                     INNER JOIN airlines A ON A.carrier = F.carrier
#                     INNER JOIN airports AI on AI.faa = F.origin
#                     LEFT JOIN planes P on P.tailnum = F.tailnum
#                     LEFT JOIN weather W on W.time_hour = F.time_hour and W.origin = F.origin''')

DModel = sqldf('''SELECT w.temp, w.humid, w.wind_speed, w.origin, p.year, w.month
                    FROM flights F
                    LEFT JOIN airlines A ON A.carrier = F.carrier
                    LEFT JOIN airports AI on AI.faa = F.origin
                    LEFT JOIN planes P on P.tailnum = F.tailnum
                    LEFT JOIN weather W on W.time_hour = F.time_hour and W.origin = F.origin''')

DModel2 = sqldf('''select a.month as Month, avg(a.temp) as Temperature, avg(a.humid) as Humidity, avg(a.wind_speed) as Wind_Speed, a.origin as Origin from DModel a
                    where Year is not null and Origin is not null
                    group by Month
                    order by 1 desc''')


fig2 = px.line(DModel2, x='Month', y=['Temperature','Humidity', 'Wind_Speed'])
## fig2.update_traces(marker_color='#78c2ad')




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
                    html.H3('Weather', style={'textAlign':'center'}),
                    dcc.Dropdown(id='Origin2',
                                 options=DModel2['Origin'].unique(),
                                 value=[],
                                 multi=True,
                                 style={'color':'black'}
                                 ),
                    html.Hr(),
                    dcc.Graph(id='Wchart', figure=fig2),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])


@callback(
    Output("Wchart", "figure"),
    Input("Origin2", "value"), 

 )   

def update_graph_card(Origin2):
      if len(Origin2) == 0:
          return dash.no_update
      else:
          df_filtered2 = DModel2[DModel2["Origin"].isin(Origin2)]
          fig2 = px.line(df_filtered2, x="Month", y=['Temperature','Humidity', 'Wind_Speed'], color="Origin",
                        labels={"Origin": "Origin"}).update_traces(mode='lines+markers')
          return fig2
