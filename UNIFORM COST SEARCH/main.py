
import networkx  as nx
import heapq
import matplotlib.pyplot as plt
import numpy as np

#here we are implementing Uniform Cost Search Algorithm using matplotlib and python obiously

"""
1. initialisation is the first sstep where we create a priority queue to store the root node and its cost
2. we then enter a loop where we pop the node with the lowest cost from the priority queue
3. if the node is the goal node we return the path and cost"""



def reconstruct_path(visited, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1]
    path.reverse()
    return path

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]
    #initialising the priority queue with the start node and cost 0
    visited = {start: (0, None)} 
     # Dictionary to store the cost and parent of each visited node
    while priority_queue:
        # Pop the node with the lowest cost
        cost, node = heapq.heappop(priority_queue)

        #if current node is equal  to goal then we return the path and cost
        if node == goal:
            return cost, reconstruct_path(visited, start, goal)
        
        #exploring the neighbors of the current node
        for neighbor, cost in graph[node]:
            total_cost = cost + visited[node][0]

            #cheeck if previously visited or not
            if neighbor not in visited or total_cost < visited[neighbor][0]:
                visited[neighbor] = (total_cost, node)
                heapq.heappush(priority_queue, (total_cost, neighbor))

    
    return None


def vis_graph(graph, path):
    G = nx.Graph()

    #addin nodes aand edges to the graph

    for nodes, edges in graph.items():
        for neighbor, cost in edges:
            G.add_edge(nodes, neighbor, weight=cost)

    # Use a circular layout for better separation and less overlap
    pos = nx.circular_layout(G)

    # Enhanced visualization
    plt.figure(figsize=(12, 8))
    ax = plt.gca()
    ax.set_facecolor('black')
    plt.gcf().patch.set_facecolor('black')

    # Identify node types
    start_node = path[0] if path else None
    goal_node = path[-1] if path else None
    intermediate_nodes = set(path[1:-1]) if path and len(path) > 2 else set()
    # Draw all nodes with a shadow effect
    # Draw all nodes with different colors for start, goal, and intermediate
    node_colors = []
    for node in G.nodes():
        if node == start_node:
            node_colors.append('#00ff00')  # Green for start
        elif node == goal_node:
            node_colors.append('#ff0000')  # Red for goal
        elif node in intermediate_nodes:
            node_colors.append('#ffb347')  # Orange for path
        else:
            node_colors.append('#aee9f5')  # Default
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1200, edgecolors='white', linewidths=2, alpha=0.95)
    # Draw all edges
    nx.draw_networkx_edges(G, pos, edge_color='#b0b0b0', width=2, alpha=0.7)
    # Draw labels with a bold font and shadow
    # Add node labels with type, offsetting labels to avoid overlap
    node_labels = {}
    label_pos = {}
    for node in G.nodes():
        if node == start_node:
            node_labels[node] = f"{node}\n(Start)"
        elif node == goal_node:
            node_labels[node] = f"{node}\n(Goal)"
        elif node in intermediate_nodes:
            node_labels[node] = f"{node}\n(Path)"
        else:
            node_labels[node] = node
        # Offset label positions slightly outward from the node
        x, y = pos[node]
        angle = np.arctan2(y, x)
        label_pos[node] = (x + 0.15 * np.cos(angle), y + 0.15 * np.sin(angle))
    nx.draw_networkx_labels(G, label_pos, labels=node_labels, font_size=14, font_weight='bold', font_color='white', bbox=dict(facecolor='black', edgecolor='white', boxstyle='round,pad=0.3', alpha=0.8))
    # Draw edge weights
    labels = nx.get_edge_attributes(G, 'weight')
    # Offset edge labels to avoid node overlap
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12, font_color='#1a5276', bbox=dict(facecolor='white', edgecolor='none', alpha=0.6), label_pos=0.6)

    if path:
        # Only draw edges that exist in the graph
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1) if G.has_edge(path[i], path[i+1])]
        # Draw the path with a gradient color
        from matplotlib import colormaps
        colors = colormaps['autumn'](np.linspace(0, 1, len(path_edges)))
        for idx, edge in enumerate(path_edges):
            nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color=[colors[idx]], width=6, alpha=0.9, arrows=True, arrowstyle='-|>', arrowsize=30)
        # Annotate the path cost
        plt.text(0.01, 0.01, f"Path: {' → '.join(path)}", fontsize=14, color='#ffb347', transform=plt.gca().transAxes, bbox=dict(facecolor='black', alpha=0.7, boxstyle='round'))

    plt.title("Uniform Cost Search Path Visualization", fontsize=20, fontweight='bold', color='white', pad=20)
    plt.axis('off')
    plt.tight_layout(pad=2.0)
    plt.show()


#example graph represented as an adjacency list
# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Example usage of the UCS function
start_node = 'A'
goal_node = 'G'
result = uniform_cost_search(graph, start_node, goal_node)

if result:
    total_cost, path = result
    print(f"Least cost path from {start_node} to {goal_node}: {' -> '.join(path)} with total cost {total_cost}")
    vis_graph(graph, path)
else:
    print(f"No path found from {start_node} to {goal_node}")
