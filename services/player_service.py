from functools import partial
from statistics import mean
from typing import List

from toolz import pipe

import repository.details_per_season_repository as d_rep
from models.DetailsPerSeason import DetailsPerSeason
from models.PlayerDto import PlayerDto
from services.calculate_service import calculate_atr, calculate_ppg_ratio, calculate_ppg_ratio_for_all_seasons


def get_all_players(position:str, season:str = None):

    all_players_details = d_rep.get_all_details_per_season()
    players_details = filter(lambda p: position in p.position, all_players_details)
    if season:
        players_details = filter(lambda p: season == p.season, players_details)
    return [create_player_dto(p) for p in players_details]


def create_player_dto(player:DetailsPerSeason, all_players:List[DetailsPerSeason]):
    season = pipe(
        all_players,
        partial(filter, lambda p: p.player_id == player.player_id),
        partial(map, lambda p: p.season),
        list
    )

    points = pipe(
        all_players,
        partial(filter, lambda p: p.player_id == player.player_id),
        partial(map, lambda p: p.points),
        list,
        mean
    )

    games= pipe(
        all_players,
        partial(filter, lambda p: p.player_id == player.player_id),
        partial(map, lambda p: p.games),
        list,
        mean
    )

    two_percent=games= pipe(
        all_players,
        partial(filter, lambda p: p.player_id == player.player_id),
        partial(map, lambda p: p.games),
        list,
        mean
    )

    three_percent= pipe(
        all_players,
        partial(filter, lambda p: p.player_id == player.player_id),
        partial(map, lambda p: p.three_percent),
        list,
        mean
    )

    art= calculate_atr(player)

    ppg_ratio= calculate_ppg_ratio_for_all_seasons(player, all_players, player.position)
    breakpoint()
    return PlayerDto(
        name=player.player_name,
        team=player.team,
        position=player.position,
        season=season,
        points=points,
        games=games,
        two_percent=two_percent,
        three_percent=three_percent,
        atr=art,
        ppg_ratio=ppg_ratio
    )
