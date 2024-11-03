# Missionaries and Cannibals Problem

from collections import deque

# Define the initial and goal states
initial_state = (3, 3, 1)  
goal_state = (0, 0, 0)   

# Define possible moves
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

# Function to check if state is valid

def is_valid_state(missionaries_left, cannibals_left):
    if missionaries_left < 0 or cannibals_left < 0 or missionaries_left > 3 or cannibals_left > 3:
        return False
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    return True

# Function to implement solution for Missionaries and Cannibals problem

def solve_missionaries_and_cannibals():
    queue = deque([(initial_state, [])]) 
    visited = set()
    visited.add(initial_state)
    
    while queue:
        (missionaries_left, cannibals_left, boat), path = queue.popleft()
        
        
        if (missionaries_left, cannibals_left, boat) == goal_state:
            return path + [(missionaries_left, cannibals_left, boat)]
        
        # Try all possible moves
        for m, c in moves:
            if boat == 1:  
                new_state = (missionaries_left - m, cannibals_left - c, 0)
            else: 
                new_state = (missionaries_left + m, cannibals_left + c, 1)
                
            # Check if the new state is valid and hasn't been visited
            if is_valid_state(new_state[0], new_state[1]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(missionaries_left, cannibals_left, boat)]))
    
    return None  


# Run the program and print the solution path

solution_path = solve_missionaries_and_cannibals()

if solution_path:
    for step, state in enumerate(solution_path):
        print(f"Step {step}: Missionaries Left = {state[0]}, Cannibals Left = {state[1]}, Boat Position = {'Left' if state[2] == 1 else 'Right'}")
else:
    print("No solution found.")
