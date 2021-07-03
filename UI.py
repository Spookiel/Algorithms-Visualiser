from abc import ABC, abstractmethod
from Simulator import Simulator
from Renderer import Renderer



class UI(ABC):


    def __init__(self):
        self._simulator = Simulator()


    @property
    def simulator(self):
        return self._simulator


    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError


class GUI(UI):

    def __init__(self) -> None:
        super().__init__()
        self._renderer = Renderer()

    def run(self) -> None:
        raise NotImplementedError

    @property
    def renderer(self):
        return self._renderer


class Terminal(UI):
    def __init__(self) -> None:
        super().__init__()


    def run(self) -> None:
        self.display_menu()



    def display_menu(self):
        print("Menu:")
        print("1. View sorting algorithm options")
        print("2. View grid searching algorithm options")
        print("3. View maze generation and searching options")
        print("4. Quit")
        print("-"*50)

