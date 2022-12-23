from enum import unique
from app import db

class User(db.Model):
    __tablename__ = "users" #Nome da tabela no banco

    id = db.Column(db.Integer, primary_key=True)#cria uma coluna no banco de dados 
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, password, name, email): #self = campo padrão Python
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r >" % self.username


class post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('user', foreign_keys=user_id) #cria relação entre a tabela user para coletar os dados

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r >" % self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('user', foreign_keys=user_id)
    follower = db.relationship('user', foreign_keys=follower_id)


