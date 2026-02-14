#python code of traditional anf baseline hill climbing algorithm in python

import numpy as np

#defining the oobjective function that can be seen to be denoted as a h function in the textbook
def objective_function(x):
    return  - (x[0]**2) + 5

#defining the generating neighbour function
def generating_neighbour(x, step_size=0.1):
    return (np.array([x[0] + step_size]),
            np.array([x[0] - step_size]),)
#this will generate two neighbours by adding and subtracting a step size to the first element of the input array x
#we can adjust the step size to control how far the neighbours are from the current solution

#defining the hill climbing algorithm
def hill_climbing(objective_function, initial, n_iterations = 100, step_size= 0.1):
    current = np.array(initial)
    current_obj = objective_function(current)

    for i in range(n_iterations):
        neighbours = generating_neighbour(current, step_size=step_size)
        neighbour_eval = np.array([objective_function(n) for n in neighbours])

        best_indx = int(np.argmax(neighbour_eval))

        if neighbour_eval[best_indx] > current_obj:
            current = neighbours[best_indx]
            current_obj = neighbour_eval[best_indx]
            print(f"Iteration {i+1}: New best solution found: {current} with objective value: {current_obj}")
        else:
            print(f"Iteration {i+1}: No better solution found. Current solution: {current} with objective value: {current_obj}")
            break
        
    return current, current_obj


#initialising the algorithm and running it
       
initial_guess = [2.0]
solution, value = hill_climbing(
        objective_function, 
        n_iterations=100,
        step_size=0.1,
        initial=initial_guess
        )

print(f"Best solution: {solution} with objective value: {value}")


   