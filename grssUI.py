from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
# import dash_core_components as dcc
# import dash_html_components as html
# import dash
# from dash import dcc, html
from dash.dependencies import Input, Output

# from dash.exceptions import PreventUpdate
# from dash.dependencies import Input, Output, State
# import numpy as np
# import dash_daq as daq

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

app = Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],)
# app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div(
            [
                html.Div(
                    [
                        html.H4("GRSSUI", className="app__header__title"),
                    ],
                    className="app__header__desc",
                ),
            ],
            className="app__header",
        ),
    html.Div(
        [
            # wind speed
            html.Div(
                [
                    dcc.Graph(
                            id='3dline',
                    ),
                    dcc.Graph(
                         id='gps',
                        # config={'staticPlot': True},
                    ), 
                    
                    dcc.Interval(
                            id='interval-component',
                            interval=1*1000, # in milliseconds
                            n_intervals=0,
                    ),
                ],
                className="two-thirds column graph__gps__container",
            ),
            html.Div(
                [
                    # histogram
                    html.Div(
                        [
                            dcc.Graph(
                                id='altie',
                            ),
                        ],
                        className="graph__container first",
                    ),
                    # wind direction
                    html.Div(
                        [
                            dcc.Graph(
                                id='temp',
                            ),
                        ],
                        className="graph__container second",
                    ),

                    html.Div(
                        [
                            dcc.Graph(
                                id='humid',
                            ),
                        ],
                        className="graph__container third",
                    ),
                ],
                className="one-third column altitude__temperature__humidity",
            ),
        ],
        className="app__content",
    ),
],
className="app__container",
)

@app.callback(
    Output('3dline', 'figure'),
    Output('altie', 'figure'),
    Output('temp', 'figure'),
    Output('humid', 'figure'),
    Output('gps', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_alt_graph(n):
    df = pd.read_csv('decoded_gps_data.txt',sep =',', names=['time', 'lat', 'long', 'stat', 'alt', 'temp', 'humid'], index_col=False)

    fig = px.line_3d(df, x="lat", y="long", z="alt" , markers = True, text = "time")    
    fig.update_layout(scene = dict(xaxis = dict(nticks=10, range=[-1000,8000]),
                                   yaxis = dict(nticks=10, range=[-1000,8000]),
                                   zaxis = dict(nticks=10, range=[0,300])),
                        uirevision='constant',
                        height=300, width=700,)
    altitude_graph = px.line(df, x="time", y="alt", title="Altitude test", markers=True, height=450, width=700, range_y=(10,130000))

    gpsgraph = px.line_mapbox(df, lat="lat", lon="long", zoom=2, height=650, width=650)
    gpsgraph.update_layout(mapbox_style="open-street-map", 
                           mapbox_zoom=2, 
                           mapbox_center_lat = 43, 
                           mapbox_center_lon = -75, 
                           mapbox_bounds_east=-69,
                           mapbox_bounds_north=46,
                           mapbox_bounds_south=38,
                           mapbox_bounds_west=-81,
                           margin={"r":0,"t":0,"l":0,"b":0},
                        #    bounds=[[38.657436, -82.014513], [45.753491, -68.914279]],
                        #    bounds=(41.763936,-73.113437,-75.400669,42.47759),
                        #    bounds=dict(bounds_east=41.763936,bounds_north=-73.113437,bounds_south=-75.400669,bounds_west=42.47759),
                           uirevision='constant')
    # gpsgraph.update_mapboxes(bounds=dict(bounds_east=41.763936,bounds_north=-73.113437,bounds_south=-75.400669,bounds_west=42.47759))
    # gpsgraph.update_mapboxes(bounds_east=41.763936,bounds_north=-73.113437,bounds_south=-75.400669,bounds_west=42.47759)
    
    temperature_graph = px.line(df, x="time", y="temp", title="Temperature test", markers=True, height=450, width=700)
    humidity_graph = px.line(df, x="time", y="humid", title="Humidity test", markers=True, height=450, width=700)

    return fig, altitude_graph, temperature_graph, humidity_graph, gpsgraph


if __name__ == '__main__':
    app.run_server(debug=True)
