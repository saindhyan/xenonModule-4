from collections import deque

# State of the question
class State:
    # Set missionaries and cannibals at left and right
    def __init__(self, missionaries_left, cannibals_left, boat, missionaries_right, cannibals_right):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat = boat
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right

    #check if current state is valid (Game over)
    def is_valid(self):
        # Check if missionaries and cannibals are non-negative
        if (self.missionaries_left < 0 or self.cannibals_left < 0 or
                self.missionaries_right < 0 or self.cannibals_right < 0):
            return False
        # Check if missionaries are outnumbered by cannibals on either side
        if (0 < self.missionaries_left < self.cannibals_left) or \
                (0 < self.missionaries_right < self.cannibals_right):
            return False
        return True

    # check if target achive (both 0 at left)
    def is_goal_state(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def __eq__(self, other):
        return (self.missionaries_left, self.cannibals_left, self.boat,
                self.missionaries_right, self.cannibals_right) == \
               (other.missionaries_left, other.cannibals_left, other.boat,
                other.missionaries_right, other.cannibals_right)

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left,
                     self.boat, self.missionaries_right, self.cannibals_right))

    def __str__(self):
        return f"({self.missionaries_left}, {self.cannibals_left}, {self.boat}, {self.missionaries_right}, {self.cannibals_right})"

# get all possible next state
def get_next_states(current_state):
    next_states = []
    # if boat at left
    if current_state.boat == 'left':
        for i in range(3):
            for j in range(3):
                if 0 < i + j <= 2:
                    next_state = State(current_state.missionaries_left - i, current_state.cannibals_left - j, 'right',
                                       current_state.missionaries_right + i, current_state.cannibals_right + j)
                    if next_state.is_valid():
                        next_states.append(next_state)
    #if boat at right
    else:
        for i in range(3):
            for j in range(3):
                if 0 < i + j <= 2:
                    next_state = State(current_state.missionaries_left + i, current_state.cannibals_left + j, 'left',
                                       current_state.missionaries_right - i, current_state.cannibals_right - j)
                    if next_state.is_valid():
                        next_states.append(next_state)
    return next_states

# bfs for problem
def breadth_first_search():
    #initial problem state
    initial_state = State(3, 3, 'left', 0, 0)
    visited = set()
    queue = deque([initial_state])
    parent = {}

    while queue:
        current_state = queue.popleft()

        # check target
        if current_state.is_goal_state():
            # Construct the path to the solution
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent.get(current_state)
            path.reverse()
            return path

        visited.add(current_state)

        # Get next possible states
        next_states = get_next_states(current_state)

        # add next states that are not visited
        for next_state in next_states:
            if next_state not in visited:
                queue.append(next_state)
                parent[next_state] = current_state
    # solution not found
    return None

def print_solution(path):
    print("Solution:")
    #Printing Path returned
    for idx, state in enumerate(path):
        print(f"Step {idx + 1}: {state}")

path = breadth_first_search()
if path:
    print_solution(path)
else:
    print("Solution not found :(")
