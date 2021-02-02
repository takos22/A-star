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

    def __str__(self) -> str:
        if self.obstacle:
            return "#"
        elif self.start:
            return "O"
        elif self.end:
            return "X"
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
