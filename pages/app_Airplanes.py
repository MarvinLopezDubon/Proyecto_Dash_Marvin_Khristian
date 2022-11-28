import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar
import os
from pandasql import sqldf
import plotly.graph_objs as go
import statistics
from functools import reduce

dash.register_page(__name__)

os.chdir('D:\\OneDrive - Universidad Galileo\\Galileo\\Product Development\\Proyecto\\assets\\Datasets')
airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
flights = pd.read_csv('flights.csv')
planes = pd.read_csv('planes.csv')
weather = pd.read_csv('weather.csv')

DModel = sqldf('''SELECT f.air_time as Air_Time, f.distance as Distancia_Recorrida, f.month as Month, 
                    p.tailnum as Tailnum, p.year as [Anio Construccion], p.type as [Tipo Avion], 
                    P.manufacturer as Fabricante, 
                    P.model as Modelo, 
                    P.engines as [No Motores], 
                    P.seats as [No Asientos]
                    FROM flights F
                    LEFT JOIN airlines A ON A.carrier = F.carrier
                    LEFT JOIN airports AI on AI.faa = F.origin
                    LEFT JOIN planes P on P.tailnum = F.tailnum
                    LEFT JOIN weather W on W.time_hour = F.time_hour and W.origin = F.origin''')
DModel2 = sqldf(''' SELECT Distancia_Recorrida, Air_Time, Month, Tailnum
                     from DModel where [Anio Construccion] is not null
                     ''')
DModel3 = DModel2.groupby(['Month', 'Tailnum']).mean().reset_index()
DModel3.columns = ['Month', 'Tailnum', 'DistRecorrMean', 'AirTimeMean']
DModel5 = DModel2.groupby(['Month', 'Tailnum']).median().reset_index()
DModel5.columns = ['Month', 'Tailnum', 'DistRecorrMedian', 'AirTimeMedian']
DModel6 = DModel2.groupby(['Month', 'Tailnum']).std().reset_index()
DModel6.columns = ['Month', 'Tailnum', 'DistRecorrstd', 'AirTimestd']
DModel7 = DModel2.groupby(['Month', 'Tailnum']).min().reset_index()
DModel7.columns = ['Month', 'Tailnum', 'DistRecorrMin', 'AirTimeMin']
DModel8 = DModel2.groupby(['Month', 'Tailnum']).max().reset_index()
DModel8.columns = ['Month', 'Tailnum', 'DistRecorrMax', 'AirTimeMax']

dfs = [DModel3, DModel5, DModel6, DModel7, DModel8]

final_df = reduce(lambda  left,right: pd.merge(left,right,on=['Tailnum', 'Month'],
                                            how='outer'), dfs)
DModel4 = sqldf(''' SELECT Tailnum, [Anio Construccion], [Tipo Avion], Fabricante, Modelo, [No Motores], [No Asientos]
                    from DModel where [Anio Construccion] is not null
                    order by [Anio Construccion]
                    ''')


fig = px.scatter(final_df, x='Month', y= ['DistRecorrMean', 'AirTimeMean', 'DistRecorrMedian', 'AirTimeMedian', 'DistRecorrstd', 'AirTimestd', 'DistRecorrMin', 'AirTimeMin', 'DistRecorrMax', 'AirTimeMax'])
fig2 = dash_table.DataTable(DModel4.to_dict('records'), 
            style_header={'textAlign':'center', 
             'backgroundColor': 'rgb(0, 0, 0)',
             'color': 'white'
             },
            style_data={'textAlign':'center',
            'backgroundColor': 'rgb(0, 0, 0)',
             'color': 'white'
            },        
            )

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar(), 
                    html.H2('Checkbox'),
                    dcc.Checklist(id = "Checklist",
                                  options=['Tiempo de Vuelo', 'Distancia Recorrida'],
                                  value=[] 
                                ),
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('Airplanes Statistics', style={'textAlign':'center'}),
                    dcc.Dropdown(id='Tailnum',
                                 options=final_df['Tailnum'].unique(),
                                 value=[],
                                 multi=True,
                                 style={'color':'black'}
                                 ),
                    html.Hr(),
                    dcc.Graph(id='StatsChart', figure=fig),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    ), 
    dbc.Row([
        dbc.Col(), 
        dbc.Col([html.Hr(),html.H3('Tabla Info Avion', style={'textAlign':'center'}), html.Hr(),
            html.H3(fig2
                )])
    
    ])
])
@callback(
    Output("StatsChart", "figure"),
    Input("Tailnum", "value"), 

)   

def update_graph_card(Tailnum):
    if len(Tailnum) == 0:
        return dash.no_update
    else:
        df_filtered = final_df[final_df["Tailnum"].isin(Tailnum)]
        fig = px.scatter(df_filtered, x='Month', y= ['DistRecorrMean', 'AirTimeMean', 'DistRecorrMedian', 'AirTimeMedian', 'DistRecorrstd', 'AirTimestd', 'DistRecorrMin', 'AirTimeMin', 'DistRecorrMax', 'AirTimeMax'])
        return fig

