#realizzare un sito web che permetta la registrazione degli utenti 
#l utente inserisce il nome, username , una password,
#la conferma della password e il sesso
# se le informazioni sono corrette il sito slava le informazioni in una struttura dati opportuna (lista dizzionari)

#seconda parte prevedere la possibilita di fare il login 
#inserendo username e password se sono corrette fornire un messagio di benvenuto diverso al seconda del sesso 
from flask import Flask,render_template, request
app = Flask(__name__)
lista=[] #struttura dati temporanea va salvata sulla ram 
@app.route('/', methods=['GET']) #homepage 
def es():
    return render_template('Registrazionees2.html')


@app.route('/dates', methods=['GET'])
def dates():
    Name = request.args['Name'] #request = i dati dal client
    Pass = request.args['Pass']
    Username = request.args['User']
    Confirm = request.args['Conf']
    Sex = request.args['Sex']

    

    if Pass==Confirm:
       lista.append({'Name':Name,'Username':Username,'Pass':Pass,'Sex':Sex})
       print(lista)
       if Sex=='M':
           return render_template('WelcomeUomo.html', nome=Name)
       else:
           return render_template('WelcomeDonna.html', nome=Name)

@app.route('/login', methods=['GET'])
def login():
    return render_template('Login.html')

@app.route('/login2', methods=['GET'])
def login2():
    username_log=request.args['Username']
    Pass_log=request.args['Pass']
    for utente in lista:
        if utente['Username'] == username_log and utente['Pass'] == Pass_log:
            if utente['Sex']== 'M':
                return render_template('WelcomeUomo.html',nome=utente['Name'])
            else:
                return render_template('WelcomeDonna.html',nome=utente['Name'])
     
    return render_template('nn.html', messaggio='username o password sbagliati')
       
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)