from api.nba_api import get_from_nba_api
from models.Player import Player
from repository.Player_repository import create_user


def load_players_from_api():
    load_players_per_season(2022)
    load_players_per_season(2023)
    load_players_per_season(2024)

def load_players_per_season(season):
    players_json = get_from_nba_api(season)
    for p in [Player(**p) for p in players_json]:
        create_user(p)
