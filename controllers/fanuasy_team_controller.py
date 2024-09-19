from dataclasses import asdict

from flask import Blueprint, jsonify

from repository.Player_repository import get_all_players

player_blueprint = Blueprint("fighter", __name__)

@player_blueprint.route("/", methods=['GET'])
def get_all_players():
    players = list(map(asdict, get_all_players()))
    return jsonify(players), 200

@fighter_blueprint.route("/", methods=['GET'])
def get_all_players():
    players = list(map(asdict, get_all_players()))
    return jsonify(players), 200