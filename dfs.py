visited=set()

def dfs(visited,graph,node):
	if node not in visited:
		print(node,end="->")
		visited.add(node)
		for side in graph[node]:
			dfs(visited,graph,side)
			
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

# Start BFS traversal from the specified start node
start_node = input("Enter the start node for DFS traversal: ")
dfs(visited, graph, start_node)