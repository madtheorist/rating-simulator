from abc import ABC, abstractmethod

from rating_simulator.core.models import Player, Result


class BaseUpdateStrategy(ABC):
    @abstractmethod
    def update(self, player_a: Player, player_b: Player, result: Result) -> None:
        """Updates the ratings of player A and player B based on the result of the game."""
        raise NotImplementedError()
