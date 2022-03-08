#realizzare un sito web che permetta la registrazione degli utenti 
#l utente inserisce il nome, username , una password,
#la conferma della password e il sesso
# se le informazioni sono corrette il sito slava le informazioni in una struttura dati opportuna (lista dizzionari)
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('Registrazionees2.html')

@app.route('/data', methods=['GET']) ##PER IL LOGIN SI USA IL POST 
def data():
    Username = request.args['Username']
    Password = request.args['Password']
    Password2 = request.args['Password2']
    Sex = request.args['Sex']
    
    if Password ==  Password2:
        return render_template('regcomp.html')
    else:
        return render_template('nn.html')

@app.route('/Login', methods=['GET']) ##PER IL LOGIN SI USA IL POST 
def login():
    Username = request.args['Username']
    Password = request.args['Password']
    
    if Username == ('admin') and Password == ('xxx123#'):
     return render_template('Login.html',username=Username)
    else:
     return render_template('negato.html')
     
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

#seconda parte prevedere la possibilita di fare il login 
#inserendo username e password se sono corrette fornire un messagio di benvenuto diverso al seconda del sesso 