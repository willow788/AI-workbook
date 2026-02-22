#her were are going to apply the backtracking  algortihm on graph coloring problem


#first we will create a graph class to represent the graph and its properties
class graph:
    def __init__(self, nodes):
        self.n = nodes
        self.graph = [[0 for column in range(nodes)]
                      for row in range(nodes)]
        
    #function to check if the color is safe for coloring that node of the graph or not
    def is_Safe(self, color, current_node_to_color, color_id):
        for current_node in range(self.n):
            #here we are checking if there is an edge between the current node and the adjacent node and if the color of the adjacent node is same as the current node then it is not safe to color the current node with that color
            if self.graph[current_node_to_color][current_node] == 1 and color[current_node] == color_id:
                return False
        return True
            
    #function to solve the graph coloring problem using backtracking algorithm
    #here c = current_node_to_color
    #m = nubmer of colors

    def graph_coloring(self, no_of_available_colors, color, current_node_to_color):

        if self.n == current_node_to_color:
            return True
        
        for current_color in range(1, no_of_available_colors+1):
            if self.is_Safe(color, current_node_to_color, current_color):
                color[current_node_to_color] = current_color
                #here we are calling the graph_coloring function recursively to color the next node of the graph and if it returns true then we have found a solution and we can return true otherwise we will backtrack and try to color the current node with the next color
                if self.graph_coloring(no_of_available_colors, color, current_node_to_color+1):
                    return True
                color[current_node_to_color] = 0
        return False
    
    #here we are appling the graph coloring problem to the given graph and number of colors
    #we will be using red green and blue as the colors to color the graph
    def graph_coloring_util(self, no_of_available_colors):
        color = [0] * self.n
        if not self.graph_coloring(no_of_available_colors, color, 0):
            return False
        return color
    
#here we are creating a graph and adding edges to it
g = graph(7)
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5), (4, 6), (5, 6)]
for u, v in edges:
    g.graph[u][v] = 1
    g.graph[v][u] = 1
#m is the number of colors we are going to use to color the graph
#
number_of_available_colors = 3
coloring = g.graph_coloring_util(number_of_available_colors)
color_names = {1: "Red", 2: "Green", 3: "Blue"}
node_names = {0: "west australia", 1: "northern territory", 2: "south australia", 3: "queensland", 4: "new south wales", 5: "victoria", 6: "tasmania"}
    
if coloring:
    print("Solution exists: Following are the assigned colors:")
    for i in range(g.n):
        color_id = coloring[i]
        print("Node", node_names[i], " --->  Color assigned:  ", color_names.get(color_id, "Unknown"))
else:
    print("No solution exists")


            

        
