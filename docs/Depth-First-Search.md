# 🌳 Depth-First Search (DFS)

<div align="center">

**Stack-Based Graph Traversal Algorithm**

![DFS Animation](https://img.shields.io/badge/Algorithm-DFS-orange?style=for-the-badge)
![Complexity](https://img.shields.io/badge/Time-O(V+E)-blue?style=for-the-badge)
![Space](https://img.shields.io/badge/Space-O(h)-green?style=for-the-badge)

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [How It Works](#-how-it-works)
- [Three Implementations](#-three-implementations)
- [Algorithm Pseudocode](#-algorithm-pseudocode)
- [Use Cases](#-use-cases)
- [Complexity Analysis](#-complexity-analysis)
- [Code Examples](#-code-examples)
- [Visualization Guide](#-visualization-guide)

---

## 🎯 Overview

**Depth-First Search (DFS)** is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. It's like exploring a maze by always taking the first unexplored path you see, going as deep as you can, then backtracking when you hit a dead end.

### Key Characteristics

- **Data Structure:** Stack (LIFO - Last In, First Out)
- **Exploration Strategy:** Go deep first, then backtrack
- **Implementation:** Recursive or iterative with explicit stack
- **Memory Usage:** O(h) where h is the maximum depth

---

## 🔍 How It Works

### Visual Example

```
Graph:        A
             / \
            B   C
           /|   |\
          D E   F G

DFS Traversal Order: A → B → D → E → C → F → G
```

### Step-by-Step Process

1. **Start** at the root/source node (A)
2. **Mark** the current node as visited
3. **Explore** the first unvisited neighbor
4. **Recurse** or push to stack
5. **Backtrack** when no unvisited neighbors remain
6. **Repeat** until all reachable nodes are visited

---

## 🛠️ Three Implementations

This project provides three progressive implementations to enhance learning:

### 1️⃣ Minimal Python Code

**Location:** `DEPTH FIRST SEARCH/minimal Python code/`

**Purpose:** Understand the core algorithm without distractions

**Features:**
- Pure Python, no external dependencies
- Recursive implementation
- Clean, readable code
- Perfect for beginners

**When to use:** When you want to understand the fundamental logic

---

### 2️⃣ DFS with Console Visuals

**Location:** `DEPTH FIRST SEARCH/DFS with Visuals/Python code/`

**Purpose:** See the algorithm in action through text output

**Features:**
- Stack state visualization
- Visited nodes tracking
- Step-by-step execution log
- Console-based output

**Sample Output:**
```
Visiting node: A
Stack that are visited: ['C', 'B']
visited nodes in the order: ['A']
-----
Visiting node: B
Stack that are visited: ['C', 'E', 'D']
visited nodes in the order: ['A', 'B']
-----
```

**When to use:** When you want to trace the algorithm's execution

---

### 3️⃣ DFS with Matplotlib Animation

**Location:** `DEPTH FIRST SEARCH/DFS using Matplotlib/Python code/`

**Purpose:** Beautiful, animated visualization

**Features:**
- Real-time graph visualization
- Color-coded node states
- Animated transitions
- Professional dark theme

**Node Colors:**
- 🟠 **Amber** - Current node being processed
- 🟢 **Green** - Visited nodes
- 🔵 **Blue** - Nodes in frontier (stack)
- ⚫ **Gray** - Unvisited nodes

**When to use:** When you want to see the algorithm visually

---

## 📋 Algorithm Pseudocode

### Recursive Implementation

```python
def DFS(graph, node, visited):
    # Mark current node as visited
    visited.add(node)
    
    # Process current node
    print(node)
    
    # Recursively visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)
```

### Iterative Implementation

```python
def DFS_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        # Pop from stack (LIFO)
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            print(node)
            
            # Push unvisited neighbors to stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
```

---

## 🎯 Use Cases

DFS is particularly useful for:

### ✅ Perfect For:
- **Path Finding** - Finding any path between two nodes
- **Cycle Detection** - Detecting cycles in graphs
- **Topological Sorting** - Ordering dependencies
- **Connected Components** - Finding graph components
- **Maze Solving** - Exploring all possible paths
- **Tree Traversal** - Pre-order, in-order, post-order

### ❌ Not Ideal For:
- **Shortest Path** - Use BFS instead
- **Level-Order Traversal** - Use BFS instead
- **Wide Graphs** - May go unnecessarily deep

---

## 📊 Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(V + E) | V = vertices, E = edges |
| **Space (Recursive)** | O(h) | h = height of recursion tree |
| **Space (Iterative)** | O(V) | Worst case: all vertices on stack |
| **Completeness** | Not guaranteed | May get stuck in infinite branches |

### Space Complexity Breakdown

- **Best Case:** O(log V) - Balanced tree
- **Average Case:** O(√V) - Random graphs
- **Worst Case:** O(V) - Linear chain

---

## 💻 Code Examples

### Example 1: Simple Graph

```python
# Define a simple graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Run DFS
visited = set()
DFS(graph, 'A', visited)

# Output: A B D E C F
```

### Example 2: With Path Tracking

```python
def DFS_with_path(graph, start, goal, path=[]):
    path = path + [start]
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = DFS_with_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    
    return None
```

---

## 🎨 Visualization Guide

### Running the Matplotlib Version

```bash
cd "DEPTH FIRST SEARCH/DFS using Matplotlib/Python code"
python main.py
```

### What You'll See

1. **Initial State** - All nodes in gray
2. **Animation Begins** - Current node turns amber
3. **Progress** - Visited nodes turn green
4. **Frontier** - Stack nodes in blue
5. **Completion** - All reachable nodes green

### Customization Options

Most implementations allow you to customize:
- Starting node
- Graph structure
- Animation speed
- Color schemes
- Node layout

---

## 🔄 DFS Variants

### 1. DFS for Trees
```python
def DFS_tree(root):
    if root is None:
        return
    print(root.value)  # Pre-order
    DFS_tree(root.left)
    DFS_tree(root.right)
```

### 2. DFS with Cycle Detection
```python
def has_cycle(graph):
    visited = set()
    rec_stack = set()
    
    for node in graph:
        if node not in visited:
            if DFS_cycle(graph, node, visited, rec_stack):
                return True
    return False
```

### 3. DFS for All Paths
```python
def all_paths_DFS(graph, start, goal):
    paths = []
    DFS_all_paths_helper(graph, start, goal, [], paths)
    return paths
```

---

## 📖 Learning Tips

1. **Start with the minimal version** - Understand the logic first
2. **Trace by hand** - Walk through small examples on paper
3. **Use the console version** - See what's happening internally
4. **Watch the animation** - Solidify your mental model
5. **Modify the code** - Try different graphs and parameters

---

## 🐛 Common Pitfalls

### Infinite Loops
```python
# ❌ WRONG - No visited check
def DFS_bad(graph, node):
    for neighbor in graph[node]:
        DFS_bad(graph, neighbor)  # Infinite loop!

# ✅ CORRECT - Track visited nodes
def DFS_good(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS_good(graph, neighbor, visited)
```

### Modifying During Iteration
```python
# ❌ WRONG
for node in visited:
    visited.add(new_node)  # Don't modify while iterating!

# ✅ CORRECT
new_nodes = []
for node in visited:
    new_nodes.append(calculate_new_node(node))
visited.update(new_nodes)
```

---

## 🔗 Related Topics

- [Breadth-First Search (BFS)](Breadth-First-Search.md) - The complementary algorithm
- [Visualization Techniques](Visualization-Techniques.md) - How to create animations
- [Customization Guide](Customization-Guide.md) - Tweaking parameters

---

<div align="center">

**Master DFS and unlock the foundation of graph algorithms! 🚀**

---

**Navigation:** [← Home](Home.md) | [Next: Breadth-First Search →](Breadth-First-Search.md)

</div>