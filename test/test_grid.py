from assets.grid import dofus_map
from utils.pathfinding import a_star_map, show_map_with_path


dofus_map.visualize()

start = (10, -29)
goal = (12, -21)

path, visited = a_star_map(dofus_map, start, goal)
print("Path:", path)
print("Visited:", visited)

show_map_with_path(dofus_map, path)


