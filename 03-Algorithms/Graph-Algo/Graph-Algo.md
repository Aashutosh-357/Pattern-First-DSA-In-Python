# 🕸️ Graph Algorithms: The Network Navigator

![Graph Algorithms](https://img.shields.io/badge/Topic-Graph_Algorithms-darkgreen?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Advanced-red?style=for-the-badge)
![Time](https://img.shields.io/badge/Study_Time-5_Hours-orange?style=for-the-badge)

> **"The Web of Connections"**
> 
> In the digital age, everything is connected. Social networks, recommendation engines, GPS navigation, task scheduling - they all rely on graphs. A graph is not just dots and lines; it's a mathematical model of relationships that powers the modern world.

Welcome to the world of **network intelligence** - where connections reveal insights.

---

## 🧠 1. The Blueprint (Concept & Structure)

### 🌐 The Analogy
A graph is like a **city map**:
- **Vertices (Nodes)**: Cities, intersections, landmarks
- **Edges**: Roads, highways, connections between cities
- **Weighted Edges**: Roads with different travel times/distances
- **Directed Edges**: One-way streets

### 🎯 Graph Representations

#### 📋 Adjacency List (Most Common)
```python
# Undirected Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

#### 📊 Visual Representation
```
    A ---- B ---- D
    |      |
    |      |
    C ---- F ---- E
```

---

## 🔍 2. Graph Traversal: Exploring the Network

### 🌊 Breadth-First Search (BFS): The Level Explorer

#### 📖 The Concept
Explore **all neighbors first** before going deeper. Like ripples in a pond spreading outward.

#### 🎯 When to Use
- **Shortest path** in unweighted graphs
- **Level-order traversal** (social network degrees of separation)
- **Connected components** detection
- **Bipartite graph** checking

#### 📊 Visual BFS Traversal
```
Starting from A:

Level 0: [A]
Level 1: [B, C]        (A's neighbors)
Level 2: [D, E, F]     (B and C's neighbors)

Order: A → B → C → D → E → F
```

#### 🐍 Implementation
```python
from collections import deque
from typing import Dict, List, Set

def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """🌊 BFS Traversal - O(V + E) time, O(V) space"""
    visited: Set[str] = set()
    queue = deque([start])
    result = []
    
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Test
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
```

### 🏔️ Depth-First Search (DFS): The Deep Explorer

#### 📖 The Concept
Explore **as far as possible** along each branch before backtracking. Like exploring a maze by always taking the first unexplored path.

#### 🎯 When to Use
- **Cycle detection** in graphs
- **Topological sorting** for DAGs
- **Connected components** in undirected graphs
- **Path finding** with backtracking

#### 📊 Visual DFS Traversal
```
Starting from A:

Path: A → B → D (dead end, backtrack)
      A → B → E → F → C (complete)

Order: A → B → D → E → F → C
```

#### 🐍 Implementation
```python
def dfs_recursive(graph: Dict[str, List[str]], start: str, visited: Set[str] = None) -> List[str]:
    """🏔️ DFS Recursive - O(V + E) time, O(V) space"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

def dfs_iterative(graph: Dict[str, List[str]], start: str) -> List[str]:
    """🏔️ DFS Iterative - O(V + E) time, O(V) space"""
    visited: Set[str] = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            # Add neighbors in reverse order for consistent traversal
            stack.extend(reversed(graph[vertex]))
    
    return result
```

---

## 🛣️ 3. Shortest Path Algorithms

### ⚡ Dijkstra's Algorithm: The Optimal Route Finder

#### 📖 The Concept
Find **shortest path** from source to all other vertices in a **weighted graph** (no negative weights).

#### 🎯 When to Use
- **GPS navigation** systems
- **Network routing** protocols
- **Social network** analysis (shortest connection path)
- **Game AI** pathfinding

#### 📊 Visual Dijkstra Example
```
Weighted Graph:
    A --2-- B --1-- D
    |       |       |
    4       3       2
    |       |       |
    C --1-- E --1-- F

Shortest paths from A:
A → B: 2
A → C: 4  
A → D: 3 (via B)
A → E: 5 (via B)
A → F: 5 (via B → D)
```

#### 🐍 Implementation
```python
import heapq
from typing import Dict, Tuple

def dijkstra(graph: Dict[str, List[Tuple[str, int]]], start: str) -> Dict[str, int]:
    """⚡ Dijkstra's Algorithm - O((V + E) log V) time"""
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, vertex)
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Test with weighted graph
weighted_graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 1), ('E', 3)],
    'C': [('A', 4), ('E', 1)],
    'D': [('B', 1), ('F', 2)],
    'E': [('B', 3), ('C', 1), ('F', 1)],
    'F': [('D', 2), ('E', 1)]
}
print(dijkstra(weighted_graph, 'A'))
```

---

## 📋 4. Topological Sort: The Task Scheduler

### 📖 The Concept
Linear ordering of vertices where for every directed edge u→v, u comes before v. Essential for **task scheduling**.

### 🎯 When to Use
- **Build systems** (compile dependencies)
- **Course prerequisites** scheduling
- **Data pipeline** task ordering (Airflow DAGs)
- **Package dependency** resolution

### 📊 Visual Topological Sort
```
DAG (Directed Acyclic Graph):
    A → B → D
    ↓   ↓   ↓
    C → E → F

Possible topological orders:
1. A → C → B → E → D → F
2. A → B → C → D → E → F
3. A → B → C → E → D → F
```

### 🐍 Implementation
```python
def topological_sort_dfs(graph: Dict[str, List[str]]) -> List[str]:
    """📋 Topological Sort using DFS - O(V + E) time"""
    visited = set()
    stack = []
    
    def dfs_helper(vertex: str):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs_helper(neighbor)
        stack.append(vertex)
    
    # Visit all vertices
    for vertex in graph:
        if vertex not in visited:
            dfs_helper(vertex)
    
    return stack[::-1]  # Reverse to get correct order

def topological_sort_kahn(graph: Dict[str, List[str]]) -> List[str]:
    """📋 Kahn's Algorithm - O(V + E) time"""
    # Calculate in-degrees
    in_degree = {vertex: 0 for vertex in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
    
    # Find vertices with no incoming edges
    queue = deque([vertex for vertex in in_degree if in_degree[vertex] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(graph) else []  # Empty if cycle exists
```

---

## 📈 5. Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Use Case |
|:----------|:---------------:|:----------------:|:---------|
| **BFS** | O(V + E) | O(V) | Shortest path (unweighted) |
| **DFS** | O(V + E) | O(V) | Cycle detection, topological sort |
| **Dijkstra** | O((V + E) log V) | O(V) | Shortest path (weighted, no negative) |
| **Topological Sort** | O(V + E) | O(V) | Task scheduling, dependencies |

---

## 🎯 6. The Engineer's Choice

### 🌊 **Use BFS when:**
- 🎯 **Shortest path** in unweighted graphs
- 🔍 **Level-order** exploration needed
- 🌐 **Social network** analysis (degrees of separation)
- 🧩 **Puzzle solving** (minimum moves)

### 🏔️ **Use DFS when:**
- 🔄 **Cycle detection** required
- 📋 **Topological sorting** needed
- 🌳 **Tree/graph** structure analysis
- 🔙 **Backtracking** algorithms

### ⚡ **Use Dijkstra when:**
- 🗺️ **GPS navigation** systems
- 🌐 **Network routing** optimization
- 💰 **Cost optimization** problems
- 🎮 **Game pathfinding** with weights

---

## 🌟 7. Advanced Graph Concepts

### 🔍 Cycle Detection
```python
def has_cycle_undirected(graph: Dict[str, List[str]]) -> bool:
    """Detect cycle in undirected graph using DFS"""
    visited = set()
    
    def dfs(vertex: str, parent: str) -> bool:
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False
```

### 🌐 Connected Components
```python
def connected_components(graph: Dict[str, List[str]]) -> List[List[str]]:
    """Find all connected components"""
    visited = set()
    components = []
    
    def dfs(vertex: str, component: List[str]):
        visited.add(vertex)
        component.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor, component)
    
    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs(vertex, component)
            components.append(component)
    
    return components
```

---

## 🧪 8. Real-World Applications

### 🌐 **Industry Usage:**
- 📱 **Social Networks** - Friend recommendations, influence analysis
- 🗺️ **Navigation Systems** - Route optimization, traffic analysis
- 🔍 **Search Engines** - PageRank algorithm, web crawling
- 💰 **Financial Systems** - Fraud detection, risk analysis
- 🏭 **Supply Chain** - Logistics optimization, dependency tracking
- 🧬 **Bioinformatics** - Protein interaction networks, phylogenetic trees

---

## 🚀 Next Adventure

> **"From network navigation to dynamic optimization"**

You've mastered the art of **navigating complex networks** and **finding optimal paths**. But what about problems where we need to make a sequence of optimal decisions? How do we break down complex problems into simpler subproblems?

**Coming Next:** 💎 **Dynamic Programming** - The Art of Optimal Substructure

---

*Happy Coding! 🎉*