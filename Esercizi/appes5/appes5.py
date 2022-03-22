#si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta.
#l'utente deve poter inserire il nome della squadra e la data di fondazione e la città.
#deve inoltre poter effetuare delle ricerche inserendo uno dei valori delle colonne e ottenendo i dati presenti.

from flask import Flask, render_template,request
app = Flask(__name__)
import pandas as pd

@app.route('/', methods=['GET'])
def home():
    return render_template('indexs.html')


@app.route('/formricerca', methods=['GET'])
def formricerca():
    return render_template('formricerca.html')


@app.route('/ricerca', methods=['GET'])
def ricerca():
    indice = request.args['indice']
    radio = request.args['sel']
    df1 = pd.read_csv('squads_database.csv')
    if indice not in df1[radio].to_list():
        return render_template('error.html')
    
    if radio == 'squadra':
        return df1[df1['squadra'].str.contains(indice)].to_html()
    if radio == 'anno':
        return df1[df1['anno'].str.contains(indice)].to_html()
    if radio == 'citta':
        return df1[df1['citta'].str.contains(indice)].to_html()
    
    #return render_template('indexs2.html')


@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('indexs1.html')

@app.route('/dati', methods=['GET'])
def dati():
    
    
    squadra = request.args['Squadra']
    anno = request.args['Anno']
    citta = request.args['Citta']
    
    
    df1 = pd.read_csv('squads_database.csv')
    
    
    nuovi_dati = {'squadra':squadra,'anno':anno,'citta':citta}
    
    df1 = df1.append(nuovi_dati,ignore_index=True)
    
    
    df1.to_csv('squads_database.csv', index=False)
    rdf1 = df1.to_html()
    #return df1.to_html()
    return render_template('indexs2.html', tables=[rdf1], titles=[''])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)