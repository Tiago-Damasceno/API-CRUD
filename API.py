from flask import Flask, render_template
from forms import FormLogin, FormCriarConta
import os

app = Flask('__name__')

lista_usuarios = ['Paula', 'Felipe', 'Eloá', 'Raví', 'Tiago']

app.secret_key = os.environ.get('FLASK_SECRET_KEY','86a80337ce81d80a3503f02eb197c8c5')


@app.route('/')
def homepage(name = None):
    return render_template("homepage.html", name = name)

@app.route('/contatos')
def contatos(name = None):
      return render_template("contatos.html", name = name)

@app.route('/usuarios')
def usuarios(name = None):
    return render_template("usuarios.html", name = name, lista_usuarios = lista_usuarios)

@app.route('/login')
def login(name = None):

    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    return render_template("login.html", name = name, form_login = form_login, form_criar_conta = form_criar_conta)

#@app.route('/mrp')

@app.route('/mrp2')
def login(name = None):

if __name__ == '__main__':
        app.run(debug=True)
