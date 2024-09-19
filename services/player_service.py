import repository.details_per_season_repository as d_rep

def get_all_players(position:str, season:str = None):
    all_players_details = d_rep.get_all_details_per_season()
    players_details = filter(lambda p: position in p.position, all_players_details)


