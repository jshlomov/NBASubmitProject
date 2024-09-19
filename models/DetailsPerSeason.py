from dataclasses import dataclass

@dataclass
class DetailsPerSeason:
    player_id: int
    position: str
    age: int
    games: int
    fieldGoals: int
    fieldAttempts: int
    fieldPercent: float
    threePercent: float
    twoPercent: float
    assists: int
    turnovers: int
    points: int
    team: str
    season: int