import pytest

from rating_simulator.core.player import Player
from rating_simulator.pairing.random import RandomPairingStrategy


def test_random_pairing_with_no_players():
    players = []
    strategy = RandomPairingStrategy()
    assert strategy.generate_pairs(players) == []


def test_random_pairing_with_odd_number_of_players():
    players = [Player(1), Player(2), Player(3)]
    strategy = RandomPairingStrategy()
    with pytest.raises(ValueError):
        strategy.generate_pairs(players)


def test_random_pairing_with_shuffle_function():
    players = [Player(1), Player(2), Player(3), Player(4)]
    strategy = RandomPairingStrategy(shuffle_func=list.reverse)
    pairs = strategy.generate_pairs(players)
    assert len(pairs) == 2
    assert pairs[0][0].player_id == 4
    assert pairs[0][1].player_id == 3
    assert pairs[1][0].player_id == 2
