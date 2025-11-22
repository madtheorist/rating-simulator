from rating_simulator.core.player import Player
from rating_simulator.core.models import Result


class BaseUpdateStrategy:

    def update(self, player_a: Player, player_b: Player, result: Result) -> None:
        """Updates the ratings of player A and player B based on the result of the match."""
        raise NotImplementedError()
