import heapq
def a_star_search(graph, start, goal, heuristic):
    open_set = [(heuristic[start], start)]
    g_costs = {start: 0}
    came_from = {}
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = reconstruct_path(came_from, current)
            print("->".join(path))
            print("Goal reached!")
            return
        
        for neighbor, cost in graph[current]:
            tentative_g_cost = g_costs[current] + cost
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_set, (f_cost, neighbor))
                came_from[neighbor] = current

    print("Goal not found.")

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    for _ in range(n):
        node = input("Enter the node: ")
        edges = input(f"Enter the edges for {node} and their costs (format: node cost node cost ...): ").split()
        graph[node] = [(edges[i], int(edges[i + 1])) for i in range(0, len(edges), 2)]
    return graph

def input_heuristics(graph):
    return {node: int(input(f"Enter the heuristic value for node {node}: ")) for node in graph}

graph = input_graph()

heuristic = input_heuristics(graph)

start_node = input("Enter the start node for A* Search traversal: ")
goal_node = input("Enter the goal node: ")

a_star_search(graph, start_node, goal_node, heuristic)
