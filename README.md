<div align="center">

# 🔍 Exploring Uninformed Search Methods

### *A Visual Journey Through AI Search Algorithms*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Artificial_Intelligence-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

*Implementations inspired by **Artificial Intelligence: A Modern Approach***

---

</div>

## 📚 About This Project

This repository is a collection of **uninformed search algorithm** implementations created as part of my AI class journey. Each algorithm is implemented with multiple approaches to help learners progress from basic concepts to advanced visualizations.

> 💡 **Learning Resource:** These implementations are based on concepts from *Artificial Intelligence: A Modern Approach* by Stuart Russell and Peter Norvig.

---

## 🎯 What's Inside

### ✅ Current Implementations

<table>
<tr>
<td width="50%">

#### 🌳 **Depth-First Search (DFS)**

Explore the depths of graph traversal with three progressive implementations:

1. **📝 Minimal Python Code**
   - Clean, recursive DFS implementation
   - Perfect for understanding the core algorithm
   - No external dependencies

2. **🖥️ DFS with Visuals**
   - Stack trace visualization
   - Console output showing visited nodes
   - Step-by-step execution logging

3. **📊 DFS using Matplotlib**
   - Beautiful graph visualization
   - Real-time animated search process
   - Color-coded nodes showing algorithm state

**Node Color Legend:**
- 🟠 **Amber** - Current node being processed
- 🟢 **Green** - Visited nodes
- 🔵 **Blue** - Nodes in the frontier (stack)
- ⚫ **Gray** - Unvisited nodes

</td>
<td width="50%">

#### 🌊 **Breadth-First Search (BFS)**

**🎉 NEW!** Level-by-level graph exploration with stunning visualizations:

**Features:**
- 🎲 **Random Graph Generation** - Automatically creates test graphs
- 🌀 **Force-Directed Layout** - Beautiful Fruchterman-Reingold spring layout
- 🎨 **Advanced Visualization** - High-quality matplotlib animations
- ⚡ **Queue-Based Traversal** - Classic BFS using deque
- 🎛️ **Customizable Parameters**:
  - Adjustable graph size (default: 20 nodes)
  - Configurable edge probability
  - Animation speed control
  - Layout customization

**Special Highlights:**
- Dependency-free force-directed positioning algorithm
- Smooth animations showing queue operations
- Real-time visualization of the BFS frontier
- Professional dark-themed graphics

</td>
</tr>
</table>

---

## 🚀 Coming Soon

Additional uninformed search methods will be added following similar implementation approaches:

- [x] **Depth-First Search (DFS)** ✅
- [x] **Breadth-First Search (BFS)** ✅ *NEW!*
- [ ] **Uniform Cost Search (UCS)**
- [ ] **Depth-Limited Search (DLS)**
- [ ] **Iterative Deepening Search (IDS)**
- [ ] **Bidirectional Search**

---

## 🎨 Features

<div align="center">

| Feature | Description |
|---------|-------------|
| ✨ **Progressive Learning** | From minimal code to full visualization |
| 📖 **Well-Documented** | Clear comments explaining each step |
| 🎭 **Beautiful Visuals** | Dark-themed, professional matplotlib outputs |
| 🔄 **Animated Algorithms** | Watch the search unfold in real-time |
| 🧠 **Educational Focus** | Built for learning and understanding |
| 🎲 **Random Graph Generation** | Test algorithms on different graph structures |
| 🌀 **Advanced Layouts** | Force-directed positioning for clarity |

</div>

---

## 🛠️ Installation & Usage

### Prerequisites

```bash
# Install required packages
pip install matplotlib numpy

# For DFS implementations (optional)
pip install networkx
```

### Running the Examples

#### 🌳 Depth-First Search

**Minimal Implementation:**
```bash
cd "DEPTH FIRST SEARCH/minimal Python code"
python main.py
```

**With Console Visualization:**
```bash
cd "DEPTH FIRST SEARCH/DFS with Visuals/Python code"
python main.py
```

**With Matplotlib Animation:**
```bash
cd "DEPTH FIRST SEARCH/DFS using Mathplotlib/Python code"
python main.py
```

#### 🌊 Breadth-First Search

```bash
cd "BREADTH FIRST SEARCH/Python code"
python bfs.py
```

**Customize BFS Parameters** (edit in bfs.py):
```python
num_nodes = 20              # Number of nodes in graph
edge_prob = 0.2             # Probability of edge creation
start_node = 0              # Starting node for search
animation_speed = 1200      # Milliseconds per frame
use_force_directed_layout = True  # Use spring layout
```

---

## 📖 Example Output

### 🌳 DFS Console Visualization
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

### 🌊 BFS Visualization Features

The BFS implementation includes:
- **Random Graph Generation** - Creates diverse test cases automatically
- **Force-Directed Layout** - Nodes positioned using physics simulation for optimal clarity
- **Animated Queue Operations** - Watch as nodes are enqueued and dequeued
- **Color-Coded States** - Visual distinction between visited, frontier, and unexplored nodes
- **Professional Styling** - Clean, modern visualization with legends and labels

---

## 🎓 Learning Objectives

These implementations were created to provide multiple perspectives on understanding search algorithms:

1. **Understand** the logic (minimal code)
2. **Trace** the execution (console output)
3. **Visualize** the process (graphical animation)
4. **Experiment** with different graph structures (random generation)

### 🔬 Key Differences: DFS vs BFS

| Aspect | DFS | BFS |
|--------|-----|-----|
| **Data Structure** | Stack (LIFO) | Queue (FIFO) |
| **Exploration** | Deep before wide | Wide before deep |
| **Use Cases** | Path finding, cycle detection | Shortest path, level-order |
| **Memory** | O(h) - height | O(w) - width |
| **Completeness** | Not guaranteed | Guaranteed (finite graphs) |

---

## 👤 Credits

### Code & Implementation
**[@willow788](https://github.com/willow788)**
- Core algorithm logic
- DFS & BFS implementations
- Random graph generation
- Force-directed layout algorithm
- Project structure and organization

### Design & Visual Enhancements
**GitHub Copilot**
- Matplotlib styling and aesthetics
- Animation improvements
- Code documentation
- README enhancements

---

## 📚 References

- **Russell, S., & Norvig, P.** *Artificial Intelligence: A Modern Approach*
- **Fruchterman, T. M., & Reingold, E. M.** (1991). Graph Drawing by Force-directed Placement
- [Matplotlib Documentation](https://matplotlib.org/)
- [NumPy Documentation](https://numpy.org/)
- [Python Collections - deque](https://docs.python.org/3/library/collections.html#collections.deque)

---

## 🎯 Educational Context

This project was created as part of my **Artificial Intelligence** coursework, with a focus on:
- Understanding fundamental search algorithms from first principles
- Implementing algorithms in progressively complex ways
- Creating effective visualizations for learning
- Exploring the differences between search strategies

Perfect for students learning AI, algorithm visualization enthusiasts, and anyone interested in understanding how search algorithms work!

---

## 📝 License

This project is open source and available for educational purposes.

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Happy Learning! 🎓**

[![GitHub followers](https://img.shields.io/github/followers/willow788?style=social)](https://github.com/willow788)
[![GitHub stars](https://img.shields.io/github/stars/willow788/Exploring-Uninformed-Search-Methods?style=social)](https://github.com/willow788/Exploring-Uninformed-Search-Methods)

---

*Made with ❤️ for AI learners everywhere*

</div>
