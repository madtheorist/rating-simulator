import copy

import numpy as np

from rating_simulator.core.models import (
    Player,
    PlayerHistoryRecord,
    SimulationHistoryRecord,
)
from rating_simulator.pairing_strategies.base import PairingStrategy
from rating_simulator.update_strategies.base import UpdateStrategy


class Simulation:
    def __init__(
        self,
        players: list[Player],
        pairing_strategy: PairingStrategy,
        update_strategy: UpdateStrategy,
        num_rounds: int = 100,
    ) -> None:
        self.players = players
        self.pairing_strategy = pairing_strategy
        self.update_strategy = update_strategy
        self.num_rounds = num_rounds
        self.history: list[SimulationHistoryRecord] = []
        self._has_run = False

    def __repr__(self):
        return f"Simulation(num_players={len(self.players)}, num_rounds={self.num_rounds})"

    def run(self) -> None:
        if self._has_run:
            raise RuntimeError("The simulation is already completed.")
        
        for round_number, round_pairings in enumerate(
            self.pairing_strategy.generate_pairs(self.players, self.num_rounds)
        ):
            game_history = []
            for pairing in round_pairings:
                player_a, player_b = pairing
                game_result = self.update_strategy.play_game(player_a, player_b)
                self.update_strategy.update_ratings(player_a, player_b, game_result)
                player_a.history.append(
                    PlayerHistoryRecord(round_number, copy.deepcopy(player_a.rating))
                )
                player_b.history.append(
                    PlayerHistoryRecord(round_number, copy.deepcopy(player_b.rating))
                )
                game_history.append(
                    (player_a.player_id, player_b.player_id, game_result)
                )
            self.history.append(SimulationHistoryRecord(round_number, game_history))
        self._has_run = True


def create_players(
    num_players: int,
    initial_rating: float = 1500,
    skill_mean: float = 1500,
    skill_std: float = 200,
    k_factor: float = 20,
) -> list[Player]:
    players = []
    for i in range(num_players):
        true_skill = np.random.normal(skill_mean, skill_std)
        players.append(
            Player(player_id=i, true_skill=true_skill, rating=initial_rating, k_factor=k_factor)
        )
    return players
