#this is the most minimal implementation of a depth-first search algorithm in Python

#we are using a recursive approach to explore all nodes in a graph

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)


    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

result = dfs_recursive(graph, 'A')

#basic explanation of the code:
#here we are writing a function dfs_recursive that takes a graph, a starting node, and a set of visited nodes
#then we are covering the base case where visited is None and initializing it as an empty set

#that is just a edge case handling
#then we are adding the starting node to the visited set
#after that we are iterating through all the neighbours of the starting node
#for each neighbour node, we are checking if it has not been visited yet
#if it has not been visited, we are calling the dfs_recursive function recursively on that neighbour node
#finally, we are returning the visited set which contains all the nodes that were visited during the DFS traversal
