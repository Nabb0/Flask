
from flask import Flask,render_template, request, Response, redirect, url_for
app = Flask(__name__)

import io
import pandas as pd
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quartieri = gpd.read_file('/workspace/Flask/ds964_nil_wm.zip')


#Home
@app.route('/', methods=['GET'])
def home():
  global lista_qt
  lista_qt= quartieri.NIL.to_list() # DEVO PER FORZA TRASFORMARE IN LISTA
  return render_template('home1.html',quartieri=lista_qt)

@app.route('/sceltaquartiere', methods=['GET'])
def sceltaquartiere():
  return render_template('sceltaquartiere.html')

  

@app.route('/mappa', methods=['GET'])
def mappa():
  scelta = request.args['scelta']
  
  if scelta == '0':
        return render_template('mappafinale.html')
  else: 
        return render_template('attorno.html')
  
  return render_template('mappafianle.html')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)