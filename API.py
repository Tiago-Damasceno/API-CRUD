from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def homepage(name = None):
    return render_template("homepage.html", name = name)

@app.route('/contatos/<contatos>')
def contatos(name = None):
      return render_template("contatos.html", name = name)




if __name__ == '__main__':
        app.run(debug=True)