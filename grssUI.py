from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
# import dash
# from dash import dcc, html
from dash.dependencies import Input, Output

# df = pd.read_csv('decoded_gps_data2.txt',sep =',', names=['time', 'lat', 'long', 'stat', 'alt', 'temp', 'humid'], index_col=False)


app = Dash(__name__)

# fig = px.line_3d(df, x="lat", y="long", z="alt" , markers = True, text = "time")
# altitude_graph = px.line(df, x="time", y="alt", title="Altitude test", markers=True)
# gpsgraph = px.line_mapbox(df, lat="lat", lon="long")
# temperature_graph = px.line(df, x="time", y="temp", title="Temperature test", markers=True)
# humidity_graph = px.line(df, x="time", y="humid", title="Humidity test", markers=True)

# gpsgraph.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4)

app.layout = html.Div(children=[
    html.H1(children="Michael Ptake :)))))"),

    

    dcc.Graph(
        id='3dline',
        # figure=fig
    ),

    html.H1(children="Altitude"),

    dcc.Graph(
        id='altie',
        # figure=altitude_graph
    ),

    html.H1(children="Temperature"),

    dcc.Graph(
        id='temp',
        # figure=temperature_graph
    ),

    html.H1(children="Humidity"),

    dcc.Graph(
        id='humid',
        # figure=humidity_graph
    ),

    html.H1(children="GPS"),

    dcc.Graph(
        id='gps',
        # figure=gpsgraph
    ), 

    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
    )
])

@app.callback(
    Output('3dline', 'figure'),
    Output('altie', 'figure'),
    Output('temp', 'figure'),
    Output('humid', 'figure'),
    Output('gps', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_alt_graph(n):
    df = pd.read_csv('decoded_gps_data2.txt',sep =',', names=['time', 'lat', 'long', 'stat', 'alt', 'temp', 'humid'], index_col=False)

    fig = px.line_3d(df, x="lat", y="long", z="alt" , markers = True, text = "time")
    altitude_graph = px.line(df, x="time", y="alt", title="Altitude test", markers=True)
    gpsgraph = px.line_mapbox(df, lat="lat", lon="long", zoom=3, height=300)
    gpsgraph.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 41, margin={"r":0,"t":0,"l":0,"b":0})
    # gpsgraph.update_layout(margin={"r":0, "t":0,"1":0,"b":0})
    temperature_graph = px.line(df, x="time", y="temp", title="Temperature test", markers=True)
    humidity_graph = px.line(df, x="time", y="humid", title="Humidity test", markers=True)

    return fig, altitude_graph, temperature_graph, humidity_graph, gpsgraph

if __name__ == '__main__':
    app.run_server(debug=True)




'''
# do curve-fitting
# temp and humidity graph(something like altitude)
# try a 2d longitude/latitude map

# we are receivng
# - a string of numbers

'''