from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import Player
from . import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    existing_player = Player.query.filter_by(username=username).first()
    if existing_player:
        return jsonify({'error': 'Username already exists'}), 409

    new_player = Player(username=username, password=generate_password_hash(password))
    db.session.add(new_player)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    player = Player.query.filter_by(username=username).first()
    if not player or not check_password_hash(player.password, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # Implement JWT or session-based authentication here
    # Return a token or set session cookie upon successful login

    return jsonify({'message': 'Login successful'})
