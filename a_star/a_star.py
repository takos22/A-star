from typing import List

from .grid import Grid
from .cell import Cell


class AStar:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.current = self.grid.start
        self.current.distance_to_end = self.current.heuristic = self.heuristic(
            self.current
        )
        self.open = {self.current}
        self.closed = set()

    def find_shortest_path(self) -> List[Cell]:
        while self.current != self.grid.end:
            self.next()

        path = self.get_path_to_current()

        for cell in path:
            cell.path = True

        return path

    def next(self) -> Cell:
        for cell in self.current.neighbours:
            if cell in self.closed:
                continue

            self.open.add(cell.open())

            heuristic = self.heuristic(cell) + 1.5 * (
                self.current.distance_from_start + 1
            )

            if cell.heuristic is None or heuristic < cell.heuristic:
                cell.distance_from_start = self.current.distance_from_start + 1
                cell.distance_to_end = self.heuristic(cell)
                cell.heuristic = heuristic
                cell.last = self.current

        self.closed.add(self.current.close())
        self.open.remove(self.current)

        self.current = min(
            self.open,
            key=lambda cell: cell.heuristic,
        )

        return self.current

    def get_path_to_current(self) -> List[Cell]:
        last = self.current.last
        path = [last, self.current]

        while last.last is not None:
            last = last.last
            path.insert(0, last)

        return path

    def heuristic(self, cell: Cell) -> int:
        return (
            ((self.grid.end.x - cell.x) ** 2 + (self.grid.end.y - cell.y) ** 2)
            ** 0.5
            + abs(self.grid.end.x - cell.x)
            + abs(self.grid.end.y - cell.y)
        )
