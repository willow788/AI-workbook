#case1: we know the model 
discount_factor = 0.9
import numpy as np
v = np.zeros(10)
#this is a one dimension mdp

def next_state(s):
    return min((s+1), 9)

def reward(s):
    if s == 9:
        return 4
    else:
        return -1
    
for i in range(10):
    new_v = np.copy(v)
    for s in range(10):
        next_s = next_state(s)
        r = reward(s)
        new_v[s] = r + discount_factor * v[next_s]
    v = new_v

print('value function given the model is: ', v  )
