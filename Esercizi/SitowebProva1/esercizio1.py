#1. Realizzare un server web che come home page presenti tre immagini della stessa dimensione una di fianco all'altra. 
#La prima immagine deve avere a che fare con le previsioni del tempo, la seconda deve contenere un libro e la terza deve contenere un calendario. 
#Utilizzare un file css per definire la grafica della pagina.

from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

import random
from datetime import datetime
@app.route('/')
def hello_world():
    return render_template("Esercizio.html")

#2. modificare il server precedente per far sì che quando l'utente clicca sulla prima immagine vengano fornite le previsioni del tempo. 
#Visto che, comunque, le previsioni dei vari servizi metereologici sono sempre sbagliate, il nostro server genera un numero casuale compreso tra 0 e 8: se il numero è minore di 2
#la previsione è "pioggia", se è compreso tra 3 e 5 la previsione è "nuvoloso", se è maggiore di 5 la previsione è "sole".
#Abbinare ad ogni previsione un'immagine adatta. Utilizzare un css per definire la grafica. La route per accedere al serizio deve essere /meteo

@app.route("/meteo")
def meteo():
    nRandom = random.randint(0,8)
    if nRandom <= 2:
        immagine = "/static/images/Troppa-pioggia-a-livello-globale-aumentano-le-precipitazioni-estreme_articleimage.jpg"
    elif nRandom <= 5:
        immagine = "/static/images/meteo-nuvole-185033.660x368.jpg"
    else:
        immagine = "/static/images/Sole-Spiaggia-Mare.jpg"
    return render_template("Meteo.html", meteo=immagine)

 #3. modificare il server precedente per far sì chhe quando l'utente clicca sulla seconda immagine il server web risponde con una frase celebre,
 #scelta casualmente da un elenco di 10 frasi (per ispirazione  https://www.frasimania.it/frasi-corte/). 
 #Utilizzare una struttura dati adatta per contenere le frasi e gli autori Il sito deve visualizzare la frase con una certa grafica (a scelta) e anche l'autore (da visualizzare con una grafica diversa).
 # Utilizzare un file css per definire la grafica della pagina. 
 #.La route per accedere al serizio deve essere /frasicelebri
@app.route("/frasicelebri")
def libro():
    frasi = [{"Autore": "Frida Kahlo" , "Frase": "Innamorati di te, della vita e dopo di chi vuoi." },
    {"Autore": "Dietrich Bonhoeffer" , "Frase": "Contro la stupidità non abbiamo difese."},
    {"Autore": "Charlie Chaplin" , "Frase": "Un giorno senza un sorriso è un giorno perso."},{"Autore": "Francesco Bacone" , "Frase": "Sapere è potere."},
    {"Autore": "Italo Calvino" , "Frase": "Il divertimento è una cosa seria."},{"Autore": "Lewis Carroll" , "Frase": "Qui siamo tutti matti."},
    {"Autore": "Johann Wolfgang von Goethe", "Frase": "Il dubbio cresce con la conoscenza."},{"Autore": "Luis Sepùlveda" , "Frase": "Vola solo chi osa farlo."},
    {"Autore": "Lucio Anneo Seneca", "Frase": "Se vuoi essere amato, ama."},{"Autore": "Voltaire", "Frase": "Chi non ha bisogno di niente non è mai povero."}]
    fRandom = random.randint(0,9)
    return render_template("frasicelebri.html", autore = frasi[fRandom]["Autore"], frase = frasi[fRandom]["Frase"])

#4. modificare il server precedente per far sì che quando l'utente clicca sulla terza immagine venga visualizzato il numero di giorni che mancano alla fine della scuola. 
# Utilizzare un file css per definire la grafica della pagina.
#La route per accedere al serizio deve essere /quantomanca
@app.route("/quantomanca")
def calendario():
    now = datetime.now()
    school = datetime(2022,6,8)
    return render_template("calendario.html", data = (school - now).days)

#ultima riga
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)