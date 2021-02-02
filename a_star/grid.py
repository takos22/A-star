from typing import Tuple
from json import load

from .cell import Cell


class Grid:
    def __init__(
        self,
        width: int,
        height: int,
        start: Tuple[int, int],
        end: Tuple[int, int],
    ):
        self.width = width
        self.height = height

        self._grid = [[Cell(x, y) for y in range(height)] for x in range(width)]

        self.start = self[start[0], start[1]]
        self.start.start = True
        self.end = self[end[0], end[1]]
        self.end.end = True

    def __getitem__(self, x: int, y: int) -> Cell:
        return self._grid[x][y]

    def __str__(self) -> str:
        return (
            "#" * (self.width + 2)
            + "\n"
            + "\n".join(
                "#" + "".join(str(cell) for cell in line) + "#"
                for line in zip(*self._grid)
            )
            + "\n"
            + "#" * (self.width + 2)
        )

    @classmethod
    def from_json(cls, filename: str = "grid.json") -> "Grid":
        with open(filename) as f:
            json_grid = load(f)

        self: Grid = cls.__new__(cls)
        self.width = len(json_grid[0])
        self.height = len(json_grid)
        self._grid = []

        for y, json_line in enumerate(json_grid):
            line = []

            for x, json_cell in enumerate(json_line):
                cell = Cell(x, y, obstacle=(json_cell == 1))
                line.append(cell)

                if json_cell == 2:
                    self.start = cell
                    cell.start = True
                elif json_cell == 3:
                    self.end = cell
                    cell.end = True

            self._grid.append(line)

        self._grid = zip(*self._grid)  # invert lines and columns
        return self
