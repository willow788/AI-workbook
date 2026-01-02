import matplotlib.pyplot as plt
import networkx as nx
import time

#defnining the graph:
# A richer DAG (no cycles) so DFS is more interesting to watch.
graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I"],
    "E": ["J"],
    "F": ["J", "K"],
    "G": ["L"],
    "H": ["K", "M"],
    "I": ["M"],
    "J": ["N"],
    "K": ["N", "O"],
    "L": ["O"],
    "M": ["P"],
    "N": [],
    "O": [],
    "P": [],
}

#implementing DFS with trace
def dfs_with_trace(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            order.append(node)

        for n in reversed(graph[node]):
           if n not in visited:
                stack.append(n)

        yield node, order, stack, visited

#visualization function

G = nx.DiGraph()

for node in graph:
    for neighbour in graph[node]:
        G.add_edge(node, neighbour)

pos = nx.spring_layout(G, seed=42, k=2.2, iterations=400, scale=3.0)

plt.style.use("dark_background")
plt.ion()
fig, ax = plt.subplots(figsize=(13, 8))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

visited_color = "#22c55e"   # green (punchier on black)
frontier_color = "#60a5fa"  # blue
current_color = "#f59e0b"   # amber
default_color = "#334155"   # slate

step = 0
for current, order, stack, visited in dfs_with_trace(graph, "A"):
    step += 1
    node_colors = []

    for node_name in G.nodes():
        if node_name == current:
            node_colors.append(current_color)
        elif node_name in visited:
            node_colors.append(visited_color)
        elif node_name in stack:
            node_colors.append(frontier_color)
        else:
            node_colors.append(default_color)

    ax.clear()
    ax.set_axis_off()

    nx.draw_networkx_edges(
        G,
        pos=pos,
        ax=ax,
        arrows=True,
        arrowstyle="-|>",
        arrowsize=18,
        width=2,
        edge_color="#94a3b8",
        connectionstyle="arc3,rad=0.12",
    )
    nx.draw_networkx_nodes(
        G,
        pos=pos,
        ax=ax,
        node_color=node_colors,
        node_size=1500,
        linewidths=2,
        edgecolors="#e2e8f0",
    )
    nx.draw_networkx_labels(
        G,
        pos=pos,
        ax=ax,
        font_size=14,
        font_weight="bold",
        font_color="#f8fafc",
    )

    from matplotlib.patches import Patch

    legend_items = [
        Patch(facecolor=current_color, edgecolor="#334155", label="Current"),
        Patch(facecolor=visited_color, edgecolor="#334155", label="Visited"),
        Patch(facecolor=frontier_color, edgecolor="#334155", label="In stack"),
        Patch(facecolor=default_color, edgecolor="#334155", label="Unseen"),
    ]
    ax.legend(
        handles=legend_items,
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        frameon=True,
        framealpha=0.95,
        facecolor="#0b1220",
        edgecolor="#94a3b8",
        labelcolor="#f8fafc",
    )

    ax.set_title(
        f"DFS Traversal (step {step})\n"
        f"Order: {order}   |   Stack: {stack}",
        fontsize=14,
        fontweight="bold",
        color="#f8fafc",
    )
    # Leave room on the right for the legend so it never covers nodes.
    plt.tight_layout(rect=[0, 0, 0.82, 1])
    plt.pause(3.0)

plt.ioff()
plt.show()
               



