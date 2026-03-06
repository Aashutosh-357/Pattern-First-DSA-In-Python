# 🕸️ Graphs: The Network Navigator

![Graph Algorithms](https://img.shields.io/badge/Topic-Graph_Algorithms-darkgreen?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Advanced-red?style=for-the-badge)
![Time](https://img.shields.io/badge/Study_Time-6_Hours-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-3_Non--Linear_DS-blueviolet?style=for-the-badge)

> **"The Web of Connections"**
>
> In the digital age, everything is connected. Social networks, recommendation engines, GPS navigation, task scheduling — they all rely on graphs. A graph is not just dots and lines; it's a mathematical model of **relationships** that powers the modern world.

Welcome to the world of **network intelligence** — where connections reveal insights.

---

## 📚 Table of Contents

| # | Topic | Difficulty |
|:--|:------|:----------:|
| 1 | [The Blueprint — What is a Graph?](#1-the-blueprint--what-is-a-graph) | 🟢 Beginner |
| 2 | [Graph Representations](#2-graph-representations) | 🟢 Beginner |
| 3 | [BFS — The Level Explorer](#3-bfs--the-level-explorer) | 🟡 Intermediate |
| 4 | [DFS — The Deep Explorer](#4-dfs--the-deep-explorer) | 🟡 Intermediate |
| 5 | [Cycle Detection](#5-cycle-detection) | 🟡 Intermediate |
| 6 | [Topological Sort — The Task Scheduler](#6-topological-sort--the-task-scheduler) | 🔴 Advanced |
| 7 | [Dijkstra's Algorithm — The Route Finder](#7-dijkstras-algorithm--the-route-finder) | 🔴 Advanced |
| 8 | [Union-Find (DSU) — The Group Detector](#8-union-find-dsu--the-group-detector) | 🔴 Advanced |
| 9 | [Bipartite Graph Detection](#9-bipartite-graph-detection) | 🔴 Advanced |
| 10 | [Complexity Cheat Sheet](#10-complexity-cheat-sheet) | — |
| 11 | [Decision Flowchart — Which Algorithm?](#11-decision-flowchart--which-algorithm) | — |
| 12 | [LeetCode Practice Problems](#12-leetcode-practice-problems) | — |
| 13 | [Real-World Applications](#13-real-world-applications) | — |

---

## 1. The Blueprint — What is a Graph?

### 🌐 The Analogy

Think of a **city map**:
- **Vertices (Nodes)** → Cities or intersections
- **Edges** → Roads connecting cities
- **Weighted Edges** → Roads with travel times/distances
- **Directed Edges** → One-way streets

### 🗂️ Types of Graphs

```
GRAPH TAXONOMY
══════════════════════════════════════════════════════════

  UNDIRECTED                   DIRECTED (Digraph)
  ─────────────                ───────────────────
  A ─── B                      A ──► B
  │     │                      │     │
  C ─── D                      ▼     ▼
                               C ──► D
  Edges have NO direction.     Edges have a direction.
  (Facebook friendships)       (Twitter follows, Airflow DAGs)

  WEIGHTED                     DAG (Directed Acyclic Graph)
  ─────────────                ────────────────────────────
  A ─5─ B                      A ──► B ──► D
  │     │                      │
  3     2                      ▼
  │     │                      C ──► E
  C ─1─ D
                               No cycles allowed.
  Edges have costs/weights.    (Course prerequisites, pipelines)
  (GPS, network routing)

══════════════════════════════════════════════════════════
```

### 📐 Key Terminology

| Term | Meaning | Real-World Example |
|:-----|:--------|:-------------------|
| **Vertex / Node** | A point in the graph | A city, user, task |
| **Edge** | A connection between two vertices | A road, friendship, dependency |
| **Degree** | Number of edges connected to a node | Number of friends |
| **In-degree** | Edges pointing *into* a node (digraph) | Twitter followers |
| **Out-degree** | Edges pointing *out of* a node (digraph) | Accounts you follow |
| **Path** | A sequence of vertices connected by edges | A route on a map |
| **Cycle** | A path that starts and ends at the same vertex | A circular dependency |
| **DAG** | Directed Acyclic Graph (no cycles) | Airflow task pipeline |
| **Connected** | Every vertex is reachable from every other | All cities are connected |

---

## 2. Graph Representations

Two main ways to store a graph in memory. Your choice impacts space and time.

### 📋 2.1 Adjacency List (Most Common ✅)

```python
from collections import defaultdict
from typing import Dict, List

# Undirected Graph: A-B, A-C, B-D, B-E, C-F, E-F
graph: Dict[str, List[str]] = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

```
Visual:
    A ──── B ──── D
    │      │
    │      │
    C ──── F ──── E
```

### 📊 2.2 Adjacency Matrix

```python
# For a graph with 4 vertices: 0, 1, 2, 3
# matrix[i][j] = 1 means there is an edge from i → j

#       0  1  2  3
matrix = [
    #0 [  0, 1, 1, 0 ],
    #1 [  1, 0, 0, 1 ],
    #2 [  1, 0, 0, 1 ],
    #3 [  0, 1, 1, 0 ]
]

# For weighted graphs, replace 1 with the actual weight.
# matrix[i][j] = 0 or float('inf') means no edge.
```

### ⚖️ 2.3 Comparison: Which to Use?

| Feature | Adjacency List | Adjacency Matrix |
|:--------|:--------------:|:----------------:|
| **Space** | O(V + E) ✅ | O(V²) ❌ |
| **Check edge (u,v) exists?** | O(degree) | O(1) ✅ |
| **List all neighbors of u?** | O(degree) ✅ | O(V) |
| **Best when** | Sparse graphs (few edges) | Dense graphs / edge lookup |
| **Used in practice** | Most interview problems ✅ | Grid problems, Floyd-Warshall |

> 💡 **Rule of thumb:** If the graph has far fewer edges than V², use an **Adjacency List**. For dense graphs or when you constantly need to check `edge(u,v)` in O(1), use an **Adjacency Matrix**.

---

## 3. BFS — The Level Explorer

### 💡 The Core Idea

Explore **all neighbors at the current level** before going deeper.
Think of it like a **rock thrown into a pond** — ripples spread outward ring by ring.

```
MENTAL MODEL:

   🟡                ← Level 0: Start (A)
  / \
🔵   🔵              ← Level 1: Direct neighbors (B, C)
/ \   \
🟢 🟢  🟢            ← Level 2: Their neighbors (D, E, F)

BFS processes one entire "ring" before moving to the next.
```

### 📊 Step-by-Step Dry Run

```
Graph:  A → [B, C]
        B → [A, D, E]
        C → [A, F]

Start: A

Step 1: Queue = [A],        Visited = {A},          Result = []
Step 2: Pop A  → Queue = [B, C],  Visited = {A,B,C}, Result = [A]
Step 3: Pop B  → Queue = [C, D, E], Visited = {A,B,C,D,E}, Result = [A,B]
Step 4: Pop C  → Queue = [D, E, F], Visited = {...,F}, Result = [A,B,C]
Step 5: Pop D  → Queue = [E, F],  Result = [A,B,C,D]
Step 6: Pop E  → Queue = [F],     Result = [A,B,C,D,E]  (F already visited)
Step 7: Pop F  → Queue = [],      Result = [A,B,C,D,E,F]

Final: A → B → C → D → E → F
```

### 🐍 Implementation

```python
from collections import deque
from typing import Dict, List, Set

def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """🌊 BFS Traversal — O(V + E) time, O(V) space"""
    visited: Set[str] = {start}
    queue: deque = deque([start])
    result: List[str] = []

    while queue:
        vertex = queue.popleft()          # Always popleft for BFS (FIFO)
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

# ── Test ──────────────────────────────────────────
graph = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'],
    'C': ['A', 'F'], 'D': ['B'],
    'E': ['B', 'F'], 'F': ['C', 'E']
}
print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
```

### 🎯 BFS for Shortest Path (Unweighted)

The most **critical** BFS application — finding the shortest path in an unweighted graph.

```python
def bfs_shortest_path(
    graph: Dict[str, List[str]], start: str, end: str
) -> List[str]:
    """Find shortest path from start to end using BFS."""
    if start == end:
        return [start]

    visited: Set[str] = {start}
    # Store the full path to each node, not just the node
    queue: deque = deque([[start]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]                 # Last node in the current path

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == end:
                    return new_path       # 🎯 Found! Return immediately
                visited.add(neighbor)
                queue.append(new_path)

    return []                             # No path found

# ── Test ──────────────────────────────────────────
print(bfs_shortest_path(graph, 'A', 'F'))  # ['A', 'C', 'F']
```

### 🎯 When to Use BFS

| Scenario | Why BFS? |
|:---------|:---------|
| Shortest path in **unweighted** graph | Explores level by level → guarantees minimum edges |
| Social network **degrees of separation** | Level 1 = friends, Level 2 = friends-of-friends |
| **Puzzle solving** (minimum moves) | E.g., Word Ladder, Rubik's cube states |
| Finding all nodes within **k distance** | Natural level-based exploration |

---

## 4. DFS — The Deep Explorer

### 💡 The Core Idea

Explore **as far as possible** down one path before backtracking.
Think of it like **solving a maze** — keep going straight until you hit a dead end, then backtrack.

```
MENTAL MODEL:

    A
    │
    B ─── D (dead end, backtrack ↩)
    │
    E
    │
    F ─── C

DFS drills deep down one branch completely before trying the next.
```

### 📊 Step-by-Step Dry Run

```
Graph: A → [B, C],  B → [D, E],  E → [F],  C → [F]

DFS from A (recursive trace):

visit(A)
  visit(B)               ← first neighbor of A
    visit(D) → dead end, backtrack
    visit(E)
      visit(F)
        C already visited? No → visit(C) → done
  B complete
A complete

Order: A → B → D → E → F → C
```

### 🐍 Implementation

```python
from typing import Dict, List, Set, Optional

def dfs_recursive(
    graph: Dict[str, List[str]],
    start: str,
    visited: Optional[Set[str]] = None
) -> List[str]:
    """🏔️ DFS Recursive — O(V + E) time, O(V) space (call stack)"""
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


def dfs_iterative(graph: Dict[str, List[str]], start: str) -> List[str]:
    """🏔️ DFS Iterative — O(V + E) time, O(V) space (explicit stack)"""
    visited: Set[str] = set()
    stack: List[str] = [start]
    result: List[str] = []

    while stack:
        vertex = stack.pop()              # Always pop from end for DFS (LIFO)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            # Add neighbors in reverse to maintain left-to-right traversal order
            stack.extend(reversed(graph[vertex]))

    return result

# ── Test ──────────────────────────────────────────
graph = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'],
    'C': ['A', 'F'], 'D': ['B'],
    'E': ['B', 'F'], 'F': ['C', 'E']
}
print(dfs_recursive(graph, 'A'))   # ['A', 'B', 'D', 'E', 'F', 'C']
print(dfs_iterative(graph, 'A'))   # ['A', 'B', 'D', 'E', 'F', 'C']
```

### 🔢 Connected Components (Using DFS)

```python
def connected_components(graph: Dict[str, List[str]]) -> List[List[str]]:
    """Find all disconnected islands in an undirected graph."""
    visited: Set[str] = set()
    components: List[List[str]] = []

    def dfs(vertex: str, component: List[str]) -> None:
        visited.add(vertex)
        component.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for vertex in graph:
        if vertex not in visited:
            component: List[str] = []
            dfs(vertex, component)
            components.append(component)

    return components

# ── Test ──────────────────────────────────────────
disconnected = {
    'A': ['B'], 'B': ['A'],           # Island 1
    'C': ['D'], 'D': ['C'],           # Island 2
    'E': []                            # Island 3 (lone node)
}
print(connected_components(disconnected))
# [['A', 'B'], ['C', 'D'], ['E']]
```

### 🎯 When to Use DFS

| Scenario | Why DFS? |
|:---------|:---------|
| **Cycle detection** | Backtracking reveals revisited nodes |
| **Topological sort** | Post-order DFS gives reverse topo order |
| **Connected components** | Natural island detection |
| **Path finding with backtracking** | E.g., can we reach node X? |
| **Tree structure problems** | DFS mirrors recursive tree traversal |

---

## 5. Cycle Detection

### 💡 The Core Idea

A **cycle** exists when you can start at a node and follow edges to come back to the same node.

```
UNDIRECTED GRAPH           DIRECTED GRAPH (Digraph)
────────────────           ─────────────────────────
  A ─── B                    A ──► B
  │     │                    │     │
  └─ C ─┘                    ▲     ▼
                              └──── C
  Cycle: A → B → C → A      Cycle: A → B → C → A
  (revisit via different    (must follow arrow direction!)
   neighbor, not parent)
```

### 🐍 5.1 Undirected Graph — Cycle Detection

```python
def has_cycle_undirected(graph: Dict[str, List[str]]) -> bool:
    """Detect cycle in undirected graph.
    Key: track 'parent' to avoid false positives from back-edges."""
    visited: Set[str] = set()

    def dfs(vertex: str, parent: Optional[str]) -> bool:
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:          # ← real cycle, not just the edge we came from
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False

# ── Test ──────────────────────────────────────────
cyclic = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
acyclic = {'A': ['B'], 'B': ['C'], 'C': []}

print(has_cycle_undirected(cyclic))    # True
print(has_cycle_undirected(acyclic))   # False
```

### 🐍 5.2 Directed Graph — Cycle Detection (with Recursion Stack)

```python
def has_cycle_directed(graph: Dict[str, List[str]]) -> bool:
    """Detect cycle in a directed graph.
    Key: use a 'recursion stack' to track current DFS path."""
    visited: Set[str] = set()
    rec_stack: Set[str] = set()           # nodes in current DFS path

    def dfs(vertex: str) -> bool:
        visited.add(vertex)
        rec_stack.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:   # ← back-edge = cycle in digraph
                return True

        rec_stack.discard(vertex)         # Remove when backtracking
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False

# ── Test ──────────────────────────────────────────
directed_cyclic = {'A': ['B'], 'B': ['C'], 'C': ['A']}   # A→B→C→A
directed_acyclic = {'A': ['B'], 'B': ['C'], 'C': []}      # A→B→C

print(has_cycle_directed(directed_cyclic))    # True
print(has_cycle_directed(directed_acyclic))   # False
```

> ⚠️ **Key Difference:** In an undirected graph, we track `parent` to skip the edge we came from. In a directed graph, we track the **recursion stack** (current path) because a back-edge in a directed graph always means a cycle.

---

## 6. Topological Sort — The Task Scheduler

### 💡 The Core Idea

A **linear ordering** of vertices in a **DAG** (Directed Acyclic Graph) such that for every directed edge `u → v`, vertex `u` comes **before** `v` in the ordering.

```
REAL-WORLD ANALOGY: Course Prerequisites

  Math101 ──► Calculus ──► Physics
                 │
                 ▼
              Statistics ──► ML

Topological order: Math101 → Calculus → Statistics → Physics → ML

You CANNOT take Calculus before Math101.
Topological sort gives us a valid study schedule.
```

### 📊 Step-by-Step Dry Run (Kahn's Algorithm)

```
Graph: A→B, A→C, B→D, C→D, D→E

Step 1: Calculate in-degrees
        A=0, B=1, C=1, D=2, E=1

Step 2: Add zero in-degree nodes to queue
        Queue = [A]

Step 3: Process A → reduce neighbors' in-degrees
        B: 1→0  (add to queue)
        C: 1→0  (add to queue)
        Queue = [B, C],  Result = [A]

Step 4: Process B → D: 2→1
        Queue = [C],     Result = [A, B]

Step 5: Process C → D: 1→0 (add to queue)
        Queue = [D],     Result = [A, B, C]

Step 6: Process D → E: 1→0 (add to queue)
        Queue = [E],     Result = [A, B, C, D]

Step 7: Process E → done
        Result = [A, B, C, D, E]  ✅
```

### 🐍 Implementation

```python
from collections import deque
from typing import Dict, List

def topological_sort_kahn(graph: Dict[str, List[str]]) -> List[str]:
    """📋 Kahn's Algorithm (BFS-based) — O(V + E) time.
    Bonus: If result length < V, a cycle exists."""
    in_degree: Dict[str, int] = {vertex: 0 for vertex in graph}

    # Count incoming edges for each vertex
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    # Start with all vertices that have no dependencies
    queue: deque = deque([v for v in in_degree if in_degree[v] == 0])
    result: List[str] = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If not all vertices processed → cycle exists
    return result if len(result) == len(graph) else []


def topological_sort_dfs(graph: Dict[str, List[str]]) -> List[str]:
    """📋 DFS-based Topological Sort — O(V + E) time.
    Post-order DFS: push to stack AFTER all children are processed."""
    visited: Set[str] = set()
    stack: List[str] = []

    def dfs(vertex: str) -> None:
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)              # Push AFTER all descendants

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]                    # Reverse for correct order

# ── Test ──────────────────────────────────────────
dag = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}
print(topological_sort_kahn(dag))   # ['A', 'B', 'C', 'D', 'E'] or similar
print(topological_sort_dfs(dag))    # ['A', 'C', 'B', 'D', 'E'] or similar
```

> 💡 **Kahn's vs DFS Topo Sort:**
> - **Kahn's** is BFS-based and detects cycles naturally (output shorter than V → cycle exists).
> - **DFS** is more concise but harder to debug. Prefer **Kahn's** in interviews.

### 🎯 When to Use Topological Sort

| Scenario | Example |
|:---------|:--------|
| **Build systems** | Compile `A.py` before `B.py` that imports it |
| **Course scheduling** | Which courses must come before others |
| **Data pipeline** (Airflow / Dagster) | Task A must finish before Task B starts |
| **Package dependency** resolution | `npm install`, `pip install` |

---

## 7. Dijkstra's Algorithm — The Route Finder

### 💡 The Core Idea

Find the **shortest (lowest-cost) path** from one source vertex to all others in a **weighted graph with no negative edges**.

```
ANALOGY: GPS Navigation

  Home ──5── Work
  │           │
  3           2
  │           │
  Gym ──1── Shop

Dijkstra explores the "cheapest path so far" at every step,
guaranteed to find the globally shortest path.
```

### 📊 Step-by-Step Dry Run

```
Weighted Graph:
  A --2-- B --1-- D
  |       |       |
  4       3       2
  |       |       |
  C --1-- E --1-- F

Start: A

         dist[A]=0, dist[B]=∞, dist[C]=∞, dist[D]=∞, dist[E]=∞, dist[F]=∞
PQ = [(0,A)]

Pop (0,A):  relax B → dist[B]=2, relax C → dist[C]=4
PQ = [(2,B), (4,C)]

Pop (2,B):  relax D → dist[D]=3, relax E → dist[E]=5
PQ = [(3,D), (4,C), (5,E)]

Pop (3,D):  relax F → dist[F]=5
PQ = [(4,C), (5,E), (5,F)]

Pop (4,C):  relax E → dist[E]=5 (no improvement, skip)
Pop (5,E):  relax F → dist[F]=5 (no improvement, skip)
Pop (5,F):  done

Result: A→0, B→2, C→4, D→3, E→5, F→5
```

### 🐍 Implementation

```python
import heapq
from typing import Dict, List, Tuple

def dijkstra(
    graph: Dict[str, List[Tuple[str, int]]],
    start: str
) -> Dict[str, int]:
    """⚡ Dijkstra's Algorithm — O((V + E) log V) time, O(V) space.
    graph format: {vertex: [(neighbor, weight), ...]}"""
    distances: Dict[str, int] = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    min_heap: List[Tuple[int, str]] = [(0, start)]  # (cost, vertex)

    while min_heap:
        current_dist, current_vertex = heapq.heappop(min_heap)

        # Skip if we already found a shorter path
        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return distances

# ── Test ──────────────────────────────────────────
weighted_graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 1), ('E', 3)],
    'C': [('A', 4), ('E', 1)],
    'D': [('B', 1), ('F', 2)],
    'E': [('B', 3), ('C', 1), ('F', 1)],
    'F': [('D', 2), ('E', 1)]
}
print(dijkstra(weighted_graph, 'A'))
# {'A': 0, 'B': 2, 'C': 4, 'D': 3, 'E': 5, 'F': 5}
```

### 🎯 When to Use Dijkstra

| Scenario | Example |
|:---------|:--------|
| **GPS navigation** | Shortest driving route |
| **Network routing** (OSPF) | Least-cost packet routing |
| **Game AI pathfinding** | Enemy reaches player via cheapest path |
| **Social graph** analysis | Minimum connections between users |

> ⚠️ **Limitation:** Dijkstra fails with **negative edge weights**. Use **Bellman-Ford** for that case.

---

## 8. Union-Find (DSU) — The Group Detector

### 💡 The Core Idea

**Union-Find** (Disjoint Set Union) is a specialized data structure to efficiently answer: *"Are nodes X and Y in the same connected group?"*

```
ANALOGY: Social Clubs

  Initially: {A} {B} {C} {D} {E}   ← Everyone in their own club

  union(A, B) → {A, B} {C} {D} {E}
  union(C, D) → {A, B} {C, D} {E}
  union(A, C) → {A, B, C, D} {E}

  find(A) == find(D)? → YES (same club!)
  find(A) == find(E)? → NO  (different clubs!)
```

### 🐍 Implementation (with Path Compression + Union by Rank)

```python
class UnionFind:
    """⚡ Union-Find with path compression & union by rank.
    find: O(α(n)) ≈ O(1) amortized | union: O(α(n)) ≈ O(1)"""

    def __init__(self, n: int):
        self.parent: List[int] = list(range(n))  # Each node is its own parent
        self.rank: List[int] = [0] * n            # Used for balancing

    def find(self, x: int) -> int:
        """Find root with path compression (flatten the tree)."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Merge two sets. Returns False if already in same set (cycle!)."""
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False                              # Same group → cycle detected!

        # Attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if two nodes are in the same group."""
        return self.find(x) == self.find(y)

# ── Test: Count Connected Components ──────────────
edges = [(0,1), (1,2), (3,4)]     # 5 nodes, 3 edges
uf = UnionFind(5)
for u, v in edges:
    uf.union(u, v)

# Components: {0,1,2} and {3,4}
print(uf.connected(0, 2))    # True  (same component)
print(uf.connected(0, 3))    # False (different component)
```

### 🎯 When to Use Union-Find

| Scenario | Example |
|:---------|:--------|
| **Cycle detection** (undirected) | Adding edge u-v creates cycle if `find(u)==find(v)` |
| **Number of connected components** | Count how many disjoint groups exist |
| **Kruskal's MST** | Add edges greedily while avoiding cycles |
| **Dynamic connectivity** | Nodes being connected in real-time |

---

## 9. Bipartite Graph Detection

### 💡 The Core Idea

A graph is **bipartite** if its vertices can be split into two groups (say, Red 🔴 and Blue 🔵) such that **every edge connects a Red node to a Blue node** (no edge within the same color group).

```
BIPARTITE ✅                  NOT BIPARTITE ❌
────────────                  ─────────────────
🔴A ── 🔵B                    🔴A ── 🔵B
🔴C ── 🔵D                    │     /
🔴A ── 🔵D                    ▼   /
                              🔴C ── (odd cycle of length 3!)

ODD CYCLE = NOT BIPARTITE
```

**Real-World Use:** Bipartite graphs model matching problems — job applicants ↔ jobs, students ↔ courses.

### 🐍 Implementation (BFS-based 2-coloring)

```python
from collections import deque
from typing import Dict, List

def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    """Check if a graph is bipartite using BFS 2-coloring.
    Assign color 0 or 1 to each node. If a neighbor has the same color → not bipartite."""
    color: Dict[int, int] = {}

    for start in graph:
        if start in color:
            continue                          # Already processed

        queue: deque = deque([start])
        color[start] = 0                      # Color the starting node

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]  # Opposite color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:   # Same color → conflict!
                    return False

    return True

# ── Test ──────────────────────────────────────────
bipartite_graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
non_bipartite = {0: [1, 2], 1: [0, 2], 2: [0, 1]}   # Triangle (odd cycle)

print(is_bipartite(bipartite_graph))   # True
print(is_bipartite(non_bipartite))     # False
```

---

## 10. Complexity Cheat Sheet

| Algorithm | Time Complexity | Space Complexity | Notes |
|:----------|:---------------:|:----------------:|:------|
| **BFS** | O(V + E) | O(V) | Guaranteed shortest path (unweighted) |
| **DFS** | O(V + E) | O(V) | Call stack depth = O(V) recursive |
| **Cycle Detection (Undirected)** | O(V + E) | O(V) | Track parent node |
| **Cycle Detection (Directed)** | O(V + E) | O(V) | Track recursion stack |
| **Topological Sort (Kahn's)** | O(V + E) | O(V) | Also detects cycles |
| **Topological Sort (DFS)** | O(V + E) | O(V) | Post-order push |
| **Dijkstra (Min-Heap)** | O((V + E) log V) | O(V) | No negative weights |
| **Union-Find** | O(α(n)) ≈ O(1) | O(V) | Best for dynamic connectivity |
| **Bipartite Check** | O(V + E) | O(V) | 2-coloring via BFS/DFS |

> `V` = number of vertices, `E` = number of edges, `α` = inverse Ackermann function (near-constant)

---

## 11. Decision Flowchart — Which Algorithm?

```
                    ┌─────────────────────────────────┐
                    │   GRAPH PROBLEM — What do I do? │
                    └──────────────┬──────────────────┘
                                   │
              ┌─────────────────────────────────────────┐
              │          What is the goal?              │
              └──┬──────────┬──────────┬───────────────┘
                 │          │          │
     ┌───────────▼──┐  ┌────▼──────┐  ┌────▼───────────────┐
     │  Shortest    │  │  Ordering │  │  Grouping /        │
     │  Path        │  │  (Dependencies)│  Connectivity     │
     └──────┬───────┘  └────┬──────┘  └────────┬───────────┘
            │               │                   │
    ┌────────▼───────┐  Topological    ┌─────────▼──────────┐
    │  Unweighted?  │    Sort          │  Union-Find (DSU)  │
    └───┬───────────┘  (Kahn's / DFS) │  or BFS/DFS        │
        │                              └────────────────────┘
   YES  │   NO
        │   └──► Negative weights?
        │         YES → Bellman-Ford
        │         NO  → Dijkstra's
        │
       BFS (guarantees min edges)

───────────────────────────────────────────────────────
  QUICK REFERENCE CARD

  🌊 BFS            → Shortest path (unweighted), level traversal
  🏔️ DFS            → Cycle detect, connected components, topo sort
  ⚡ Dijkstra        → Shortest path (weighted, non-negative)
  📋 Topological    → Task scheduling, DAG ordering
  🔗 Union-Find     → Dynamic grouping, Kruskal's MST, cycle detect
  🎨 Bipartite      → 2-coloring, matching problems
───────────────────────────────────────────────────────
```

---

## 12. LeetCode Practice Problems

Work through these in order — each one is a direct application of one pattern above.

### 🌊 BFS Problems

| Problem | Difficulty | Key Pattern |
|:--------|:----------:|:------------|
| [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium | BFS/DFS flood fill |
| [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | 🟡 Medium | Multi-source BFS |
| [127. Word Ladder](https://leetcode.com/problems/word-ladder/) | 🔴 Hard | BFS shortest path |
| [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | 🟡 Medium | BFS on grid |

### 🏔️ DFS Problems

| Problem | Difficulty | Key Pattern |
|:--------|:----------:|:------------|
| [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium | DFS + HashMap |
| [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | 🟡 Medium | DFS flood fill |
| [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟡 Medium | Reverse DFS from two sources |

### 🔄 Cycle Detection Problems

| Problem | Difficulty | Key Pattern |
|:--------|:----------:|:------------|
| [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium | Directed cycle detection |
| [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 🟡 Medium | Union-Find cycle detection |

### 📋 Topological Sort Problems

| Problem | Difficulty | Key Pattern |
|:--------|:----------:|:------------|
| [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium | Topo sort / cycle detect |
| [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 Medium | Return topo order |
| [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | 🟡 Medium | Topo sort (leaf removal) |

### ⚡ Dijkstra / Weighted Path Problems

| Problem | Difficulty | Key Pattern |
|:--------|:----------:|:------------|
| [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium | Classic Dijkstra |
| [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | 🟡 Medium | Dijkstra on grid |
| [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium | BFS/Bellman-Ford variant |

### 🔗 Union-Find Problems

| Problem | Difficulty | Key Pattern |
|:--------|:----------:|:------------|
| [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | 🟡 Medium | DSU components |
| [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 🟡 Medium | DSU cycle detect |
| [1202. Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) | 🟡 Medium | DSU grouping |

---

## 13. Real-World Applications

```
INDUSTRY APPLICATIONS OF GRAPH ALGORITHMS
══════════════════════════════════════════════════════════════

  📱 Social Networks       🗺️ Navigation          🔍 Search Engines
  ─────────────────        ────────────          ──────────────────
  ▸ Friend recommend.      ▸ Dijkstra / A*       ▸ PageRank (BFS)
  ▸ Influence analysis     ▸ Traffic routing      ▸ Web crawling (BFS)
  ▸ Community detect.      ▸ ETA estimation       ▸ Link analysis

  🏭 Data Pipelines        💰 Finance             🧬 Bioinformatics
  ─────────────────        ──────────             ──────────────────
  ▸ Airflow DAG order      ▸ Fraud detect.        ▸ Protein networks
    (Topological Sort)     ▸ Transaction graph    ▸ Gene pathways
  ▸ Spark job scheduling   ▸ Risk propagation     ▸ Drug interactions

  🔧 DevOps / Build        🎮 Game Dev            📦 Package Managers
  ─────────────────        ───────────            ───────────────────
  ▸ Dependency graphs      ▸ AI pathfinding       ▸ npm / pip resolve
  ▸ CI/CD pipelines        ▸ World generation     ▸ Version conflicts
  ▸ Microservice mesh      ▸ NPC behavior         ▸ Circular deps

══════════════════════════════════════════════════════════════
```

---

## 🚀 Next Adventure

> **"From network navigation to dynamic optimization"**

You've mastered the art of **navigating complex networks**, **detecting cycles**, **ordering tasks**, and **finding optimal paths**. But what about problems where we need to make a **sequence of optimal decisions**, re-using previously computed results?

**Coming Next:** 💎 **Dynamic Programming** — The Art of Optimal Substructure

---

*Happy Coding! 🎉*