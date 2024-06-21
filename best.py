import heapq #heapq is a prority queue

def best_first_search(graph, start, heuristic):
    visited = set()
    priority_queue = [(heuristic[start], start)] #hear it adds the star element and its huristic value in the queue
    
    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        
        if node not in visited:
            print(node, end="->")
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

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

# Take the graph input from the user
graph = input_graph()

# Take the heuristic values input from the user
heuristic = input_heuristics(graph)

# Start Best-First Search traversal from the specified start node
start_node = input("Enter the start node for Best-First Search traversal: ")
best_first_search(graph, start_node, heuristic)