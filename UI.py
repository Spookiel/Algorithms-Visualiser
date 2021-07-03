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
    MENULEN = 4
    def __init__(self) -> None:
        super().__init__()


    def run(self) -> None:
        self.display_menu()
        str_choice: str = "0"
        while True:

            str_choice = input(f"Enter choice (1-{Terminal.MENULEN}): ")
            try:
                int_choice: int = int(str_choice)
            except ValueError:
                print("Invalid input for choice, please try again")
                continue #Back to start of loop

            if int_choice < 1 or int_choice > self.MENULEN:
                print("Choice is out of range, please try again")
                continue

            #Valid choice so process here

            if int_choice==1:
                pass
            elif int_choice==2:
                pass
            elif int_choice==3:
                pass
            elif int_choice==4:
                pass




    def process_sorting_choice(self):
        pass

    def display_menu(self):
        print("Menu:")
        print("1. View sorting algorithm options")
        print("2. View grid searching algorithm options")
        print("3. View maze generation and searching options")
        print("4. Quit")
        print("-"*50)

