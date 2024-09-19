from typing import List
import statistics as s
from toolz import pipe
from toolz.curried import partial

from models.DetailsPerSeason import DetailsPerSeason


def calculate_atr(details: DetailsPerSeason):
    return details.assists / details.turnovers

def calculate_ppg_ratio_for_all_seasons(curr_details:DetailsPerSeason, all_players:List[DetailsPerSeason], position:str):
    return (calculate_ppg_ratio(curr_details, all_players, 2022, position) +
            calculate_ppg_ratio(curr_details, all_players, 2023, position) +
            calculate_ppg_ratio(curr_details, all_players, 2024, position)
            / 3)



def calculate_ppg_ratio(curr_details:DetailsPerSeason, all_players:List[DetailsPerSeason], season:str, position:str):
    return points_per_game(curr_details) / global_points_per_game_in_season(all_players, season, position)

def points_per_game(details:DetailsPerSeason):
    return details.points / details.games

def global_points_per_game_in_season(players_details:List[DetailsPerSeason], season:str, position:str):
    return pipe(
        players_details,
        partial(filter, lambda p: p.season == season and position in p.position),
        partial(map, points_per_game),
        list,
        s.mean
    )
