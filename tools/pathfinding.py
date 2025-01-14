import heapq
import matplotlib.pyplot as plt

def a_star_map(map_manager, start, goal):

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))  # (f, g, position)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    visited = []

    while open_list:
        _, current_g, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, visited

        visited.append(current)
        neighbors = map_manager.maps[current].neighbors

        for neighbor in neighbors:
            tentative_g_score = current_g + 1  # Suppose uniforme cost for every move
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor))

    return [], visited

def show_map_with_path(map_manager, path):
    nodes = map_manager.maps.values()

    # Set up the grid limits
    x_min = min(node.x for node in nodes)
    x_max = max(node.x for node in nodes)
    y_min = min(node.y for node in nodes)
    y_max = max(node.y for node in nodes)

    # Create the plot
    fig, ax = plt.subplots()
    for node in nodes:
        ax.plot(node.x, node.y, 'bo')  # Points on the map
        for neighbor in node.neighbors:
            ax.plot([node.x, neighbor[0]], [node.y, neighbor[1]], 'k-', alpha=0.5)  # Connexions

    # Highlight the path
    for i in range(len(path) - 1):
        ax.plot([path[i][0], path[i + 1][0]], [path[i][1], path[i + 1][1]], 'r-', linewidth=2)

    ax.set_title("Map with Path")
    ax.set_aspect('equal')
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()
