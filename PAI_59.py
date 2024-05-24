from collections import deque

def astar_solve(jug1_capacity, jug2_capacity, target):
    # To store visited states
    visited = set()
    # To store the steps
    path = []
    # Use a queue to perform BFS
    q = deque()
    # Initial state
    q.append((0, 0))  # Both jugs are initially empty
    while q:
        state = q.popleft()

        # If we have already visited this state, skip it
        if state in visited:
            continue
        # Mark this state as visited
        visited.add(state)

        # Record the path
        path.append(state)
        jug1, jug2 = state

        # If either jug has the target amount of water, we are done
        if jug1 == target or jug2 == target:
            path.append(state)
            print_steps(path)
            return True

        # Generate all possible next states and add them to the queue
        # Fill jug1
        q.append((jug1_capacity, jug2))
        # Fill jug2
        q.append((jug1, jug2_capacity))
        # Empty jug1
        q.append((0, jug2))
        # Empty jug2
        q.append((jug1, 0))
        # Pour jug1 to jug2
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        q.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        # Pour jug2 to jug1
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        q.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))

    # If we exhaust all possibilities and do not find a solution
    print("No solution.")
    return False

def print_steps(path):
    for step in path:
        print(f"Jug1: {step[0]} liters, Jug2: {step[1]} liters")

# Example usage
jug1_capacity = 7
jug2_capacity = 3
target = 5

print(astar_solve(jug1_capacity, jug2_capacity, target))