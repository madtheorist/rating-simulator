import random
from typing import Callable, Iterator

from rating_simulator.core.models import Player
from rating_simulator.pairing.base import BasePairingStrategy


class RandomPairingStrategy(BasePairingStrategy):
    def __init__(self, shuffle_func: Callable = random.shuffle):
        self.shuffle_func = shuffle_func

    def generate_pairs(
        self, players: list[Player], num_rounds: int
    ) -> Iterator[list[tuple[Player, Player]]]:
        """For each round, yield a list of random pairings."""
        if len(players) % 2 == 1:
            raise ValueError("Need an even number of players.")

        for _ in range(num_rounds):
            self.shuffle_func(players)
            yield [(players[i], players[i + 1]) for i in range(0, len(players), 2)]
