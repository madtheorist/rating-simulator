from dataclasses import dataclass
from enum import Enum


class Player:
    def __init__(
        self,
        player_id: int,
        true_skill: float = 1500.0,
        rating: float = 1500.0,
        k_factor: float = 32,
    ):
        self.player_id = player_id
        self.true_skill = true_skill
        self.rating = rating
        self.k_factor = k_factor

    def __repr__(self):
        return f"Player(player_id={self.player_id}, true_skill={self.true_skill:.2f}, rating={self.rating:.2f}"


class Result(Enum):
    PLAYER_A_WIN = "Player A"
    PLAYER_B_WIN = "Player B"
    DRAW = "Draw"


@dataclass
class PlayerHistoryRecord:
    round_number: int
    rating: float


@dataclass
class SimulationHistoryRecord:
    round_number: int
    game_results: list[tuple[Player, Player, Result]]
