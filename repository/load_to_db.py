from toolz import get_in

from api.nba_api import get_from_nba_api
from models.DetailsPerSeason import DetailsPerSeason
from models.Player import Player
from repository.Player_repository import create_player
from repository.details_per_season_repository import create_details_per_season


def load_players_from_api():
    load_players_per_season(2022)
    load_players_per_season(2023)
    load_players_per_season(2024)

def load_players_per_season(season):
    players_json = get_from_nba_api(season)
    for pj in players_json:
        new_id = create_player(player_from_json(pj))
        create_details_per_season(details_from_json(pj, new_id))

def player_from_json(json):
    return Player(**{
        "player_name" : get_in(["playerName"], json),
        "player_id": get_in(["playerId"], json)
    })

def details_from_json(json, new_id):
    return DetailsPerSeason(**{
        "player_id" : new_id,
        "player_name" : get_in(["playerName"], json),
        "position" : get_in(["position"], json),
        "age" : get_in(["age"], json),
        "games" : get_in(["games"], json),
        "field_goals" : get_in(["fieldGoals"], json),
        "field_attempts" : get_in(["fieldAttempts"], json),
        "field_percent" : get_in(["fieldPercent"], json),
        "three_percent" : get_in(["threePercent"], json),
        "two_percent" : get_in(["twoPercent"], json),
        "assists" : get_in(["assists"], json),
        "turnovers" : get_in(["turnovers"], json),
        "points" : get_in(["points"], json),
        "team" : get_in(["team"], json),
        "season" : get_in(["season"], json),
    })