# Uniform-Cost Search

import heapq

# Function to implement UCS Algorithm

def uniform_cost_search(graph, start, goal) :
    priority_queue = [(0,start)]
    visited = set()
    costs = {start: 0}

    while priority_queue :
        # Fetching node with the lowest cost
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal :
            return current_cost
        
        if current_node in visited:
            continue

        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node] :
            new_cost = current_cost + weight

            # To check if the new path of the neighbor is cheaper
            if neighbor not in visited and(neighbor not in costs or new_cost < costs[neighbor]) :
                costs[neighbor] = new_cost 
                heapq.heappush(priority_queue, (new_cost, neighbor))
    
    # If the goal is not reachable
    return -1

# Function to take user input for graph

def input_graph() :
    graph = {}
    edges = int(input("Enter the number of edges in the graph : "))
    print("The format for entering edges is : start_node, goal_node, weight ")

    for i in range(edges) :
        edges = input("Enter edge : ")
        start_node, goal_node, weight = edges.split()
        weight = int(weight)

        if start_node not in graph :
            graph[start_node] = []
        graph[start_node].append((goal_node, weight))

        # If the graph is undirected, add the reverse edge

        if goal_node not in graph :
            graph[goal_node] = []
        graph[goal_node].append((start_node, weight))

    return graph

# Function for running the script

if __name__ == "__main__" :
    graph = input_graph()
    start = input("The start node for the graph is : ")
    goal = input("The goal node for the graph is : ")

    cost = uniform_cost_search(graph, start, goal)

    if cost > 0 :
        print(f"The cost of the least-cost path from {start} to {goal} is: {cost}")
    else:
        print(f"There is no path from {start} to {goal}.")
