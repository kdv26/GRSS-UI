from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from filewriter import writeOne

app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                            id='3dline',
                    ),
                ], width=3),
                dbc.Col([
                    dcc.Graph(
                         id='gps',
                        # config={'staticPlot': True},
                    ), 
                ], width=4),
                dbc.Col([
                    dcc.Graph(
                        id='altie',
                    ),
                ], width=4),
            ], align='center'), 

            html.Br(),

            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id='temp',
                    ),
                ], width=4),
                dbc.Col([
                    dcc.Graph(
                        id='humid',
                    ), 
                ], width=4),
            ], align='center'),   
            
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Img(
                        id='pics',
                    ),
                ], width=4),
            ], align='center'),

        ]), color = 'dark',
    ),

    dcc.Interval(
            id='interval-component',
            interval=1*1000, # 1 sec intervals
            n_intervals=0,
    ),

],)

@app.callback(
    Output('3dline', 'figure'),
    Output('altie', 'figure'),
    Output('temp', 'figure'),
    Output('humid', 'figure'),
    Output('gps', 'figure'),
    Output('pics', 'src'),
    Input('interval-component', 'n_intervals')
)
def update_alt_graph(n):
    df = pd.read_csv('decoded_gps_data.txt',sep =',', names=['time', 'lat', 'long', 'stat', 'alt', 'temp', 'humid'], index_col=False)

    fig = px.line_3d(df, x="lat", y="long", z="alt" , markers = True, text = "time")    
    fig.update_layout(scene = dict(xaxis = dict(nticks=5, range=[35,45]),
                                   yaxis = dict(nticks=5, range=[-90,-60]),
                                   zaxis = dict(nticks=10, range=[10,130000])),
                        uirevision='constant',
                        margin={"r":0,"t":0,"l":0,"b":0},
                        height=350, width=350,)
    # st.plotly_chart(fig, use_container_width=True)

    
    altitude_graph = px.line(df, x="time", y="alt", title="Altitude test", markers=True, height=400, width=600, range_y=(10,130000))
    altitude_graph.update_layout(margin={"r":40,"t":50,"l":0,"b":0}, uirevision='constant')

    gpsgraph = px.line_mapbox(df, lat="lat", lon="long", zoom=2, height=400, width=470)
    gpsgraph.update_layout(mapbox_style="open-street-map", 
                           mapbox_zoom=2, 
                           mapbox_center_lat = 43, 
                           mapbox_center_lon = -75, 
                           mapbox_bounds_east=-69,
                           mapbox_bounds_west=-81,
                           mapbox_bounds_north=46,
                           mapbox_bounds_south=38,
                           margin={"r":0,"t":0,"l":0,"b":0},
                           uirevision='constant')
    
    temperature_graph = px.line(df, x="time", y="temp", title="Temperature test", markers=True, height=250, width=500)
    temperature_graph.update_layout(margin={"r":40,"t":50,"l":0,"b":0}, uirevision='constant')

    humidity_graph = px.line(df, x="time", y="humid", title="Humidity test", markers=True, height=250, width=500)
    humidity_graph.update_layout(margin={"r":40,"t":50,"l":0,"b":0}, uirevision='constant')
  
    return fig, altitude_graph, temperature_graph, humidity_graph, gpsgraph, app.get_asset_url(str(n) + '.jpg')

if __name__ == '__main__':
    app.run_server(debug=True)
