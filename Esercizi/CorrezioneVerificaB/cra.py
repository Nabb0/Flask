#parte iniziale
from flask import Flask,render_template, request, Response, redirect, url_for
app = Flask(__name__)

#Dichiarazioni delle variabili
import io
import pandas as pd
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#Dichiarazioni delle dataframe
stazioni=pd.read_csv('/workspace/Flask/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv', sep=';')
stazionigeo=gpd.read_file('/workspace/Flask/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson')
quartieri = gpd.read_file('/workspace/Flask/ds964_nil_wm.zip')

#Route della homepage
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

#1. Avere un elenco di tutte le stazioni radio che si trovano in un certo quartiere. L’utente sceglie il nome del
#quartiere da un elenco di radiobutton (ordinato in ordine alfabetico) e clicca su un bottone. Il sito risponde con
#l’elenco ordinato in ordine alfabetico delle stazioni radio presenti in quel quartiere

@app.route('/input', methods=['GET'])
def input():
    return render_template('input.html',quartieri=quartieri.NIL.sort_values(ascending=True)) 
    #visualizzazione di tutti i quartieri coi radio in ordine alfabetico

@app.route('/Qtscelto', methods=['GET'])
def Qtscelto():
    Qtscelto = request.args["quartiere"] #prende la variabile del utente
    qt_utente=quartieri[quartieri.NIL.str.contains(Qtscelto)] #controlla se il quartiere scelto dal utente sia valido
    stazioni1=stazionigeo[stazionigeo.within(qt_utente.geometry.squeeze())]#cerca le stazioni al interno del quartiere
    return render_template("qtscelto.html",risultato=stazioni1.to_html())


#2. Avere le stazioni radio presenti in un quartiere. L’utente inserisce il nome del quartiere (anche solo una parte di
#esso), clicca su un bottone e ottiene la mappa del quartiere con un pallino nero sulla posizione delle stazioni
#radio


@app.route("/ricerca", methods=["GET"])
def ricerca():
    return render_template("ricerca.html")

@app.route("/mappa", methods=["GET"])
def mappa():
    global quartiere_ricerca, stazioni_ricerca
    quartiereUtente = request.args["quartiere"]
    quartiere_ricerca = quartieri[quartieri["NIL"].str.contains(quartiereUtente)]
    stazioni_ricerca = stazionigeo[stazionigeo.within(quartiere_ricerca.geometry.squeeze())]
    return render_template("mappa.html", quartiere = quartiere_ricerca.NIL)

#per avere l immagine con le stazione al interno dell qt
@app.route("/mappa.png", methods=["GET"])
def mappapng():
    fig, ax = plt.subplots(figsize = (12,8))

    quartiere_ricerca.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    stazioni_ricerca.to_crs(epsg=3857).plot(ax=ax, facecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

#esercizio 3

@app.route('/numero', methods=['GET'])
def numero():
    #numero stazioni per ogni municipio
    global risultato
    risultato=stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()
    return render_template('elenco.html',risultato=risultato.to_html())

       

@app.route('/grafico', methods=['GET'])
def grafico():
    #costruzione grafico
    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.OPERATORE

    ax.bar(x, y, color = "#304C89")
    #visualizzazione grafico

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype='image/png')





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)