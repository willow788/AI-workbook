#here we are impleementing minnimax algorithm for a very simple basic game will explore other games too in futher videos

import math

def minimax_search(current_depth, node_index, max_turn, scores, target_Depth):

    #base case that the target depth is reached as in a solution is found
    if target_Depth == current_depth:
        return scores[node_index]
    if max_turn:
        return max(minimax_search(current_depth + 1, node_index*2, False, scores, target_Depth), minimax_search(current_depth + 1, node_index*2 + 1, False, scores, target_Depth))
    else:
        return min(minimax_search(current_depth + 1, node_index*2, True, scores, target_Depth), minimax_search(current_depth + 1, node_index*2 + 1, True, scores, target_Depth))

#driving code
scores_for_evaluation = [3, 5, 2, 1, 4, 6, 7, 8]

tree_depth = math.log(len(scores_for_evaluation), 2)

print("the optimal value is : ", end="")
print(minimax_search(0, 0, True, scores_for_evaluation, tree_depth))
