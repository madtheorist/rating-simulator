# rating-simulator
(WIP) A Python package for simulating zero-sum games using Monte Carlo methods with customizable rating systems.

Example usage:

```python
if __name__ == "__main__":
    players = create_players(num_players=200)
    pairing_strategy = RandomPairingStrategy()
    update_strategy = EloUpdateStrategy(draw_prob=0.1)
    simulation = Simulation(players, pairing_strategy, update_strategy, num_rounds=1000)
    simulation.run()
    player_1 = simulation.players[0]
    print([record.rating for record in player_1.history]) # get the rating graph of a player over time
    print(player_1.true_skill) # get the true skill of the player. The rating should converge to the true skill over time.

```
In short: lets you simulate games between players with hidden “true skill” values and see how ratings evolve over time. Currently supports:

- Elo rating system (with optional draw probability)
- Random pairing strategy
- 
Planned features: more pairing strategies (round-robin, Swiss) and rating systems (Glicko, TrueSkill); more simulation options (noisiness, league formats)
