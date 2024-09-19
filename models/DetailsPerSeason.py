from dataclasses import dataclass

@dataclass
class DetailsPerSeason:
    player_id: int
    player_name: str
    position: str
    age: int
    games: int
    field_goals: int
    field_attempts: int
    field_percent: float
    three_percent: float
    two_percent: float
    assists: int
    turnovers: int
    points: int
    team: str
    season: int
    id: int = None