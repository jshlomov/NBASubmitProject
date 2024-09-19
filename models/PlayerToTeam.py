from dataclasses import dataclass


@dataclass
class PlayerToTeam:
    team_id: int
    player_id: int
    id: int = None
