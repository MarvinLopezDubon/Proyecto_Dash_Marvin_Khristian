import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)

def layout():
    return html.Div([
    html.H3("Conclusiones y Observasiones", style={'textAlign':'center'}, className='my-3'),
    html.Hr(),
    dbc.Row([dcc.Markdown('•	En este proyecto en donde mediante información de datos en archivos .CSV se debe de poder graficar con Python, Dash y Plotly. En un inicio se tomaron los 5 archivos y se cargaron en Sql Serve Management Studio para poder crear el cubo dimensional y almacenarlo dentro de una vista y poderlo consultar con Python mediante una conexión de SQL el cual funcionó, sin embargo, al momento de verificar la entrega nos percatamos que no seria funcional por que cuando evaluaran el proyecto no haría la conexión a nuestra base de datos. En este punto se cambio y ahora se cargan los archivos en el origen del proyecto para poder trabajar en él.')]),
    dbc.Row([dcc.Markdown('•	Se agrego un carrousel a nuestro proyecto como parte de mejoras de presentación siempre ubicado desde la pagina dash.plotly.com, y adicionalmente se editaron imágenes para mostrar.')]),
    dbc.Row([dcc.Markdown('•	El Login de Dash no están completo debido a que cuando es primera vez que ingresa la url si le solicita que ingrese usuario y contraseña, pero si refresca este ya no lo solicita, por lo que debe de borrar cache para que olvide el registro y de esta forma le solicito login de nuevo.')]),
    html.Hr(),
    dbc.Row([
       dcc.Markdown('Flights'),
        dcc.Markdown('•	En la gráfica de cantidad de vuelos en el tiempo, técnicamente se implementó bien, ahora bien en el análisis de la información para el año 2001 hay un pico en la cantidad de vuelos registrados y luego de ello se redujeron de forma considerable, esto lo podríamos atribuir a los acontecimientos de 09/11.'),
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dcc.Markdown('Airlines'),
        dcc.Markdown('•	En la gráfica Aerolineas con más vuelos por mes, en la configuración no se presentó ningún inconveniente, en cuanto al análisis de la información nos percatamos que los Origin con más vuelos son UA, EV, DL, B6.'),
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dcc.Markdown('Airplanes'),
        dcc.Markdown('•	En la grafica de distancia recorrida y tiempo en el aire, en esta sección tuvimos que realizar una parte del código en sql y la otra parte en Python para poder obtener las estadisitcas. Adicionalmente se implemento una tabla para que se pudiera mostrar la información de los aviones, en esta sección también se le agrego como mejoras los colores, en la pagina dash.plotly.com se encontraron los checkbox para agregarlos como parte de la gráfica.'),
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dcc.Markdown('Weather'),
        dcc.Markdown('•	En la gráfica de condiciones climáticas, tuvimos un contratiempo debido a que se nos presento un problema, el cual, cuando se seleccionaba la pestaña “Weather” esta automáticamente regresaba a la pestaña que se tenia marcada anteriormente, pero si se escribía el nombre de la pestaña en la url de esta manera si se mantenía estática, se realizo una revisión minuciosa y encontramos que en la consulta de sql en la parte del group by teníamos la variable year de más, al eliminarla se corrigió el problema y la gráfica ya nos mostro los datos. '),
    ], justify='center')
])