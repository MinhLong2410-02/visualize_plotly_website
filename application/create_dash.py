import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go



df = pd.read_csv('weather-history.csv', parse_dates =["date"], index_col ="date")
df.fillna(method='bfill', inplace=True)
ele = {'tmin': 'Nhiệt độ thấp nhất', 'tmax': 'Nhiệt độ cao nhất', 'prcp': 'Lượng mưa', 'snwd': 'Lượng tuyết rơi', 'awnd': 'Tốc độ gió trung bình'}

def init_dashboard(flask_app):
    # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = Dash(
        url_base_pathname="/dash/",
        name = "Dashboard",
        server = flask_app, 
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )
    
    app.layout = html.Div([
        html.H1(children='Dash Board', style = {'text-align': 'center'}),
        dbc.Row([
            html.H6('Chọn thuộc tính'),
            dbc.Col([
                dcc.Dropdown(id="element", 
                            options=[{"label": "Nhiệt độ thấp nhất", "value": "tmin"},
                                    {"label": "Nhiệt độ cao nhất", "value": "tmax"},
                                    {"label": "Lượng mưa", "value": "prcp"},
                                    {"label": "Lượng tuyết rơi", "value": "snow"},
                                    {"label": "Độ sâu lớp tuyết", "value": "snwd"},
                                    {"label": "Tốc độ gió trung bình", "value": "awnd"}],
                            multi=False,
                            value="prcp",
                            style={'width': "40%"})
            ])

            ,html.H6('Chọn kiểu giá trị'),
            dbc.Col([
                dcc.Dropdown(id="val", 
                            options=[{"label": "Nhỏ nhất", "value": "min"},
                                    {"label": "Lớn nhất", "value": "max"},
                                    {"label": "Tổng", "value": "sum"},
                                    {"label": "Trung bình", "value": "mean"},
                                    {"label": "Trung vị", "value": "median"}],
                            multi=False,
                            value="sum",
                            style={'width': "40%"})
            ])
        ]),
        dbc.Row([
            dcc.Graph(id="graph1")
        ]),

        dbc.Row([
            html.H6('Chọn năm'),
            dbc.Col([
                dcc.Dropdown(id="year", 
                            options=[{"label": "2017", "value": 2017},
                                    {"label": "2018", "value": 2018},
                                    {"label": "2019", "value": 2019},
                                    {"label": "2020", "value": 2020},
                                    {"label": "2021", "value": 2021},
                                    {"label": "2022", "value": 2022}],
                            multi=False,
                            value="2021",
                            style={'width': "40%"})
            ]),
        dbc.Row([
            dcc.Graph(id="graph2")
        ]),
    ])
    ])

    @app.callback(Output("graph1", "figure"), 
                [Input("val", "value"), Input("element", "value")])
    def display_graph(val, element):
        if val == 'sum':
            yearly = df.resample('Y').sum()
        elif val == 'min':
            yearly = df.resample('Y').min()
        elif val == 'max':
            yearly = df.resample('Y').max()
        elif val == 'mean':
            yearly = df.resample('Y').mean()
        elif val == 'median':
            yearly = df.resample('Y').median()
        # yearly = df.resample('Y').sum()
        fig = px.bar(yearly, y=element, title = f'Biểu đồ {ele[element]} theo từng năm'.upper())
    
        return fig

    @app.callback(Output("graph2", "figure"), 
                Input("year", "value"))
    def display_graph(year):
        df_y = df[df.index.year == year]
        monthly = df_y.resample('M').sum()
        fig = px.bar(monthly, y=monthly['prcp'], title = f'Biểu đồ tổng lượng mưa năm {year}')
        return fig
    
    return app
