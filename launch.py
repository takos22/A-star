from a_star import Window, Grid, AStar

grid = Grid.from_json()
# AStar(grid).find_shortest_path(True)
Window(grid).run()
