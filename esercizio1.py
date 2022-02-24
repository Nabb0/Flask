#1. Realizzare un server web che come home page presenti tre immagini della stessa dimensione una di fianco all'altra. 
#La prima immagine deve avere a che fare con le previsioni del tempo, la seconda deve contenere un libro e la terza deve contenere un calendario. 
#Utilizzare un file css per definire la grafica della pagina.

from flask import Flask, render_template
app = Flask(__name__)

import random

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

#ultima riga
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)