from abc import ABC

class Solver(ABC):
    def __init__(self) -> None:
        pass


class MazeSolver():
    def __init__(self) -> None:
        pass

class GraphSolver():
    def __init__(self) -> None:
        pass
class GridSolver():
    def __init__(self) -> None:
        self._curGrid = []
        self._steps = []


    def bfs(self):
        # Generates a sequence of steps
        pass
