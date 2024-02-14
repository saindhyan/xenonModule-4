def pour_water(jug1_max, jug2_max, target_amount):
    # Check if the target amount is feasible
    if target_amount > max(jug1_max, jug2_max) or target_amount % gcd(jug1_max, jug2_max) != 0:
        print("Target amount is not feasible.")
        return None

    visited = set()
    queue = [(0, 0, [])]  # (jug1, jug2, steps)

    # BFS to find the solution
    while queue:
        jug1, jug2, steps = queue.pop(0)

        # Check if the target amount is reached or not
        if jug1 == target_amount:
            return jug1, jug2, steps

        # Check current state in visited
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Fill jug-1
        if jug1 < jug1_max:
            queue.append((jug1_max, jug2, steps + ['Fill jug1']))


        # Fill jug-2
        if jug2 < jug2_max:
            queue.append((jug1, jug2_max, steps + ['Fill jug2']))

        # Empty jug-1
        if jug1 > 0:
            queue.append((0, jug2, steps + ['Empty jug1']))

        # Empty jug-2
        if jug2 > 0:
            queue.append((jug1, 0, steps + ['Empty jug2']))

        # Pour from jug-1 to jug-2
        if jug1 > 0 and jug2 < jug2_max:
            pour = min(jug1, jug2_max - jug2)
            queue.append((jug1 - pour, jug2 + pour, steps + ['Pour from jug1 to jug2']))

        # Pour from jug-2 to jug-1
        if jug2 > 0 and jug1 < jug1_max:
            pour = min(jug2, jug1_max - jug1)
            queue.append((jug1 + pour, jug2 - pour, steps + ['Pour from jug2 to jug1']))

    # if solution not found
    return None

# Find gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a



# user-defined jug sizes and target amount
print("\nProblem Values:")
jug1_max = int(input("Enter the size of the first jug: "))
jug2_max = int(input("Enter the size of the second jug: "))
target_amount = int(input("Enter the target amount: "))
result = pour_water(jug1_max, jug2_max, target_amount)
if result:
    jug1, jug2, steps = result
    print("Steps to achieve the target amount:")
    for step in steps:
        print(step)
    print("jug1 - ",jug1,"Jug2 - ",jug2)
else:
    print("solution not found.")
