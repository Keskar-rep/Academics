# Depth-First Search

# Function to implement DFS Algorithm 

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end =' ')

    for neighbor in graph[start] :
        if neighbor not in visited :
            dfs(graph, neighbor, visited)

# Function to take a user input for the graph

def input_graph():
    graph={}
    vertices = int(input("Enter the number of vertices in the graph : "))

    for i in range(vertices):
        vertex = input(f"Enter vertex number {i+1} : ")
        neighbors = input(f"Enter the neighbors of vertex {vertex} seperated by a space : ").split()
        graph[vertex] = neighbors

    return graph

# Function to run the script

if __name__ == "__main__" :
    graph = input_graph()
    start = input(f"Enter the start node for DFS : ")
    
    print("DFS Traversal : ")
    dfs(graph, start)
    




    


