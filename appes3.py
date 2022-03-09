#realizzare un server web che permetta di conoscere capoluoghi di regione l'utente inaerisce il nome della regione 
#e il proggramma restituisce il nome dell capoluogo di regine 
#caricare i capoluogi e le regioni in una opportuta struttura dati
#modificare poin l es precedente per permettere al utente di inserire un capoluogo e di avere la regione in cui si trova
#l utente sceglie se avere la regione o il capo luogo selezionado un radio button 

from flask import Flask,render_template,request
app = Flask(__name__)


capoluoghiRegione = {"Abruzzo": "Aquila", "Basilicata": "Potenza", "Calabria": "Catanzaro", "Campania": "Napoli", "Emilia-Romagna": "Bologna", "Friuli-venezia-Giulia": "Trieste", "Lazio": "Roma", "Liguaria": "Genova", "Lombardia": "Milano", "Marche": "Ancona", "Molise": "Campobasso", "Piemonte": "Torino", "Puglia": "Bari", "Sardegna": "Cagliari", "Sicilia": "Palermo", "Toscana": "Firenze", "Trentino-Alto Adige": "Trento", "Umbria": "Perugia", "valle d'Aosta": "Aosta", "Veneto": "Venezia"}


@app.route('/', methods=['GET'])
def hello_world():
   return render_template('RegioneOcapo.html')
 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)