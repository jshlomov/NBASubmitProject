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
    twoPercent: float
    threePercent: float
    atr: float
    ppg_ratio:float