#here we are going to implement the tabu search algorithm for n queens problem

import numpy as np

#definning a queue class to keep track of the tabu list
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def _normalize(self, item):
        if isinstance(item, np.ndarray):
            return tuple(int(x) for x in item.tolist())
        if isinstance(item, list):
            return tuple(int(x) for x in item)
        return item

    def enqueue(self, item):
        item = self._normalize(item)
        if len(self.queue) >= self.max_size:
            self.dequeue()
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def is_full(self):
        return len(self.queue) >= self.max_size

    def __contains__(self, item):
        return self._normalize(item) in self.queue
    
#defining the objective function for n queens problem
def objective_function(state):
    #we have to count the number of pairs of queens that are attacking each other
    attacking_pairs = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            #two queens are attacking each other if they are in the same column or in the same diagonal
            #we can check if they are in the same column by comparing their values and we can check if they are in the same diagonal by comparing the absolute difference of their values with the absolute difference of their indices
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1
    return -attacking_pairs

#defining the generating neighbour function for n queens problem
def generating_neighbour(state):
    neighbours = []
    m = len(state)
    for i in range(m):
        for j in range(m):
            if state[i] != j:
                neighbour = state.copy()
                neighbour[i] = j
                neighbours.append(neighbour)
    return neighbours


#defining the best heuristic function to select the best neighbour
def best_heuristic(neighbours, objective_function):
    best_neighbour = None
    best_value = float('-inf')
    for neighbour in neighbours:
        value = objective_function(neighbour)
        if value > best_value:
            best_value = value
            best_neighbour = neighbour
    return best_neighbour, best_value

#defining the tabu search algorithm
def tabu_search(objective_function, initial, n_iterations = 100, tabu_size = 10):
    current= np.array(initial)
    current_obj = objective_function(current)
    tabu_list = Queue(max(1, int(tabu_size)))
    for i in range(n_iterations):
        neighbours = generating_neighbour(current)
        best_neighbour, best_value = best_heuristic(neighbours, objective_function)
        if best_value > current_obj and best_neighbour not in tabu_list:
            current = best_neighbour
            current_obj = best_value
            tabu_list.enqueue(current)
            print(f"Iteration {i+1}: New best solution found: {current} with objective value: {current_obj}")
        else:
            print(f"Iteration {i+1}: No better solution found. Current solution: {current} with objective value: {current_obj}")

    return current, current_obj 

#initialising the algorithm and running it
initial_guess = [0, 1, 2, 3] #this is a solution for 4 queens problem where all queens are in the same column
solution, value = tabu_search(
        objective_function, 
        n_iterations=100,
        tabu_size=10,
        initial=initial_guess
        )
print(f"Best solution: {solution} with objective value: {value}")


