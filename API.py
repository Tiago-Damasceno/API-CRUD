from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')
lista_usuarios = ['Paula', 'Felipe', 'Eloá', 'Raví', 'Tiago']

db = SQLAlchemy(app)

app.secret_key = os.environ.get('FLASK_SECRET_KEY', '86a80337ce81d80a3503f02eb197c8c5')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'






@app.route('/')
def homepage(name=None):
    return render_template("homepage.html", name=name)


@app.route('/contatos')
def contatos(name=None):
    return render_template("contatos.html", name=name)


@app.route('/usuarios')
def usuarios(name=None):
    return render_template("usuarios.html", name=name, lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login(name=None):
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()

    if form_login.validate_on_submit() and 'botão_login' in request.form:
        flash(f'login feito com sucesso para o email {form_login.email.data}', 'alert-success')
        return redirect(url_for('homepage'))
        # fez login  com sucesso
    if form_criar_conta.validate_on_submit() and 'botão_submit_criarconta' in request.form:
        flash(f'conta criada com sucesso para o email {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('homepage'))
        # criou conta com sucesso

    return render_template("login.html", name=name, form_login=form_login, form_criar_conta=form_criar_conta)


if __name__ == '__main__':
    app.run(debug=True)
