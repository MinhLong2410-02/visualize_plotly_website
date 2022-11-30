from flask import Flask, render_template, url_for
import pandas as pd
import json, plotly, plotly.express as px
from .create_dash import init_dashboard
from .eda_dash import *
app = Flask(__name__)
init_dashboard(app)

@app.route("/")
@app.route("/index")
@app.route("/table")
def index():
    graph1JSON = graph1()
    graph2JSON = graph2()
    graph3JSON = graph3()
    graph4JSON = graph4()
    graph5JSON = graph5()
    
    return render_template("table.html", title = 'Home', 
                           graph1JSON = graph1JSON, 
                           graph2JSON = graph2JSON,
                           graph3JSON = graph3JSON,
                           graph4JSON = graph4JSON,
                           graph5JSON = graph5JSON)


@app.route("/about")
def about():
    return render_template("about.html")
