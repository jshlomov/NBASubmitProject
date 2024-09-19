from dataclasses import asdict
from http.cookiejar import debug
from idlelib.debugger_r import debugging

import services.player_service as s
from flask import Blueprint, jsonify, request

from repository.Player_repository import get_all_players

player_blueprint = Blueprint("player", __name__)

@player_blueprint.route("/", methods=['GET'])
def get_all_players():
    args = request.args
    players = list(map(asdict, s.get_all_players(args.get("position"), args.get("season"))))
    return jsonify(players), 200