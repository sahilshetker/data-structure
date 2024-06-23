visited = set()

def dfs(visited, graph, node, goal):
    if node not in visited:
        print(node, end="->")
        
        if node == goal:
            print("Goal reached!")
            return True
        
        visited.add(node)
        
        for side in graph[node]:
            if side not in visited:  
                if dfs(visited, graph, side, goal):  
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

start_node = input("Enter the start node for DFS traversal: ")

goal = input("Enter the goal node: ")

if not dfs(visited, graph, start_node, goal):
    print("Goal not found in the graph.")
