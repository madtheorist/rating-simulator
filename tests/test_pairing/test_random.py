import pytest

from rating_simulator.core.models import Player
from rating_simulator.pairing.random import RandomPairingStrategy


def test_random_pairing_with_no_players():
    players = []
    strategy = RandomPairingStrategy()
    for pairings in strategy.generate_pairs(players, num_rounds=3):
        assert pairings == []


def test_random_pairing_with_odd_number_of_players():
    players = [Player(1), Player(2), Player(3)]
    strategy = RandomPairingStrategy()
    with pytest.raises(ValueError):
        next(strategy.generate_pairs(players, num_rounds=3))


def test_random_pairing_with_deterministic_shuffle_function():
    players = [Player(1), Player(2), Player(3), Player(4)]
    strategy = RandomPairingStrategy(shuffle_func=list.reverse)
    pairings = next(strategy.generate_pairs(players, num_rounds=1))
    assert len(pairings) == 2
    assert pairings[0][0].player_id == 4
    assert pairings[0][1].player_id == 3
    assert pairings[1][0].player_id == 2
