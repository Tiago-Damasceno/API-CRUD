from flask import Flask, render_template

app = Flask('__name__')

lista_usuarios = ['Paula', 'Felipe', 'Eloá', 'Raví', 'Tiago']

@app.route('/')
def homepage(name = None):
    return render_template("homepage.html", name = name)

@app.route('/contatos')
def contatos(name = None):
      return render_template("contatos.html", name = name)

@app.route('/usuarios')
def usarios(name = None):
    return render_template("usuarios.html", name = name, lista_usuarios = lista_usuarios)


if __name__ == '__main__':
        app.run(debug=True)
