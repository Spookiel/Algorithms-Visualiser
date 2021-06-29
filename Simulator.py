
from abc import ABC
from Solver import Solver
from Creator import Creator


class Simulator(ABC):
    def __init__(self) -> None:


        self._creator = Creator()
        self._solver = Solver()