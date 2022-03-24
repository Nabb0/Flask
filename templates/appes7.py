#Si vuole realizzare un sito web per insegnare la geografia.
# # Il sito deve presentare una serie di radiobutton contenenti i nomi delle regioni, caricate da un opportuno dataframe.
# # L'utente seleziona una regione, clicca su un bottone e ottiene l'elenco delle province di quella regione in un menù a tendina (caricate anch'esse da un dataframe).#
#  Seleziona quindi una provincia, clicca su un bottone e ottiene l'elenco dei comuni di quella provincia in ordine alfabetico.
#Facoltativo
#I nomi dei comuni sono link ipertestuali: se l'utente clicca su un comune ottiene la mappa del comune 

from flask import Flask, render_template, send_file, make_response, url_for, Response,request
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
provincia = gpd.read_file('/workspace/Flask/Provincia.zip')
regioni = gpd.read_file('/workspace/Flask/Regioni.zip')
ripgeo = gpd.read_file('/workspace/Flask/RipGeo.zip')

@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')











if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)