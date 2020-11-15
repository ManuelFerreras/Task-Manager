from flask import Flask
from flask import request
from flask import render_template
from flask import Response
from flask import json
from flask import redirect
from flask import url_for
from flask import make_response

import json

mails = []

f = open('mails.json')
mails = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
        
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/loginForm', methods=['POST'])
def iniciarSesion():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        print(data['mail'])
        if checkMailAndPass(data['mail'], data['contrasena']) == True:
            return Response(json.dumps({'mensaje':'Usuario correcto'}), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'mensaje':'Usuario incorrecto'}), status=401, mimetype='application/json')
        
@app.route('/registerForm', methods=['POST'])
def registrarCuenta():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        print(data['mail'])
        if checkMail(data['mail']) == False:
            mails.append(data)
            saveJson()
            return Response(json.dumps({'mensaje':'Usuario Creado Correctamente'}), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'mensaje':'Ya se ha creado un usuario con ese email'}), status=409, mimetype='application/json')

def checkMailAndPass(mail, password):
    for mailsCount in mails:
        if mail == mailsCount['mail'] and password == mailsCount['contrasena']:
            return True
    return False

def checkMail(mail):
    for mailsCount in mails:
        if mail == mailsCount['mail']:
            return True
    return False

def saveJson():
    global mails
    with open('mails.json', 'w') as f:
        json.dump(mails, f)


if __name__ == '__main__':
    app.run()
