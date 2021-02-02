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
        self.obstacle = obstacle
        self.start = start
        self.end = end

    def __str__(self):
        if self.obstacle:
            return "#"
        elif self.start:
            return "O"
        elif self.end:
            return "X"
        return " "
