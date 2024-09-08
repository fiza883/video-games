from flask import Flask, render_template
import pandas as pd
import numpy as np
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
app = Flask(__name__)


def load_dataset():
    df=pd.read_csv(r'C:\Users\LENOVO\Documents\Video-Game-Analysis\Dataset\vgsales.csv')
    df.Publisher.fillna('Electronic Arts',inplace=True)
    df.Year.fillna(2009.0,inplace=True)
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/platform')
def platform():
    return render_template('platform.html')

@app.route('/Publisher')
def publisher():
    return render_template('Publisher.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/tool')
def tools():
    return render_template('tool.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 