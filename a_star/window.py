import pygame
import tkinter

from .grid import Grid
from .a_star import AStar


class Window:
    def __init__(self, grid: Grid = None):
        if grid is None:
            self.get_input("Width:")
            width = int(self.input_value)
            self.get_input("Height:")
            height = int(self.input_value)
            self.get_input("Start position 'x,y':")
            start = (
                int(self.input_value.split(",")[0]),
                int(self.input_value.split(",")[1]),
            )
            self.get_input("End position 'x,y':")
            end = (
                int(self.input_value.split(",")[0]),
                int(self.input_value.split(",")[1]),
            )
            grid = Grid(width, height, start, end)
        self.grid = grid

        self.done = False
        self.algorithm = False

        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.fps = 32
        self.font = pygame.font.SysFont("comicsansms", 24)
        self.launch_text = self.font.render(
            "Launch", True, (255, 255, 255), (63, 63, 63)
        )
        self.size = self.width, self.height = (
            self.grid.width * 16,
            self.grid.height * 16 + 32,
        )

    def event_loop(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_pressed = True

    def update(self):
        if self.algorithm:
            self.update_a_star()

        self.update_drawing()

    def update_a_star(self):
        if self.a_star.current != self.grid.end:
            return self.a_star.next()

        for cell in self.a_star.get_path_to_current():
            cell.path = True

        self.algorithm = False

    def update_drawing(self):
        if self.mouse_pressed:
            pos = self.mouse_pos[0] // 16, self.mouse_pos[1] // 16
            if pos[1] >= self.grid.width:
                self.grid.reset()
                self.a_star = AStar(self.grid)
                self.algorithm = True
                return
            self.grid[pos].obstacle = not self.grid[pos].obstacle

    def draw(self):
        for cell in self.grid:
            cell.draw(self.screen)
        self.screen.blit(self.launch_text, (0, self.grid.height * 16))
        pygame.display.update()

    def run(self):
        pygame.init()

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("A* Algorithm")
        self.screen.fill((63, 63, 63))

        while not self.done:
            self.clock.tick(self.fps)
            self.event_loop()
            self.update()
            self.draw()
        pygame.quit()

    def get_input(self, prompt):
        def set_value():
            self.input_value = input_entry.get()
            root.quit()
            root.destroy()

        root = tkinter.Tk()
        tkinter.Label(root, text=prompt).pack()
        input_entry = tkinter.Entry(root)
        input_entry.pack()
        tkinter.Button(root, text="Ok", command=set_value).pack()
        root.mainloop()
