from rating_simulator.updates.elo import EloUpdateStrategy
from rating_simulator.core.player import Player
from rating_simulator.core.models import Result

import pytest


@pytest.mark.parametrize(
    "result, rating_change_sign",
    [
        (Result.PLAYER_A_WIN, 1),  # A should gain, B should lose
        (Result.PLAYER_B_WIN, -1),  # A should lose, B should gain
        (Result.DRAW, 0),
    ],
)
def test_elo_update_strategy(result, rating_change_sign):
    player_a_initial_rating = 1500
    player_b_initial_rating = 1600

    player_a = Player(
        player_id=1, true_skill=1200, rating=player_a_initial_rating, k_factor=30
    )
    player_b = Player(
        player_id=2, true_skill=1300, rating=player_b_initial_rating, k_factor=30
    )

    strategy = EloUpdateStrategy()
    strategy.update(player_a, player_b, result)

    a_delta = player_a.rating - player_a_initial_rating
    b_delta = player_b.rating - player_b_initial_rating
    assert a_delta == -b_delta
    if rating_change_sign == 1:
        assert a_delta > 0
    elif rating_change_sign == -1:
        assert a_delta < 0
