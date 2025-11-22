from rating_simulator.core.models import Player, SimulationHistoryRecord
from rating_simulator.pairing.base import BasePairingStrategy
from rating_simulator.updates.base import BaseUpdateStrategy


class Simulation:
    def __init__(
        self,
        players: list[Player],
        pairing_strategy: BasePairingStrategy,
        update_strategy: BaseUpdateStrategy,
        num_rounds: int = 100,
    ) -> None:
        self.players = players
        self.pairing_strategy = pairing_strategy
        self.update_strategy = update_strategy
        self.num_rounds = num_rounds
        self.history: list[SimulationHistoryRecord] = []
