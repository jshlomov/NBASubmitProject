from dataclasses import dataclass
from typing import List


@dataclass
class PlayerDto:
    name: str
    team: str
    position: str
    season: List[str]
    points: int
    games: int
    two_percent: float
    three_percent: float
    atr: float
    ppg_ratio:float