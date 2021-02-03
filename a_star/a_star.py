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

        last = self.current.last
        path = [last, self.current]
        while last.last is not None:
            last = last.last
            path.insert(0, last)
        return path

    def next(self) -> Cell:
        for cell in self.current.neighbours:
            if cell in self.closed:
                continue

            self.open.add(cell)

            heuristic = (
                self.current.distance_from_start + 1 + self.heuristic(cell)
            )

            if cell.heuristic is None or heuristic < cell.heuristic:
                cell.distance_from_start = self.current.distance_from_start + 1
                cell.distance_to_end = self.heuristic(cell)
                cell.heuristic = heuristic
                cell.last = self.current

        self.open.remove(self.current)
        self.closed.add(self.current)

        self.current = min(
            self.open,
            key=lambda cell: cell.heuristic,
        )

        return self.current

    def heuristic(self, cell: Cell) -> float:
        return abs(self.grid.end.x - cell.x) + abs(self.grid.end.y - cell.y)
