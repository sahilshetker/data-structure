def dls(visited, graph, node, depth, limit):
    if depth > limit:
        return
    if node not in visited:
        print(node, end="->")
        visited.add(node)
        for side in graph[node]:
            dls(visited, graph, side, depth + 1, limit)

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    
    for _ in range(n):
        node = input("Enter the node: ")
        edges = input(f"Enter the edges for {node} separated by space: ").split()
        graph[node] = edges
    
    return graph

# Take the graph input from the user
graph = input_graph()

# Start DFS traversal from the specified start node
start_node = input("Enter the start node for DLS traversal: ")
depth_limit = int(input("Enter the depth limit: "))
visited = set()
dls(visited, graph, start_node, 0, depth_limit)