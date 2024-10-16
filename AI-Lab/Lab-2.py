# Breadth-First Search

# Function to implement BFS Algorithm

def bfs(graph, start):
    visited = set()        # Set to keep track of visited nodes
    queue = [start]        # List used as a queue, starting with the start node
    visited.add(start)     # Mark the start node as visited

    while queue:
        node = queue.pop(0)    # Remove the first element from the list (queue)
        print(node, end = ' ')   # Print the current node

        # Iterate over all the neighbors of the current node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)    # Mark the neighbor as visited
                queue.append(neighbor)   # Add the neighbor to the end of the list (enqueue)

# Function to take user input for graph

def input_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))

    for i in range(vertices):
        vertex = input(f"Enter vertex {i+1}: ")
        neighbors = input(f"Enter the neighbors of {vertex} seperated by a space : ").split()
        graph[vertex] = neighbors

    return graph

# Function for running the script
if __name__ == "__main__":
    graph = input_graph()   
    start = input("Enter the start node for BFS: ")

    print("BFS traversal:")
    bfs(graph, start)
