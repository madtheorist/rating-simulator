from rating_simulator.core.simulation import Simulation, create_players
from rating_simulator.pairing_strategies.random import RandomPairingStrategy
from rating_simulator.update_strategies.elo import EloUpdateStrategy

if __name__ == "__main__":
    players = create_players(num_players=200)
    pairing_strategy = RandomPairingStrategy()
    update_strategy = EloUpdateStrategy(draw_prob=0.1)
    simulation = Simulation(players, pairing_strategy, update_strategy, num_rounds=1000)
    simulation.run()
    player_1 = simulation.players[0]
    print([record.rating for record in player_1.history])
    print(player_1.true_skill)
