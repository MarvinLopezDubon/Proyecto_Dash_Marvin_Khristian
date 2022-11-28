import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)


layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Carousel(
    items=[
        {
            "key": "1",
            "src": "/assets/CodeSS1.jpg",
            "header": "Universidad Galileo",
            "caption": "Master in Business Intelligence and Analytics, Product Development",
        },
        {
            "key": "2",
            "src": "/assets/CodeSS2.jpg",
            "header": "App DASH",
            "caption": "Grafica de vuelos en el tiempo en DASH",
        },
        {
            "key": "3",
            "src": "/assets/CodeSS3.jpg",
            "header": "Visual Studio",
            "caption": "Código de Python-Dash en Visual Studio",
        },
        {
            "key": "4",
            "src": "/assets/CodeSS4.jpg",
            "header": "SQL Server Management Studio",
            "caption": "Creación de Vista con cubo dimensional de los Datasets",
        },
    ], interval=1400
)

        ])

    ]), 
    dbc.Row([
    dbc.Col([
    html.Hr(),
    dcc.Markdown('### Khristian De La Vega', style={'textAlign':'center'}),
    dcc.Markdown('Carnet: 20001599', style={'textAlign': 'center'}),
    html.Img(src=r'assets/Khristian.png', alt='Image Not Found', style={'display': 'block' , 'height': '45%','width': '25%', 'marginLeft': 'auto','marginRight': 'auto'}),
    
    dcc.Markdown('Universidad Galileo', style={'textAlign': 'center'}),
    dcc.Markdown('Master in Business Intelligence and Analytics', style={'textAlign': 'center'}),
    html.Hr(), 
    dcc.Markdown('')
    ]), 
   

    dbc.Col([
    html.Hr(),
    dcc.Markdown('### Marvin López', style={'textAlign':'center'}),
    dcc.Markdown('Carnet: 14006749', style={'textAlign': 'center'}),
    html.Img(src=r'assets/Marvin.png', alt='Image Not Found', style={'display': 'block' , 'height': '45%','width': '25%', 'marginLeft': 'auto','marginRight': 'auto'}),
    dcc.Markdown('Universidad Galileo', style={'textAlign': 'center'}),
    dcc.Markdown('Master in Business Intelligence and Analytics', style={'textAlign': 'center'}),
    html.Hr(), 
    dcc.Markdown('')
     
            ])
     
     
     ])
     ])
