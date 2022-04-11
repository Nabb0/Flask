
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
  global qt_utente
  qt_utente=request.args['quartiere']
  return render_template('sceltaquartiere.html')

  

@app.route('/mappa', methods=['GET'])
def mappa():
  scelta = request.args['scelta']
  
  if scelta == '0':
        return render_template('mappafinale.html')
  else: 
        return render_template('attorno.html')
  
@app.route("/mappa.png", methods=["GET"])
def mappapng():

    fig, ax = plt.subplots(figsize = (12,8))
    
    quartiere=quartieri[quartieri.NIL.str.contains(qt_utente)]
    quartiere.to_crs(epsg=3857).plot(ax=ax)
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route("/mappa2.png", methods=["GET"])
def mappapng2():

    fig, ax = plt.subplots(figsize = (12,8))
    
    
    Qt=quartieri[quartieri.NIL.str.contains(qt_utente)]
    QtConfinanati=quartieri[quartieri.touches(Qt.geometry.squeeze())]
    QtConfinanati.to_crs(epsg=3857).plot(ax=ax)
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)