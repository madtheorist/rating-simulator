from abc import ABC, abstractmethod
from typing import Iterator

from rating_simulator.core.models import Player


class BasePairingStrategy(ABC):
    @abstractmethod
    def generate_pairs(
        self, players: list[Player], num_rounds: int
    ) -> Iterator[list[tuple[Player, Player]]]:
        """Generate pairs of players for a given number of rounds.
        Each round yields a new list of pairs.

        Args:
            players (List[Player]): A list of Player instances. Must be even in length.
            rounds (int): Number of rounds to generate pairs for.

        Yields:
            Iterator[List[Tuple[Player, Player]]]: Lists of player pairs for each round.
        """
        raise NotImplementedError()
