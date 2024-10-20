import heapq  

# A* Algorithm Implementation

def a_star(graph, start, goal, heuristic):
    # Priority queue for open set
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], start))  # (f_score, node)

    # Dictionaries to keep track of costs
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[neighbor]:  # A better path has been found
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]

                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # If there is no path

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]  # Return reversed path

# Function to input the graph from the user
def input_graph():
    graph = {}
    edges = int(input("Enter the number of edges in the graph: "))

    for _ in range(edges):
        edge_input = input("Enter edge (format: start_node end_node weight): ")
        start_node, end_node, weight = edge_input.split()
        weight = int(weight)

        if start_node not in graph:
            graph[start_node] = []
        graph[start_node].append((end_node, weight))

        if end_node not in graph:
            graph[end_node] = []
        graph[end_node].append((start_node, weight))  # Comment this line if the graph is directed

    return graph

# Function to input heuristic values from the user
def input_heuristics(graph):
    heuristic = {}
    for node in graph:
        value = float(input(f"Enter heuristic value for {node}: "))
        heuristic[node] = value
    return heuristic

# Function to run the A* algorithm
if __name__ == "__main__":
    graph = input_graph()  # Get graph input from user
    heuristic = input_heuristics(graph)  # Get heuristic values for nodes
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    path = a_star(graph, start_node, goal_node, heuristic)

    if path:
        print(f"The shortest path from {start_node} to {goal_node} is: {path}")
    else:
        print(f"There is no path from {start_node} to {goal_node}.")
