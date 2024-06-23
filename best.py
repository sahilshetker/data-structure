import heapq
def best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic[start], start)]
    path = []
    
    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        
        if node not in visited:
            path.append(node)
            visited.add(node)
            
            if node == goal:
                print("->".join(path))
                print("Goal reached!")
                return
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
    
    print("Goal not found.")

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    
    for _ in range(n):
        node = input("Enter the node: ")
        edges = input(f"Enter the edges for {node} separated by space: ").split()
        graph[node] = edges
    
    return graph

def input_heuristics(graph):
    heuristic = {}
    for node in graph:
        h_value = int(input(f"Enter the heuristic value for node {node}: "))
        heuristic[node] = h_value
    return heuristic

graph = input_graph()

heuristic = input_heuristics(graph)

start_node = input("Enter the start node for Best-First Search traversal: ")
goal_node = input("Enter the goal node: ")
best_first_search(graph, start_node, goal_node, heuristic)
