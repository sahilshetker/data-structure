visited=[]
queue=[]

def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end="->")
        
        if m == goal:
            print("Goal reached!")
            return
        
        for side in graph[m]:
            if side not in visited:
                visited.append(side)
                queue.append(side)

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    
    for _ in range(n):
        node = input("Enter the node: ")
        edges = input(f"Enter the edges for {node} separated by space: ").split()
        graph[node] = edges
    
    return graph

graph = input_graph()

start_node = input("Enter the start node for BFS traversal: ")
goal = input("Enter the goal node: ")
bfs(visited, graph, start_node, goal)
