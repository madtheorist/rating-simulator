class Player:

    def __init__(
        self,
        player_id: int,
        true_skill: float,
        rating: float = 1500.0,
        k_factor: float = 32,
    ):
        self.player_id = player_id
        self.true_skill = true_skill
        self.rating = rating
        self.k_factor = k_factor

    def __repr__(self):
        return f"Player(player_id={self.player_id}, true_skill={self.true_skill:.2f}, rating={self.rating:.2f}"
