# rating-simulator
(WIP) A Python package for simulating zero-sum games using Monte Carlo methods with customizable rating systems.

Example usage:

```python
if __name__ == "__main__":

    # create some players with a Gaussian skill distribution, and initialise their ratings
    players = create_players(num_players=200, initial_rating=1500, skill_mean=1500, skill_std=200)

    # pick a pairing strategy and update strategy
    pairing_strategy = RandomPairingStrategy()
    update_strategy = EloUpdateStrategy(draw_prob=0.1)

    # instantiate a Simulation object and run the simulation
    simulation = Simulation(players, pairing_strategy, update_strategy, num_rounds=1000)
    simulation.run()

    # analyse the results
    player_1 = simulation.players[0]
    print([record.rating for record in player_1.history]) # get the rating graph of a player over time
    print(player_1.true_skill) # get the true skill of the player. The rating should converge to the true skill over time.

```
In short: it lets you simulate games between players with hidden “true skill” values and see how the ratings converge over time. Currently supports:

- Elo rating system (with optional draw probability)
- Random pairing strategy
  
Planned features: 
- data viz methods
- more pairing strategies (round-robin, Swiss)
- more rating systems (Glicko, TrueSkill)
- more simulation options (noisiness, league formats)
- option to adjust the true skill of players as rounds progress
