# Water-Jug Problem

# Function to implement solution for Water-Jug Problem

def water_jug_problem_dfs(x, y, z):
    if z > max(x, y) or z % gcd(x, y) != 0:
        print("No solution: Target amount cannot be measured.")
        return False
    
    visited = set()
    path = []
    stack = [(0, 0, [])] 
    
    while stack:
        jug1, jug2, current_path = stack.pop()
        current_path.append((jug1, jug2))
        
        if jug1 == z or jug2 == z:
            print(f"Solved: ({jug1}, {jug2})")
            print("Path to solution:")
            for state in current_path:
                print(state)
            return True
        
        if (jug1, jug2) in visited:
            continue
        
        visited.add((jug1, jug2))
        
        next_states = []
        
        # Fill jug1
        next_states.append((x, jug2))
        # Fill jug2
        next_states.append((jug1, y))
        # Empty jug1
        next_states.append((0, jug2))
        # Empty jug2
        next_states.append((jug1, 0))
        # Pour water from jug1 to jug2
        pour_to_jug2 = min(jug1, y - jug2)
        next_states.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        # Pour water from jug2 to jug1
        pour_to_jug1 = min(jug2, x - jug1)
        next_states.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
        
        # Add all valid new states to the stack
        for state in next_states:
            if state not in visited:
                stack.append((state[0], state[1], current_path.copy()))
    
    # If no solution was found
    print("No solution: Target amount cannot be measured.")
    return False

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
        x = int(input("Enter the capacity of Jug X: "))
        y = int(input("Enter the capacity of Jug Y: "))
        z = int(input("Enter the target amount of water to measure: "))

        water_jug_problem_dfs(x, y, z)
