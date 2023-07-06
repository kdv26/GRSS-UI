from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
# from filewriter import writeOne
import json
import numpy as np
import plotly.graph_objects as go
import urllib.request
import dash_daq as daq

app = Dash(__name__, 
           meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],)

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

app.layout = html.Div([

    html.Div(
        [
            html.Div(
                [
                    html.H4("GRSS UI", className="app__header__title"),
                ],
                className="app__header__desc",
            ),
        ],
        className="app__header",
    ),

    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [html.H6("3D Position Graph", className = "graph__title",)]
                            ), 
                        
                            dcc.Graph(
                                id='3dline',
                            ),
                    
                        ], 
                        className = "graph__container first",
                    ),

                    html.Div(
                        [
                            html.Div(
                                [html.H6("GPS", className = "graph__title",)]
                            ), 

                            dcc.Graph(
                                id='gps',
                            ),
                        ], 
                        className = "graph__container second",
                    ), 
                ],
                className = "one-third column histogram__direction",
            ),

            html.Div(
                [
                    html.Div(
                        [
                            html.Div
                            (
                                [html.H6("Altitude Line Graph", className = "graph__title")]
                            ),

                            dcc.Graph(
                                id='altie',
                            ),
                        ],
                        className = "linegraph2d__container",
                    ),

                    html.Div(
                        [
                            html.Div(
                                [html.H6("Temperature Line Graph", className = "graph__title")]
                            ),

                            dcc.Graph(
                                id='temp',
                            ),
                        ],
                        className = "linegraph2d__container",
                    ),

                    html.Div(
                        [
                            html.Div(
                                [html.H6("Humidity Line Graph", className = "graph__title")]
                            ),

                            dcc.Graph(
                                id='humid',
                            ),
                        ],
                        className = "linegraph2d__container",
                    ),
                ],
                className = "one-third column",
            ),

            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [html.H6("Altitude", className = "graph__title",)]
                            ), 
                        
                            daq.Tank(
                                id="altvert",
                                label="Vertical Altitude",
                                min=0,
                                max=20000,
                                value=0,
                                units="kilometers",
                                height = 800,
                                showCurrentValue=True,
                                # color="#303030",
                            )
                        ], 
                        className = "graph__container",
                    ),
                ],
                className = "one-third column",
            ),
        ],
        className="app__content",
    ),

    dcc.Interval(
            id='interval-component',
            interval=1*1000, # 1 sec intervals
            n_intervals=0,
    ),
],
className="app__container",
)

'''
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
                # dbc.Col([
                #     html.Img(
                #         id='pics',
                #     ),
                # ], width=8),
                dbc.Col([
                    dcc.Graph(
                        id='altvert',
                    ), 
                ], width=3),
            ], align='center'),

        ]), color = 'dark',
    ),

        dcc.Interval(
            id='interval-component',
            interval=1*1000, # 1 sec intervals
            n_intervals=0,
    ),
'''

@app.callback(
    Output('3dline', 'figure'),
    Output('altie', 'figure'),
    Output('temp', 'figure'),
    Output('humid', 'figure'),
    Output('gps', 'figure'),
    Output('altvert', 'value'),
    # Output('pics', 'src'),
    Input('interval-component', 'n_intervals')
)
def update_alt_graph(n):
    '''
    df = pd.read_csv('decoded_gps_data2.txt',sep =',', 
                     names=['time', 'lat', 'long', 'stat', 'alt', 'temp', 'humid'], 
                     converters={'lat' : str, 'long' : str},
                     index_col=False)
   
    # The converters argument in read_csv changes the lat and long variables into strings so that leading 0's are preserved
    df.fillna(value=0, inplace=True)
    df.replace(to_replace =
               {'lat' : {'' : '0000.0000'}, 
                'long' : {'' : '00000.0000'}
                },
                inplace=True)
    
    # print(f"df:\n{df}")
    # Converting LATS
    raw_lat = df.lat.str
    lat_degrees = raw_lat[:2]
    lat_minutes = raw_lat[2:]
    #Convert the minutes into degrees by dividing by 60
    #Change type to float first
    lat_min_to_degrees = lat_minutes.astype("float") / 60
    # Add the converted minutes to the degrees
    converted_lats = lat_degrees.astype("float") + lat_min_to_degrees
    df["lat"] = converted_lats

    # Converting LONGS
    raw_long = df.long.str
    long_degrees = raw_long[:3]
    long_minutes = raw_long[3:]    
    #Convert the minutes into degrees by dividing by 60
    #Change type to float first
    long_min_to_degrees = long_minutes.astype("float") / 60
    # Add the converted minutes to the degrees
    converted_longs = long_degrees.astype("float") + long_min_to_degrees
    df["long"] = (converted_longs * -1)
    '''

    # '''
    df = pd.read_csv('decoded_gps_data.txt', sep = ',', 
                     names=['time', 'lat', 'long', 'stat', 'alt', 'temp', 'humid'], 
                     index_col=False)
    # '''

    # '''
    fig = px.line_3d(df, x="lat", y="long", z="alt" , markers = True, text = "time")    
    fig.update_layout(scene = dict(xaxis = dict(nticks=5, range=[35,45]),
                                   yaxis = dict(nticks=5, range=[-90,-60]),
                                   zaxis = dict(nticks=10, range=[10,20000])),
                        uirevision='constant',
                        margin={"r":0.8,"t":0.4,"l":0.8,"b":0.4},
                        height=400, width=550,)    
    # '''

    '''
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
                            x=df['long'], y=df['lat'], z=df['alt'], 
                            uirevision='constant', 
                            marker=dict(size=4)))
    fig.update_layout(scene = dict(xaxis = dict(nticks=5, range=[-90,-60]),
                                   yaxis = dict(nticks=5, range=[35,45]),
                                   zaxis = dict(nticks=5, range=[10,20000])),
                        margin={"r":0,"t":0,"l":0,"b":0},
                        height=350, width=350,)
    '''

    # st.plotly_chart(fig, use_container_width=True)

    altitude_graph = px.line(df, x="time", y="alt", title="Altitude test", markers=True, height=250, width=500, range_y=(10,20000))
    altitude_graph.update_layout(margin={"r":40,"t":50,"l":0,"b":0}, uirevision='constant')

    # gpsgraph = px.line_mapbox(df, lat="lat", lon="long")
    gpsgraph = px.line_mapbox(df, lat="lat", lon="long", zoom=2, height=400, width=550)
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
    
    altvertvalue = df['alt'].tail(n=1)
    
    temperature_graph = px.line(df, x="time", y="temp", markers=True, height=250, width=500)
    temperature_graph.update_layout(margin={"r":40,"t":50,"l":0,"b":0}, uirevision='constant')

    humidity_graph = px.line(df, x="time", y="humid", title="Humidity test", markers=True, height=250, width=500)
    humidity_graph.update_layout(margin={"r":40,"t":50,"l":0,"b":0}, uirevision='constant')

    # writeOne(n)

    # return fig, altitude_graph, temperature_graph, humidity_graph, gpsgraph, app.get_asset_url(str(n) + '.jpg')
    return fig, altitude_graph, temperature_graph, humidity_graph, gpsgraph, altvertvalue
    # return fig, gpsgraph

if __name__ == '__main__':
    app.run_server(debug=True)
