import json, plotly, plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
df = pd.read_csv("./weather-history.csv", parse_dates =["date"], index_col ="date") 
ele = {'tmin': 'Nhiệt độ thấp nhất', 'tmax': 'Nhiệt độ cao nhất', 'prcp': 'Lượng mưa', 'snwd': 'Lượng tuyết rơi', 'awnd': 'Tốc độ gió trung bình'}
yearly = df.resample('Y').sum()


def jsonify(fig):
    return json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    
def graph1():
    fig = go.Figure()
    fig.add_trace(go.Histogram(x = df['tmin'], name = ele['tmin']))
    fig.add_trace(go.Histogram(x = df['tmax'], name = ele['tmax']))
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        barmode='overlay',
        title={
            'text': f'<b>Tổng nhiệt độ</b>',
            'y':0.8,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_color="red",
        font_color="yellow",
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="gray",
            font_size=16,
            font_family="Rockwell"),
        showlegend = False
    )
    return jsonify(fig)

def graph2():
    y = 2020
    year = df[df.index.year == y]
    monthly = year.resample('M').sum()
    y_m = monthly.tmax.max()
    x_m = monthly.loc[monthly.tmax == y_m].index.month[0]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=monthly.index.month, y=monthly['tmin'],
        name=ele['tmin'],
        connectgaps=True)
    )

    fig.add_trace(go.Scatter(x=monthly.index.month, y=monthly['tmax'],
        name=ele['tmax'],
        connectgaps=True,)
    )
    fig.update_layout(
        barmode='overlay',
        title_font_color="red",
        font_color="yellow",
        hovermode="x unified",
        hoverlabel=dict(
        bgcolor="gray",
        font_size=16,
        font_family="Rockwell"),
        showlegend = False
    )
    fig.add_annotation(
        x=x_m,
        y=y_m,
        xref="x",
        yref="y",
        text="max=2816",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#00e600",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
        )
    fig.update_layout(yaxis_title=None, xaxis_title=None, margin=dict(l=5, r=5, t=5, b=5))
    return jsonify(fig)

def graph3():
    fig = go.Figure()
    for y in df.index.year.unique():
        year = df[df.index.year == y]
        monthly = year.resample('M').sum()
        y_m = monthly.prcp.max()
        x_m = monthly.loc[monthly.prcp == y_m].index.month[0]
        fig.add_trace(go.Scatter(x=monthly.index.month, y=monthly['prcp'],
            name=f'năm: {y}',
            connectgaps=True)
        )
    return jsonify(fig)

def graph4():
    year = df[df.index.year == 2020]
    monthly = year.resample('M').sum()
    fig = px.bar(x = monthly.index.month, y=monthly['prcp'],
                text_auto=True,
                labels={
                    "x": "",
                    "y": ""
                    })
    fig.update_layout(
        barmode='overlay',
        title_font_color="red",
        font_color="yellow",
        showlegend = False,
        plot_bgcolor='black'
    )
    fig.update_layout(yaxis_title=None, xaxis_title=None, margin=dict(l=5, r=5, t=5, b=5))
    return jsonify(fig)

def graph5():
    fig = go.Figure(go.Barpolar(
        r=yearly.awnd,
        theta=list(map(lambda x: str(x), yearly.index.year.values)),
        width=[0.8, 0.6, 0.4, 0.5, 0.3, 0.2],
        marker_color=["#4618DF", '#709BFF', '#2AC93A', '#FFAA70', '#D50909', '#FFDF70'],
        marker_line_color="yellow",
        marker_line_width=2,
        opacity=0.8
    ))

    return jsonify(fig)