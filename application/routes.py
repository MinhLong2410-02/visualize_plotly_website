from flask import Flask, render_template, url_for
import pandas as pd
import json, plotly, plotly.express as px
from .create_dash import init_dashboard
app = Flask(__name__)
init_dashboard(app)

@app.route("/")
@app.route("/index")
@app.route("/table")
def index():
    df = px.data.medals_wide()
    fig1 = px.bar(df, x = 'nation', y = ['gold', 'silver', 'bronze'], title = "Wide-Form Input")
    graph1JSON = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)
    
    df = px.data.iris()
    fig2 = px.scatter_3d(df, x = "sepal_length", y = 'sepal_width', z = "petal_width", color = 'species', title = "Iris Dataset")
    graph2JSON = json.dumps(fig2, cls = plotly.utils.PlotlyJSONEncoder)
    
    
    return render_template("table.html", title = 'Home', graph1JSON = graph1JSON, graph2JSON = graph2JSON)


@app.route("/about")
def about():
    return render_template("about.html")
