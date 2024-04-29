from models import Highscore
from flask import Blueprint, request, jsonify

highscore_bp = Blueprint('highscore', __name__)

@highscore_bp.route('/highscore', methods=['POST'])
def create_highscore():  
    data = request.json
    name = data.get('name')
    points = data.get('points')
    highscore = Highscore.create(name=name, points=points)
    return jsonify({'message': 'Highscore created successfully', 'id': highscore.id}), 201

@highscore_bp.route('/highscore', methods=['GET'])
def get_highscore():
    all_highscores = Highscore.select()
    if all_highscores:
        highest_highscore = all_highscores.order_by(Highscore.points.desc()).first()
        return jsonify({'highscore': highest_highscore.points})
    else:
        return jsonify({'message': 'There are no highscores.'}), 404
    
@highscore_bp.route('/highscoreAll', methods=['GET'])
def get_everyHighscore():
    all_highscores = Highscore.select()
    return jsonify({'highscores': [highscore.serialize() for highscore in all_highscores]})