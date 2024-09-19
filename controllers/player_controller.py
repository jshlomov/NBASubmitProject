from dataclasses import asdict
import repository.Player_repository as p_rep

from flask import Blueprint, jsonify, request

from repository.Player_repository import get_all_players

player_blueprint = Blueprint("fighter", __name__)

@player_blueprint.route("/", methods=['GET'])
def get_all_players():
    args = request.args
    players = list(map(asdict, p_rep.get_all_players()))
    return jsonify(players), 200

@player_blueprint.route("/", methods=['GET'])
def get_all_players():
    players = list(map(asdict, p_rep.get_all_players()))
    return jsonify(players), 200