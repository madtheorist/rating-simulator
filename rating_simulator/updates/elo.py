from rating_simulator.core.models import Player, Result
from rating_simulator.updates.base import BaseUpdateStrategy


class EloUpdateStrategy(BaseUpdateStrategy):
    """Implementation of a basic ELO update strategy.

    Performance is approximated as a logistic curve with base 10.
    """

    def update(self, player_a: Player, player_b: Player, result: Result) -> None:
        expected_score_a = 1 / (1 + 10 ** ((player_b.rating - player_a.rating) / 400))
        expected_score_b = 1 / (1 + 10 ** ((player_a.rating - player_b.rating) / 400))

        if result == Result.PLAYER_A_WIN:
            actual_score_a, actual_score_b = 1.0, 0.0
        elif result == Result.PLAYER_B_WIN:
            actual_score_a, actual_score_b = 0.0, 1.0
        else:
            actual_score_a, actual_score_b = 0.5, 0.5

        player_a.rating = player_a.rating + player_a.k_factor * (
            actual_score_a - expected_score_a
        )
        player_b.rating = player_b.rating + player_b.k_factor * (
            actual_score_b - expected_score_b
        )
