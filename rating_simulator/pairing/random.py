from rating_simulator.core.player import Player
from rating_simulator.pairing.base import BasePairingStrategy
from typing import Callable

import random


class RandomPairingStrategy(BasePairingStrategy):
    def __init__(self, shuffle_func: Callable = random.shuffle):
        self.shuffle_func = shuffle_func

    def generate_pairs(self, players: list[Player]) -> list[tuple[Player, Player]]:
        if len(players) % 2 == 1:
            raise ValueError("Need an even number of players.")
        self.shuffle_func(players)
        return [(players[i], players[i + 1]) for i in range(0, len(players), 2)]
