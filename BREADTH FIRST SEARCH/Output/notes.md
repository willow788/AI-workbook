
# Breadth-First Search (BFS)

Breadth-First Search (BFS) is a graph traversal algorithm used to explore nodes and edges of a graph level by level. It starts from a chosen source node and visits all its neighbors before moving to the next level of nodes.

BFS works on both **graphs** and **trees**, and is particularly useful when the shortest path (in terms of number of edges) is needed in an unweighted graph.

---

## Key Ideas

- BFS uses a **queue (FIFO)** to keep track of nodes to explore.
- Nodes are processed **level by level**.
- A **visited set** prevents revisiting nodes and getting stuck in cycles.
- Works on:
  - Directed graphs
  - Undirected graphs
  - Connected or disconnected graphs

---

## Algorithm Steps

1. Choose a starting node.
2. Mark it as visited and put it into a queue.
3. While the queue is not empty:
   - Remove the node from the front of the queue.
   - Visit all its unvisited neighbors.
   - Mark neighbors as visited and add them to the queue.
4. Continue until the queue becomes empty.

---

## Pseudocode

```text
BFS(graph, start):
    create a queue Q
    mark start as visited
    enqueue start into Q

    while Q is not empty:
        node = dequeue from Q
        
        for each neighbor of node:
            if neighbor is not visited:
                mark neighbor as visited
                enqueue neighbor
````

---

## Time and Space Complexity

| Property | Complexity   |
| -------- | ------------ |
| Time     | **O(V + E)** |
| Space    | **O(V)**     |

Where:

* `V` = number of vertices
* `E` = number of edges

---

## Common Uses of BFS

* Finding the **shortest path in an unweighted graph**
* Level-order traversal of trees
* Checking if a graph is bipartite
* Finding connected components
* Networking: packet routing
* Web crawlers
* AI search problems (shortest moves)

---

## Example Output Order

If BFS starts at node `A`, a possible traversal could be:

`A → B → C → D → E → F`

Order depends on adjacency list ordering.

---

## BFS vs DFS (Quick Comparison)

| Feature                     | BFS            | DFS              |
| --------------------------- | -------------- | ---------------- |
| Structure used              | Queue          | Stack/Recursion  |
| Traversal style             | Level-by-level | Deep-first       |
| Shortest path (unweighted)? | ✔ Yes          | ✘ Not guaranteed |
| Memory                      | Higher         | Lower            |

---

## Visualization Meaning (if included)

In the animation:

* **Gray nodes** → Not yet discovered
* **Orange nodes** → In the queue (frontier)
* **Green nodes** → Fully visited
* **Blue edges** → Discovered edges during traversal

This helps understand the algorithm flow visually.

---

## Code Reference

The repository includes a Python implementation from scratch along with a Matplotlib visualization that animates BFS traversal in real time.

---

## Summary

Breadth-First Search is one of the most fundamental graph algorithms. Its level-order exploration and shortest-path guarantee in unweighted graphs make it a core tool in computer science, networking, AI, and competitive programming.

Understanding BFS helps build strong intuition for more advanced graph algorithms.

---

```



