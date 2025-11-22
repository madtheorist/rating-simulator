from abc import ABC, abstractmethod

from rating_simulator.core.models import Result
from rating_simulator.core.player import Player


class BaseUpdateStrategy(ABC):
    @abstractmethod
    def update(self, player_a: Player, player_b: Player, result: Result) -> None:
        """Updates the ratings of player A and player B based on the result of the match."""
        raise NotImplementedError()
