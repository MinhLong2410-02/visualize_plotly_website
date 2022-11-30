import json, plotly, plotly.express as px
import pandas as pd

df = pd.read_csv("./weather-history.csv", parse_dates =["date"], index_col ="date") 

def graph1():
    global df
    yearly = df.resample('Y').sum()
    yearly['year'] = yearly.index.year.to_list()
    fig = px.bar(df, x = yearly.index.year, y = yearly.prcp, title = "Lượng mưa thay đổi qua các năm")
    fig.update_layout(xaxis_title="Các năm", yaxis_title="Lượng mưa")
    return json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
