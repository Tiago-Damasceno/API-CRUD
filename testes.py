from API import app, db
from models import Usuario, Post


with app.app_context():
    db.create_all()


with app.app_context():
    usuario = Usuario(usuario=tiago, senha=123456, email=tiago@gmail.com)
    usuario2 = Usuario(usuario=thayane, senha=654321, email=thayane@gmail.com)

    db.session.add(usuario)
    db.session.add(usuario2)

    db.session.commit()
with app.app_context():
    meus_usuarios = Usuario.querry.all()
    print(meus_usuarios)