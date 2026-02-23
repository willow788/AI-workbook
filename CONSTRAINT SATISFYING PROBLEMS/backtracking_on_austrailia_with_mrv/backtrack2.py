#now we will solve the same problem using backtracking with mrv heuristic
#MRV stands for minimum remaining values 
"""In Mrv heuristic,
we will select the vector that has the minimum remaining values in the domain of the variable
we will select the variable that has the least number of legal values in its domain
"""

#defining the graph class
class Graph:
    def __init__(graph, nodes):
        #graph.n is the number of nodes in the graph, we are giving t the values of the nodes in the graph
        graph.n = nodes

        #here we are making a list of lists to represent the graph, we are initializing all the values in the graph to 0,
        #these values will be updated to 1 when we add an edge between two nodes in the graph

        graph.graph = [[0 for column in range(nodes)]
                       for row in range(nodes)]
        
    #function to check if the color is safe for colorin or not
    #logic - we will check if there is a edge between the current node and the adj node
    #if there is a edge we will see if the color of the adj node is same as the current node then it is not safe and we will not assign that color
    #otherwse it is safe to assign that color to the current node

    def is_safe(graph, color, current_node_to_color, color_id):
        for current_node in range(graph.n):
            #here we are definnig adj_node as the value of the graph at the current node and the adjacent node, if there is a edge between the current node and the adjacent node then adj_node will be 1 otherwise it will be 0
            adj_node = graph.graph[current_node_to_color][current_node] 
            adj_node_color = color[current_node]
            #here we are getting the color of the adjacent node 
            if adj_node == 1 and adj_node_color == color_id:
                return False
        return True
    
    #defining the mrv heurustic function
    #logic of the mrv heuristic :
    #we will select the variable that has the least number of legal values in its domain

    def mrv_heuristic(graph, color, no_of_available_colors):
        min_remaining_values = float('inf') #inintialised to infinity
        selected_node = -1 #none selected yet
        for node in range(graph.n):
            if color[node] == 0:  #node is not colored yet
                legal_values_count = 0
                for color_id in range(1, no_of_available_colors + 1):
                    if graph.is_safe(color, node, color_id):
                        legal_values_count += 1
                if legal_values_count < min_remaining_values:

                            #if the legal values is less than min values:
                            #we will uodate the min remaining vales to the legal values count
                            #also we will update the selected node to the current node

                     min_remaining_values = legal_values_count
                     selected_node = node
        return selected_node
    
    #function to solve the graph coloring problem using backtracking algorithm with mrv heuristic
    def graph_coloring(graph, no_of_available_colors, color):
        #here we are calling the mrv heuristic function to select the node with the minimum remaining values in its domain

        current_node_to_color = graph.mrv_heuristic(color, no_of_available_colors)
        #if current_node is -1:
        #it means all the nodes has been already colored and we have found a solution so we can return true
        if current_node_to_color == -1:
            return True
        #here we are trying to color the current node with all the available colors and checking if it is safe to color the current node with that color or not
        for current_color in range(1, no_of_available_colors + 1):

            #if it is safe then will assign that color to the current node
            
            if graph.is_safe(color, current_node_to_color, current_color):
                color[current_node_to_color] = current_color

                #here we are calling the graphh_coloring recursively to color next node
                #if it returns true--- we got a solution
                #otherwise we will backtrack and try to color the current node with the next color
                #color[current_node_to_color] = 0 
                #means we are unassigning the color from the current node and trying to assign the next color to the current node

                if graph.graph_coloring(no_of_available_colors, color):
                    return True
                color[current_node_to_color] = 0
        return False
    
    #here we are appling the graph coloring problem to the given graph and number of colors
    
g = Graph(7)
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5), (4, 6), (5, 6)]
for u, v in edges:
    g.graph[u][v] = 1
    g.graph[v][u] = 1
#m is the number of colors we are going to use to color the graph
#
number_of_available_colors = 3
coloring = [0] * g.n
is_colored = g.graph_coloring(number_of_available_colors, coloring)
color_names = {1: "Red", 2: "Green", 3: "Blue"}
node_names = {0: "West Australia",
              1: "Northern territory", 
              2: "South australia", 
              3: "Queensland", 
              4: "New south wales", 
              5: "Victoria",
              6: "Tasmania"}
    
if is_colored:
    print("Solution exists: Following are the assigned colors:")
    print("here we have used mrv heuristic to select the node with the minimum remaining values in its domain and then we have tried to color that node with all the available colors and checking if it is safe to color that node with that color or not")
    print("this is an approach to inprove the backtracking algorithm by reducing the search space and finding a solution faster,")
    print("we can see that the solution is same but faster.")
    print("we can also compare the number of steps taken to find the solution with and without mrv heuristic to see the difference in performance")
    #we can also compare the number of steps taken to find the solution with and without mrv heuristic to see the difference in performance 


    for i in range(g.n):
        color_id = coloring[i]
        print("Node", node_names[i], " --->  Color assigned:  ", color_names.get(color_id, "Unknown"))
else:
    print("No solution exists")
    

        


                            

                            
            
        
