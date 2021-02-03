from a_star import Grid, AStar

grid = Grid.from_json("grid.json")
print(grid)
a_star = AStar(grid)
print(a_star.find_shortest_path())
print(grid)
