def dls(visited, graph, node, depth, limit, goal):
    if depth > limit:
        return False
    if node not in visited:
        print(node, end="->")
        if node == goal:
            print("Goal reached!")
            return True
        visited.add(node)
        for side in graph[node]:
            if dls(visited, graph, side, depth + 1, limit, goal): 
                return True
    return False

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    
    for _ in range(n):
        node = input("Enter the node: ")
        edges = input(f"Enter the edges for {node} separated by space: ").split()
        graph[node] = edges
    
    return graph

graph = input_graph()

start_node = input("Enter the start node for DLS traversal: ")
goal = input("Enter the goal node: ")
depth_limit = int(input("Enter the depth limit: "))

visited = set()
if not dls(visited, graph, start_node, 0, depth_limit, goal):
    print("Goal not found within the depth limit.")
