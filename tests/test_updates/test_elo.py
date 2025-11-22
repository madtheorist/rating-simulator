from unittest.mock import patch

import pytest

from rating_simulator.core.models import GameResult, Player
from rating_simulator.update_strategies.elo import EloUpdateStrategy


def test_elo_play_game():
    player_a = Player(player_id=1, true_skill=1200, rating=1300, k_factor=30)
    player_b = Player(player_id=2, true_skill=1400, rating=1500, k_factor=30)
    strategy = EloUpdateStrategy(draw_prob=0)
    with patch("random.random", return_value=0.5):
        game_result = strategy.play_game(player_a, player_b)
        assert game_result == GameResult.PLAYER_B_WIN

    with patch("random.random", return_value=0.1):
        game_result = strategy.play_game(player_a, player_b)
        assert game_result == GameResult.PLAYER_A_WIN


def test_elo_play_game_with_draw_prob():
    player_a = Player(player_id=1, true_skill=1200, rating=1300, k_factor=30)
    player_b = Player(player_id=2, true_skill=1200, rating=1500, k_factor=30)
    strategy = EloUpdateStrategy(draw_prob=0.9)
    with patch("random.random", return_value=0.6):
        game_result = strategy.play_game(player_a, player_b)
        assert game_result == GameResult.DRAW

    with patch("random.random", return_value=0.96):
        game_result = strategy.play_game(player_a, player_b)
        assert game_result == GameResult.PLAYER_B_WIN


@pytest.mark.parametrize(
    "result, rating_change_sign",
    [
        (GameResult.PLAYER_A_WIN, 1),  # A should gain, B should lose
        (GameResult.PLAYER_B_WIN, -1),  # A should lose, B should gain
        (GameResult.DRAW, 0),
    ],
)
def test_elo_update_ratings(result, rating_change_sign):
    player_a_initial_rating = 1500
    player_b_initial_rating = 1600

    player_a = Player(
        player_id=1, true_skill=1200, rating=player_a_initial_rating, k_factor=30
    )
    player_b = Player(
        player_id=2, true_skill=1300, rating=player_b_initial_rating, k_factor=30
    )

    strategy = EloUpdateStrategy(draw_prob=0.1)
    strategy.update_ratings(player_a, player_b, result)

    a_delta = player_a.rating - player_a_initial_rating
    b_delta = player_b.rating - player_b_initial_rating
    assert a_delta == -b_delta
    if rating_change_sign == 1:
        assert a_delta > 0
    elif rating_change_sign == -1:
        assert a_delta < 0
