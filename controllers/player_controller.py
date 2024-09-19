from dataclasses import asdict

import services.player_service as s
from flask import Blueprint, jsonify, request

player_blueprint = Blueprint("player", __name__)

@player_blueprint.route("/", methods=['GET'])
def get_all_players():
    args = request.args
    players = s.get_all_players(args.get("position"), args.get("season"))
    breakpoint()
    players_to_return = list(map(asdict, players))
    return jsonify(players_to_return), 200