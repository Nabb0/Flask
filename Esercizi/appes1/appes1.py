# eseguire un se4rver web che permetta di effetuare il login 
# l'utente inserisce il username e la password :
#se lo username e admin e la password e xxx123# :
#il sito ci saluta con un messagio di benvenuto
#altrimenti ci da un messagio d errore 
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('usernameepassword.html')

@app.route('/data', methods=['GET']) ##PER IL LOGIN SI USA IL POST 
def data():
    Username = request.args['Username']
    Password = request.args['Password']
    
    if Username == ('admin') and Password == ('xxx123#'):
     return render_template('welcome.html',username=Username)
    else:
     return render_template('Negato.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)