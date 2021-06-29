
from abc import ABC
from src.Solver import Solver
from src.Creator import Creator


class Simulator(ABC):
    def __init__(self) -> None:


        self._creator = Creator()
        self._solver = Solver()