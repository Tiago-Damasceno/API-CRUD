from API import database
from datetime import datetime
class Usuario(database.model):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False )
    senha = database.Column(database.String, nullable=False, )
    email = database.Column(database.String, nullable=False, unique=True)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationsip('Post', backref='autor', lazy=True)
    estilo = database.Column(database.String, nullable=False, default='Não Informado')


class Post(database.model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criação = database.Column(database.Datetime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer,  database.ForeignKey('usuario.id'), nullable=False)

