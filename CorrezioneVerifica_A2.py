#1. inserire il nome di un comune, cliccare su un bottone ed ottenere le seguenti informazioni:
#    a. mappa geografica con i confini del comune (confini neri, area del comune trasparente)
#    b. area del comune (espressa in km 2 )
#    c. elenco dei comuni limitrofi (in ordine alfabetico)

from flask import Flask, render_template, request, Response
app = Flask(__name__)

import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

comuni = gpd.read_file('/workspace/Flask/Comuni.zip')
province = gpd.read_file('/workspace/Flask/Provincia.zip')
regioni = gpd.read_file('/workspace/Flask/Regioni.zip')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)