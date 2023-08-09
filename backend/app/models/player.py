from flask_login import UserMixin
from app import db

class Player(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    wallet = db.relationship('Wallet', backref='player', uselist=False)
    warehouse = db.relationship('Warehouse', backref='player', uselist=False)
    inventory = db.relationship('Inventory', backref='player', uselist=False)
    # Outras informações podem ser adicionadas aqui.

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, default=0)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemons = db.relationship('Pokemon', backref='warehouse')
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'), nullable=False)
    # Outros atributos de Pokémon podem ser adicionados aqui.