# Hill-Climbing Search

import random

# Function to implement Hill-Climbing Search Algorithm
def hill_climbing_search(fn, neighbor_fn, x_range, max_iter) :
    current = random.choice(x_range)

    for i in range(max_iter) :
        neighbors = neighbor_fn(current)
        next_neighbor = max(neighbors, key = lambda x : fn(x))

        if fn(next_neighbor) <= fn(current) :
            break

        current = next_neighbor

    return current, fn(current)

# Function to obtain the function of x
def input_function() :
    str_func = input("Enter the function of x : ")
    return lambda x : eval(str_func)

# Function to obtain the neighborhood function
def input_neighbors_function() :
    step_size = float(input("Enter the step size of the function x : "))
    return lambda x : [x+dx for dx in [-step_size, 0, step_size]]

# Function to obtain the maximum iterations performable
def input_max_iter() :
    max_i = int(input("Enter the number of max iterations you want to perform : "))
    return max_i

# Function to obtain the user input of x range
def input_x_range() :
    start = int(input("Enter the start of the x range : "))
    end = int(input("Enter the end of the x range : "))
    return[x for x in range(start, end+1)]

# Function for running the script
if __name__ == "__main__" :
    fn = input_function()
    neighbor_fn = input_neighbors_function()
    x_range = input_x_range()
    max_iter = input_max_iter()

    best_solution, best_value = hill_climbing_search(fn, neighbor_fn, x_range, max_iter)
    print(f"Best Solution x : {best_solution} and Best Value fn(x) : {best_value}")
        

    


