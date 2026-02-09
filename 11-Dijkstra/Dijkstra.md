# 🗺️ Pattern 9: Dijkstra's Algorithm (Shortest Path)

## 🎯 **Welcome to Graph Shortest Path**

> 💡 **Mental Model:** Dijkstra's algorithm finds the **shortest path** from a source to all other nodes in a weighted graph, like finding the fastest route on a GPS map.

---

## 🚗 **The GPS Navigation Analogy**

### 🎭 **The Concept**
Imagine using GPS to find the shortest route from your home to various destinations:

```
        Home (Start)
       /  |  \
     5km 3km 10km
     /    |    \
   Park  Mall  Beach
    |     |      |
   2km   4km    1km
    |     |      |
  School Work  Cafe
```

**Dijkstra's Process:**
1. Start at Home (distance = 0)
2. Explore nearest unvisited neighbor (Mall, 3km)
3. Update distances to neighbors through Mall
4. Pick next nearest unvisited node
5. Repeat until all nodes visited
6. Always choose the **closest unvisited node**

### 🔄 **Dijkstra vs BFS vs DFS**
| Aspect | Dijkstra | BFS | DFS |
|--------|----------|-----|-----|
| **Graph Type** | Weighted | Unweighted | Any |
| **Finds** | Shortest path (weighted) | Shortest path (unweighted) | Any path |
| **Data Structure** | Min-Heap (Priority Queue) | Queue (FIFO) | Stack (LIFO) |
| **Greedy** | Yes | No | No |
| **Time Complexity** | O(E log V) | O(V + E) | O(V + E) |
| **Use Case** | GPS, Network routing | Level traversal | Complete exploration |

---

## 🎯 **The Essential Tool: Priority Queue (Min-Heap)**

### 📦 **Why Priority Queue?**
**Dijkstra = Min-Heap** (Always get the node with minimum distance)

```python
Priority Queue (Min-Heap):
┌─────────────────────────────┐
│  Top → (A, 0) ← Minimum     │
│        (B, 5)               │
│        (C, 8)               │
│        (D, 12) ← Maximum    │
└─────────────────────────────┘
     ↑           ↑
   Pop        Push
  (Min)    (Any value)
```

**Key Insight:** Priority queue ensures we always process the closest unvisited node first (greedy choice).

---

## 🎬 **The Algorithm**

### 📋 **Step-by-Step Process**
1. **Initialize:** 
   - Set distance to source = 0
   - Set distance to all other nodes = ∞
   - Add source to priority queue
2. **Loop:** While priority queue is not empty
3. **Extract Min:** Get node with minimum distance
4. **Skip if Visited:** If already processed, skip
5. **Mark Visited:** Mark current node as visited
6. **Relax Edges:** For each neighbor:
   - Calculate new distance = current distance + edge weight
   - If new distance < old distance, update and add to queue
7. **Repeat:** Continue until queue is empty

### 🔑 **The Relaxation Concept**
```python
# Edge Relaxation
Current node: A (distance = 5)
Neighbor: B (current distance = 10)
Edge weight: A → B = 2

New distance = 5 + 2 = 7
If 7 < 10:
    Update B's distance to 7
    Add (B, 7) to priority queue
```

---

## 🎬 **Visual Walkthrough**

### 🌐 **Example Graph**
```
Graph (weighted):
      A
    /   \
   4     2
  /       \
 B----3----C
  \       /
   5     1
    \   /
      D

Edges:
A → B: 4
A → C: 2
B → C: 3
B → D: 5
C → D: 1
```

### 📊 **Execution Trace (Source = A)**

```python
# Initial State
Distances: {A: 0, B: ∞, C: ∞, D: ∞}
Priority Queue: [(0, A)]
Visited: {}

# Step 1: Process A (distance = 0)
Pop: (0, A)
Mark A as visited
Relax edges from A:
  - A → B (4): 0 + 4 = 4 < ∞ → Update B to 4
  - A → C (2): 0 + 2 = 2 < ∞ → Update C to 2

Distances: {A: 0, B: 4, C: 2, D: ∞}
Priority Queue: [(2, C), (4, B)]
Visited: {A}

# Step 2: Process C (distance = 2)
Pop: (2, C)
Mark C as visited
Relax edges from C:
  - C → B (3): 2 + 3 = 5 > 4 → No update
  - C → D (1): 2 + 1 = 3 < ∞ → Update D to 3

Distances: {A: 0, B: 4, C: 2, D: 3}
Priority Queue: [(3, D), (4, B)]
Visited: {A, C}

# Step 3: Process D (distance = 3)
Pop: (3, D)
Mark D as visited
Relax edges from D:
  - D → B (5): 3 + 5 = 8 > 4 → No update

Distances: {A: 0, B: 4, C: 2, D: 3}
Priority Queue: [(4, B)]
Visited: {A, C, D}

# Step 4: Process B (distance = 4)
Pop: (4, B)
Mark B as visited
No unvisited neighbors

Distances: {A: 0, B: 4, C: 2, D: 3}
Priority Queue: []
Visited: {A, B, C, D}

# Final Result
Shortest distances from A:
A → A: 0
A → B: 4 (path: A → B)
A → C: 2 (path: A → C)
A → D: 3 (path: A → C → D)
```

---

## 💻 **Core Implementation**

### 🔨 **Basic Dijkstra's Algorithm**
```python
import heapq
from typing import Dict, List, Tuple
from collections import defaultdict

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, int]:
    """
    Dijkstra's Algorithm for shortest path
    
    Args:
        graph: Adjacency list {node: [(neighbor, weight), ...]}
        source: Starting node
    
    Returns:
        Dictionary of shortest distances from source
    
    Time: O(E log V) | Space: O(V)
    """
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    # Priority queue: (distance, node)
    pq = [(0, source)]
    visited = set()
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # Skip if already visited
        if current_node in visited:
            continue
        
        # Mark as visited
        visited.add(current_node)
        
        # Relax edges
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            # If found shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

### 🔨 **Dijkstra with Path Reconstruction**
```python
def dijkstra_with_path(graph: Dict[int, List[Tuple[int, int]]], 
                       source: int, 
                       target: int) -> Tuple[int, List[int]]:
    """
    Dijkstra's Algorithm with path reconstruction
    
    Returns:
        (shortest_distance, path)
    
    Time: O(E log V) | Space: O(V)
    """
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    # Track parent for path reconstruction
    parent = {source: None}
    
    pq = [(0, source)]
    visited = set()
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Early termination if target found
        if current_node == target:
            break
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    
    return distances[target], path
```

### 🔨 **Dijkstra for Grid (2D Array)**
```python
def dijkstra_grid(grid: List[List[int]], 
                  start: Tuple[int, int], 
                  end: Tuple[int, int]) -> int:
    """
    Dijkstra's Algorithm for 2D grid
    Each cell has a cost/weight
    
    Time: O(N*M log(N*M)) | Space: O(N*M)
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    # Initialize distances
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = grid[start[0]][start[1]]
    
    # Priority queue: (distance, row, col)
    pq = [(grid[start[0]][start[1]], start[0], start[1])]
    
    while pq:
        current_dist, row, col = heapq.heappop(pq)
        
        # Reached target
        if (row, col) == end:
            return current_dist
        
        # Skip if we've found a better path already
        if current_dist > distances[row][col]:
            continue
        
        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                distance = current_dist + grid[new_row][new_col]
                
                # If found shorter path
                if distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = distance
                    heapq.heappush(pq, (distance, new_row, new_col))
    
    return distances[end[0]][end[1]]
```

---

## 🎯 **Dijkstra Variations & Problems**

### 📊 **Problem 1: Network Delay Time**
```python
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    LeetCode 743: Network Delay Time
    Find time for signal to reach all nodes
    
    times[i] = [source, target, time]
    k = starting node
    """
    # Build graph
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Dijkstra
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0
    
    pq = [(0, k)]
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if current_dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # Get maximum distance
    max_dist = max(distances.values())
    return max_dist if max_dist != float('inf') else -1
```

### 📊 **Problem 2: Path with Minimum Effort**
```python
def minimum_effort_path(heights: List[List[int]]) -> int:
    """
    LeetCode 1631: Path with Minimum Effort
    Find path where maximum absolute difference is minimized
    """
    rows, cols = len(heights), len(heights[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Track minimum effort to reach each cell
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0
    
    # Priority queue: (effort, row, col)
    pq = [(0, 0, 0)]
    
    while pq:
        current_effort, row, col = heapq.heappop(pq)
        
        # Reached destination
        if row == rows - 1 and col == cols - 1:
            return current_effort
        
        # Skip if we've found better path
        if current_effort > efforts[row][col]:
            continue
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Effort is max difference along path
                effort = max(current_effort, 
                           abs(heights[new_row][new_col] - heights[row][col]))
                
                if effort < efforts[new_row][new_col]:
                    efforts[new_row][new_col] = effort
                    heapq.heappush(pq, (effort, new_row, new_col))
    
    return 0
```

### 📊 **Problem 3: Cheapest Flights Within K Stops**
```python
def find_cheapest_price(n: int, 
                       flights: List[List[int]], 
                       src: int, 
                       dst: int, 
                       k: int) -> int:
    """
    LeetCode 787: Cheapest Flights Within K Stops
    Modified Dijkstra with stop constraint
    """
    # Build graph
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))
    
    # Priority queue: (cost, node, stops)
    pq = [(0, src, 0)]
    
    # Track minimum cost to reach node with given stops
    visited = {}
    
    while pq:
        cost, node, stops = heapq.heappop(pq)
        
        # Reached destination
        if node == dst:
            return cost
        
        # Skip if too many stops
        if stops > k:
            continue
        
        # Skip if we've visited with fewer stops and lower cost
        if node in visited and visited[node] <= stops:
            continue
        
        visited[node] = stops
        
        # Explore neighbors
        for neighbor, price in graph[node]:
            heapq.heappush(pq, (cost + price, neighbor, stops + 1))
    
    return -1
```

### 📊 **Problem 4: Swim in Rising Water**
```python
def swim_in_water(grid: List[List[int]]) -> int:
    """
    LeetCode 778: Swim in Rising Water
    Find minimum time to reach bottom-right
    """
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue: (time, row, col)
    pq = [(grid[0][0], 0, 0)]
    visited = set()
    
    while pq:
        time, row, col = heapq.heappop(pq)
        
        # Reached destination
        if row == n - 1 and col == n - 1:
            return time
        
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 0 <= new_col < n and 
                (new_row, new_col) not in visited):
                # Time is max elevation along path
                new_time = max(time, grid[new_row][new_col])
                heapq.heappush(pq, (new_time, new_row, new_col))
    
    return -1
```

### 📊 **Problem 5: Path with Maximum Probability**
```python
def max_probability(n: int, 
                   edges: List[List[int]], 
                   succ_prob: List[float], 
                   start: int, 
                   end: int) -> float:
    """
    LeetCode 1514: Path with Maximum Probability
    Modified Dijkstra for maximum instead of minimum
    """
    # Build graph
    graph = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        prob = succ_prob[i]
        graph[u].append((v, prob))
        graph[v].append((u, prob))
    
    # Max-heap: use negative probabilities
    pq = [(-1.0, start)]
    probabilities = [0.0] * n
    probabilities[start] = 1.0
    
    while pq:
        current_prob, node = heapq.heappop(pq)
        current_prob = -current_prob
        
        if node == end:
            return current_prob
        
        if current_prob < probabilities[node]:
            continue
        
        for neighbor, edge_prob in graph[node]:
            new_prob = current_prob * edge_prob
            
            if new_prob > probabilities[neighbor]:
                probabilities[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))
    
    return 0.0
```

---

## 🌍 **Real-World Applications**

### 🎯 **Where Dijkstra Shines**

#### 1️⃣ **GPS Navigation Systems**
```python
# Google Maps, Waze, Apple Maps
- Nodes: Intersections
- Edges: Roads
- Weights: Travel time/distance
- Goal: Find fastest route
```

#### 2️⃣ **Network Routing (Internet)**
```python
# OSPF (Open Shortest Path First) Protocol
- Nodes: Routers
- Edges: Network connections
- Weights: Bandwidth, latency
- Goal: Optimize packet routing
```

#### 3️⃣ **Airline Route Planning**
```python
# Flight booking systems
- Nodes: Airports
- Edges: Flight routes
- Weights: Cost, time, distance
- Goal: Find cheapest/fastest route
```

#### 4️⃣ **Game Development**
```python
# NPC pathfinding
- Nodes: Grid cells/waypoints
- Edges: Valid moves
- Weights: Movement cost
- Goal: Find optimal path for AI
```

---

## 📝 **Drill Questions with Answers**

### ❓ **Question 1: Why Priority Queue?**

**Answer:**

```python
# Without Priority Queue (Wrong approach):
# Process nodes in random order
Queue: [A, B, C, D]
Process A (dist=10), then B (dist=5), then C (dist=3)
❌ Inefficient - might process far nodes before near ones

# With Priority Queue (Correct approach):
# Always process nearest unvisited node
Min-Heap: [(3, C), (5, B), (10, A)]
Process C (dist=3), then B (dist=5), then A (dist=10)
✅ Efficient - greedy choice guarantees optimal solution

# Why it works:
# Dijkstra's greedy property: Once a node is visited,
# we've found the shortest path to it.
# Priority queue ensures we visit nodes in order of distance.
```

### ❓ **Question 2: Can Dijkstra Handle Negative Weights?**

**Answer: NO! ❌**

```python
# Example where Dijkstra fails with negative weights:
Graph:
A --2--> B
|        |
5      -10
|        |
v        v
C --1--> D

# Dijkstra's result (WRONG):
A → B: 2 (path: A → B)
A → D: -8 (path: A → B → D)

# But actual shortest path:
A → D: -4 (path: A → C → D)

# Why it fails:
# Dijkstra marks B as visited with distance 2
# It never reconsiders B, even though A → C → D → B
# might give a shorter path with negative edges

# Solution: Use Bellman-Ford algorithm for negative weights
```

### ❓ **Question 3: Time Complexity Breakdown**

**Answer:**

```python
# Dijkstra's Time Complexity: O(E log V)

# Breakdown:
components = {
    "Initialization": "O(V) - set all distances to infinity",
    "Main Loop": "O(V) - visit each vertex once",
    "Heap Operations": {
        "Extract Min": "O(log V) - done V times → O(V log V)",
        "Decrease Key": "O(log V) - done E times → O(E log V)"
    },
    "Total": "O(V log V + E log V) = O(E log V)"
}

# Space Complexity: O(V)
space = {
    "Distances Array": "O(V)",
    "Priority Queue": "O(V) - at most V elements",
    "Visited Set": "O(V)",
    "Total": "O(V)"
}

# Note: E ≥ V-1 for connected graph, so O(E log V) dominates
```

### ❓ **Question 4: Dijkstra vs Bellman-Ford vs Floyd-Warshall**

**Answer:**

```python
comparison = {
    "Dijkstra": {
        "Type": "Single-source shortest path",
        "Negative Weights": "❌ No",
        "Time": "O(E log V)",
        "Space": "O(V)",
        "Best For": "Sparse graphs, non-negative weights"
    },
    
    "Bellman-Ford": {
        "Type": "Single-source shortest path",
        "Negative Weights": "✅ Yes (detects negative cycles)",
        "Time": "O(V * E)",
        "Space": "O(V)",
        "Best For": "Graphs with negative weights"
    },
    
    "Floyd-Warshall": {
        "Type": "All-pairs shortest path",
        "Negative Weights": "✅ Yes (no negative cycles)",
        "Time": "O(V³)",
        "Space": "O(V²)",
        "Best For": "Dense graphs, all-pairs distances"
    }
}

# When to use which:
# - Dijkstra: GPS, network routing (non-negative weights)
# - Bellman-Ford: Currency arbitrage, negative weights
# - Floyd-Warshall: Small graphs, need all-pairs distances
```

---

## 🏆 **LeetCode Problems**

### 🟢 **Easy**
1. **Network Delay Time (LC-743)** - Classic Dijkstra
2. **Path with Maximum Probability (LC-1514)** - Max instead of min

### 🟡 **Medium**
3. **Path with Minimum Effort (LC-1631)** - 2D grid variant
4. **Cheapest Flights Within K Stops (LC-787)** - Constrained Dijkstra
5. **Swim in Rising Water (LC-778)** - Min-max path
6. **Find the City (LC-1334)** - Multiple source Dijkstra
7. **Minimum Cost to Reach Destination (LC-1928)** - Time-based
8. **Reachable Nodes (LC-882)** - Modified graph

### 🔴 **Hard**
9. **Minimum Cost to Make Valid Path (LC-1368)** - 0-1 BFS variant
10. **Shortest Path Visiting All Nodes (LC-847)** - State-space search

---

## 🎯 **Key Takeaways**

### ✅ **Core Concepts**
- **Dijkstra finds shortest path** in weighted graphs with non-negative weights
- **Greedy algorithm:** Always pick nearest unvisited node
- **Priority Queue (Min-Heap)** is essential for efficiency
- **Edge relaxation** updates distances when shorter path found

### 📊 **Complexity Analysis**
```python
complexity_guide = {
    "Time Complexity": "O(E log V) with binary heap",
    "Time (Fibonacci Heap)": "O(E + V log V) - theoretical best",
    "Space Complexity": "O(V) - distances + priority queue",
    "Best Case": "O(V log V) - no edges to relax",
    "Worst Case": "O(E log V) - dense graph"
}
```

### 💡 **Dijkstra Template**
```python
def dijkstra_template(graph, source):
    # Initialize
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    pq = [(0, source)]
    visited = set()
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        # Skip if visited
        if node in visited:
            continue
        
        visited.add(node)
        
        # Relax edges
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

### 🎯 **When to Use Dijkstra**
✅ **Use Dijkstra when:**
- Finding shortest path in weighted graph
- All edge weights are non-negative
- Single-source shortest path needed
- Graph is sparse (E ≈ V)

❌ **Don't use Dijkstra when:**
- Graph has negative weights (use Bellman-Ford)
- Need all-pairs shortest paths (use Floyd-Warshall)
- Unweighted graph (use BFS - simpler and faster)
- Graph has negative cycles (no solution exists)

### 🔑 **Common Pitfalls**
```python
pitfalls = {
    "1. Forgetting visited check": {
        "Problem": "Process same node multiple times",
        "Solution": "Use visited set or check current_dist > distances[node]"
    },
    
    "2. Wrong heap order": {
        "Problem": "Using max-heap instead of min-heap",
        "Solution": "Use heapq (min-heap) or negate values for max-heap"
    },
    
    "3. Not handling disconnected nodes": {
        "Problem": "Some nodes unreachable",
        "Solution": "Check if distance == infinity before using"
    },
    
    "4. Incorrect edge relaxation": {
        "Problem": "Update distance incorrectly",
        "Solution": "new_dist = current_dist + edge_weight"
    }
}
```

---

## 🎓 **Advanced Concepts**

### 🧠 **Bidirectional Dijkstra**
```python
def bidirectional_dijkstra(graph, source, target):
    """
    Run Dijkstra from both source and target
    Meet in the middle for faster search
    
    Time: O(E log V) but faster in practice
    """
    # Forward search from source
    forward_dist = {source: 0}
    forward_pq = [(0, source)]
    forward_visited = set()
    
    # Backward search from target
    backward_dist = {target: 0}
    backward_pq = [(0, target)]
    backward_visited = set()
    
    best_distance = float('inf')
    
    while forward_pq or backward_pq:
        # Forward step
        if forward_pq:
            dist, node = heapq.heappop(forward_pq)
            if node in forward_visited:
                continue
            forward_visited.add(node)
            
            # Check if paths meet
            if node in backward_visited:
                best_distance = min(best_distance, 
                                  forward_dist[node] + backward_dist[node])
            
            # Relax edges...
        
        # Backward step
        if backward_pq:
            dist, node = heapq.heappop(backward_pq)
            if node in backward_visited:
                continue
            backward_visited.add(node)
            
            # Check if paths meet
            if node in forward_visited:
                best_distance = min(best_distance, 
                                  forward_dist[node] + backward_dist[node])
            
            # Relax edges...
    
    return best_distance
```

### 🧠 **A* Algorithm (Dijkstra + Heuristic)**
```python
def a_star(graph, source, target, heuristic):
    """
    A* = Dijkstra + Heuristic function
    Faster for finding path to specific target
    
    Priority: f(n) = g(n) + h(n)
    g(n) = actual distance from source
    h(n) = heuristic estimate to target
    """
    # Priority queue: (f_score, g_score, node)
    pq = [(heuristic(source, target), 0, source)]
    g_scores = {source: 0}
    visited = set()
    
    while pq:
        f_score, g_score, node = heapq.heappop(pq)
        
        if node == target:
            return g_score
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            tentative_g = g_score + weight
            
            if tentative_g < g_scores.get(neighbor, float('inf')):
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, target)
                heapq.heappush(pq, (f_score, tentative_g, neighbor))
    
    return float('inf')

# Example heuristic for grid (Manhattan distance)
def manhattan_distance(node, target):
    return abs(node[0] - target[0]) + abs(node[1] - target[1])
```

---

## 🔬 **Proof of Correctness**

### 📐 **Why Dijkstra Works**

```python
"""
Theorem: Dijkstra's algorithm finds the shortest path 
         from source to all nodes in a graph with 
         non-negative edge weights.

Proof (by induction):

Base Case:
- Initially, distance to source = 0 (correct)
- Distance to all others = ∞

Inductive Hypothesis:
- Assume all visited nodes have correct shortest distances

Inductive Step:
- Pick unvisited node u with minimum distance d
- Claim: d is the shortest distance to u

Proof by contradiction:
- Suppose there's a shorter path to u with distance d' < d
- This path must go through some unvisited node v
- Distance to v ≥ d (since u has minimum distance)
- Path through v: distance(v) + edge(v,u) ≥ d
- But all edges are non-negative, so:
  d' = distance(v) + edge(v,u) ≥ d
- Contradiction! (d' < d but d' ≥ d)
- Therefore, d is the shortest distance to u

Conclusion:
- Greedy choice (pick nearest unvisited node) is optimal
- Algorithm correctly computes shortest paths
"""
```

---

*Master Dijkstra, navigate graphs with precision! 🗺️*