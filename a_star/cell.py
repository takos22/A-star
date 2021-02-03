class Cell:
    def __init__(
        self,
        x: int,
        y: int,
        obstacle: bool = False,
        start: bool = False,
        end: bool = False,
    ):
        self.x = x
        self.y = y
        self.pos = (x, y)

        self.obstacle = obstacle
        self.start = start
        self.end = end

        self.neighbours = set()
        self.last = None
        self.distance_from_start = 0 if self.start else None
        self.distance_to_end = None
        self.heuristic = None
        self.opened = False
        self.closed = False
        self.path = False

    def __str__(self) -> str:
        if self.obstacle:
            return "#"
        elif self.start:
            return "O"
        elif self.end:
            return "X"
        elif self.path:
            return "+"
        elif self.closed:
            return "*"
        elif self.opened:
            return "."
        return " "

    def __repr__(self) -> str:
        return str(self.pos)

    def add_neighbours(self, grid) -> set:
        if self.x > 0 and not grid[self.x - 1, self.y].obstacle:
            self.neighbours.add(grid[self.x - 1, self.y])  # left

        if self.x + 1 < grid.width and not grid[self.x + 1, self.y].obstacle:
            self.neighbours.add(grid[self.x + 1, self.y])  # right

        if self.y > 0 and not grid[self.x, self.y - 1].obstacle:
            self.neighbours.add(grid[self.x, self.y - 1])  # top

        if self.y + 1 < grid.height and not grid[self.x, self.y + 1].obstacle:
            self.neighbours.add(grid[self.x, self.y + 1])  # bottom

        return self.neighbours

    def open(self) -> "Cell":
        self.opened = True
        return self

    def close(self) -> "Cell":
        self.opened = False
        self.closed = True
        return self
