from abc import ABC, abstractmethod

from rating_simulator.core.player import Player


class BasePairingStrategy(ABC):
    @abstractmethod
    def generate_pairs(self, players: list[Player]) -> list[tuple[Player, Player]]:
        """For a given sim round, generates a list of player pairs to play against each other."""
        raise NotImplementedError()
