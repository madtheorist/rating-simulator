from abc import ABC, abstractmethod

from rating_simulator.core.models import GameResult, Player


class BaseUpdateStrategy(ABC):
    @abstractmethod
    def play_game(self, player_a: Player, player_b: Player) -> GameResult:
        """Simulate a game between Player A and Player B based on their true skill and return the outcome."""
        raise NotImplementedError()

    @abstractmethod
    def update_ratings(
        self, player_a: Player, player_b: Player, result: GameResult
    ) -> None:
        """Updates the ratings of player A and player B based on the result of the game."""
        raise NotImplementedError()
