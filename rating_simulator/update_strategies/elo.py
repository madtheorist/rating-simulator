import random

from rating_simulator.core.models import GameResult, Player
from rating_simulator.update_strategies.base import UpdateStrategy


class EloUpdateStrategy(UpdateStrategy):
    """Implementation of a basic ELO update strategy.

    Performance is approximated as a logistic curve with base 10.
    """

    def __init__(self, draw_prob: float = 0.0):
        self.draw_prob = draw_prob

    def play_game(self, player_a: Player, player_b: Player) -> GameResult:
        player_a_win_prob = (1 - self.draw_prob) / (
            1 + 10 ** ((player_b.true_skill - player_a.true_skill) / 400)
        )
        rand = random.random()
        if rand < player_a_win_prob:
            return GameResult.PLAYER_A_WIN
        elif rand < player_a_win_prob + self.draw_prob:
            return GameResult.DRAW
        return GameResult.PLAYER_B_WIN

    def update_ratings(
        self, player_a: Player, player_b: Player, result: GameResult
    ) -> None:
        expected_score_a = (1 - self.draw_prob) / (
            1 + 10 ** ((player_b.rating - player_a.rating) / 400)
        ) + 0.5 * self.draw_prob
        expected_score_b = 1 - expected_score_a

        if result == GameResult.PLAYER_A_WIN:
            actual_score_a, actual_score_b = 1.0, 0.0
        elif result == GameResult.PLAYER_B_WIN:
            actual_score_a, actual_score_b = 0.0, 1.0
        else:
            actual_score_a, actual_score_b = 0.5, 0.5

        player_a.rating = player_a.rating + player_a.k_factor * (
            actual_score_a - expected_score_a
        )
        player_b.rating = player_b.rating + player_b.k_factor * (
            actual_score_b - expected_score_b
        )
