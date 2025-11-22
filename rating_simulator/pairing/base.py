from abc import ABC, abstractmethod
from typing import Iterator

from rating_simulator.core.models import Player


class BasePairingStrategy(ABC):
    @abstractmethod
    def generate_pairs(
        self, players: list[Player], num_rounds: int
    ) -> Iterator[list[tuple[Player, Player]]]:
        """Generate pairs of players for a given number of rounds.
        Each round yields a new list of pairings.

        Args:
            players (list[Player]): A list of Player instances. Must be even in length.
            rounds (int): Number of rounds to generate pairings for.

        Yields:
            Iterator[list[tuple[Player, Player]]]: Lists of player pairings for each round.
        """
        raise NotImplementedError()
