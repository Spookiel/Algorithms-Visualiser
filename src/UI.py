from abc import ABC, abstractmethod
from src.Simulator import Simulator
from src.Renderer import Renderer



class UI(ABC):

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError


class GUI(UI):

    def __init__(self) -> None:

        self._simulator = Simulator()
        self._renderer = Renderer()


class Terminal(UI):
    def __init__(self) -> None:

        self._simulator = Simulator()

