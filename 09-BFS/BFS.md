# 🌊 Pattern 7: Tree BFS (Breadth-First Search)

## 🎯 **Welcome to Trees and Graphs**

> 💡 **Mental Model:** BFS explores trees **level by level**, like water ripples spreading from a center point.

---

## 🌊 **The Water Ripple Analogy**

### 🎭 **The Concept**
Imagine dropping a stone in water. The ripples spread outward in circles:

```
        🪨 Root (Level 0)
       /  \
      ⭕  ⭕  Level 1
     / \  / \
    ⭕ ⭕ ⭕ ⭕  Level 2
```

**BFS Process:**
1. Touch the Root (Level 0)
2. Touch ALL nodes at Level 1 (Children)
3. Touch ALL nodes at Level 2 (Grandchildren)
4. Continue level by level...

### 🔄 **BFS vs DFS**
| Aspect | BFS (Breadth-First) | DFS (Depth-First) |
|--------|---------------------|-------------------|
| **Exploration** | Level by level | Branch by branch |
| **Data Structure** | Queue (FIFO) | Stack (LIFO) |
| **Use Case** | Shortest path | Complete exploration |
| **Space** | O(width) | O(height) |

---

## 🎯 **The Essential Tool: Queue**

### 📦 **Why Queue?**
**BFS = Queue** (FIFO: First In, First Out)

```python
Queue Operations:
┌─────────────────────────┐
│  Front → [A, B, C] ← Back │
└─────────────────────────┘
     ↑           ↑
  Dequeue    Enqueue
  (Remove)    (Add)
```

**Key Insight:** Queue ensures we visit older nodes (higher levels) before newer nodes (lower levels).

---

## 🎬 **Problem: Level Order Traversal**

### 📝 **Problem Statement**
Given a binary tree, return a list of values separated by levels.

### 🌳 **Example**
```
Input Tree:
      1
     / \
    2   3
   / \   \
  4   5   6

Output: [[1], [2, 3], [4, 5, 6]]
```

---

## 🔧 **The Algorithm**

### 📋 **Step-by-Step Process**
1. **Initialize:** Create queue, add root
2. **Loop:** While queue is not empty
3. **Level Snapshot:** Capture current level size
4. **Process Level:** For each node in current level:
   - Dequeue node from front
   - Process node value
   - Enqueue children to back
5. **Repeat:** Move to next level

---

## 🎬 **Visual Walkthrough**

### 🌳 **Example Tree**
```
    1
   / \
  7   9
```

### 📊 **Execution Trace**
```python
# Initial State
Queue: [1]
Result: []

# Level 0 Processing
Level size: 1
Process node 1:
  - Dequeue: 1
  - Add to result: [[1]]
  - Enqueue children: 7, 9
Queue: [7, 9]
Result: [[1]]

# Level 1 Processing
Level size: 2
Process node 7:
  - Dequeue: 7
  - Add to current level: [7]
  - No children
Queue: [9]

Process node 9:
  - Dequeue: 9
  - Add to current level: [7, 9]
  - No children
Queue: []
Result: [[1], [7, 9]]

# Queue empty - Done!
Final Result: [[1], [7, 9]]
```

---

## 💻 **Core Implementation**

### 🔨 **Basic Level Order Traversal**
```python
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    BFS Level Order Traversal
    Time: O(N) | Space: O(W) where W is max width
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # 🔑 Key: Freeze current level size
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()  # FIFO: Remove from front
            current_level.append(node.val)
            
            # Add children to back
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

---

## 🎯 **BFS Variations**

### 📊 **Problem 1: Reverse Level Order**
```python
def reverse_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Return levels from bottom to top
    Input: [[1], [2, 3], [4, 5, 6]]
    Output: [[4, 5, 6], [2, 3], [1]]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result[::-1]  # Reverse the result
```

### 📊 **Problem 2: Zigzag Level Order**
```python
def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Alternate direction for each level
    Level 0: Left to Right
    Level 1: Right to Left
    Level 2: Left to Right...
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse if going right to left
        if not left_to_right:
            current_level.reverse()
        
        result.append(current_level)
        left_to_right = not left_to_right
    
    return result
```

### 📊 **Problem 3: Minimum Depth**
```python
def min_depth(root: Optional[TreeNode]) -> int:
    """
    Find shortest path from root to any leaf
    BFS is OPTIMAL for this!
    """
    if not root:
        return 0
    
    queue = deque([(root, 1)])  # (node, depth)
    
    while queue:
        node, depth = queue.popleft()
        
        # Found first leaf - this is minimum depth!
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0
```

### 📊 **Problem 4: Maximum Depth**
```python
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Find longest path from root to any leaf
    """
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        level_size = len(queue)
        depth += 1
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth
```

### 📊 **Problem 5: Level Averages**
```python
def level_averages(root: Optional[TreeNode]) -> List[float]:
    """
    Calculate average value for each level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_sum = 0
        
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_sum / level_size)
    
    return result
```

---

## 🌍 **Real-World Application: Shortest Path**

### 🎯 **Why BFS for Shortest Path?**

**Guarantee:** BFS finds the shortest path in unweighted graphs!

```python
# Example: City Network
     A (Start)
    / \
   B   C
  /     \
 D       E (Target)

BFS explores:
Level 0: A
Level 1: B, C
Level 2: D, E ← Found target at level 2!

Shortest path: A → C → E (2 hops)
```

**Why not DFS?**
- DFS might explore A → B → D first (deep dive)
- Then backtrack to find A → C → E
- No guarantee of finding shortest path first

---

## 📝 **Drill Questions with Answers**

### ❓ **Question 1: Queue State Trace**

**Tree:**
```
      A
     / \
    B   C
     \
      D
```

**Answer:**
```python
# Initial
Start: [A]

# After processing A
Dequeue A, Enqueue B and C
After processing A: [B, C]

# After processing B
Dequeue B, Enqueue D (B's right child)
After processing B: [C, D]

# After processing C
Dequeue C, no children
After processing C: [D]

# After processing D
Dequeue D, no children
After processing D: []

# Complete trace:
Start: [A]
After A: [B, C]
After B: [C, D]
After C: [D]
After D: []
```

### ❓ **Question 2: Minimum Depth - BFS vs DFS**

**Answer: Use BFS!**

**Reasoning:**
```python
# Consider this tree:
        Root
       /    \
      A      B (Leaf!)
     /
    C
   /
  D
 /
E (Leaf)

# BFS explores level by level:
Level 0: Root
Level 1: A, B ← Found leaf B! Minimum depth = 2
# Stops immediately, no need to explore deeper

# DFS would explore:
Root → A → C → D → E (depth 5)
Then backtrack to find B (depth 2)
# Wastes time exploring deep branches

# Conclusion: BFS is OPTIMAL for minimum depth
# Time: O(N) worst case, but often much faster
# DFS: Always O(N) - must explore all paths
```

### ❓ **Question 3: Space Complexity**

**Answer: B) O(N)**

**Explanation:**
```python
# Worst case: Complete binary tree
# Last level contains ~N/2 nodes

# Example:
        1           Level 0: 1 node
       / \
      2   3         Level 1: 2 nodes
     / \ / \
    4  5 6  7       Level 2: 4 nodes

# When processing level 1, queue contains level 2
# Queue size = 4 nodes = N/2 (where N=7)
# Space Complexity: O(N)

# More precisely: O(W) where W is maximum width
# For complete binary tree: W ≈ N/2 = O(N)
```

---

## 🏆 **LeetCode Problems**

### 🟢 **Easy**
1. **Binary Tree Level Order Traversal (LC-102)** - Classic BFS
2. **Average of Levels (LC-637)** - Level aggregation
3. **Minimum Depth (LC-111)** - Shortest path
4. **Maximum Depth (LC-104)** - Can use BFS or DFS

### 🟡 **Medium**
5. **Binary Tree Zigzag (LC-103)** - Alternating direction
6. **Binary Tree Right Side View (LC-199)** - Last node per level
7. **Level Order Bottom (LC-107)** - Reverse traversal
8. **Populating Next Right Pointers (LC-116)** - Level linking

---

## 🎯 **Key Takeaways**

### ✅ **Core Concepts**
- **BFS explores level by level** using a queue
- **Queue (FIFO)** is essential for BFS
- **Level size snapshot** is the key technique
- **Optimal for shortest path** in unweighted graphs

### 📊 **Complexity Analysis**
```python
complexity_guide = {
    "Time Complexity": "O(N) - visit each node once",
    "Space Complexity": "O(W) - max width of tree",
    "Worst Case Space": "O(N) - complete binary tree",
    "Best Case Space": "O(1) - skewed tree"
}
```

### 💡 **BFS Template**
```python
def bfs_template(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # 🔑 Freeze level size
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            # Add children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

### 🎯 **When to Use BFS**
✅ **Use BFS when:**
- Finding shortest path
- Level-by-level processing
- Finding minimum depth
- Exploring neighbors first

❌ **Don't use BFS when:**
- Need to explore all paths (use DFS)
- Memory is very limited (DFS uses less space)
- Tree is very wide (BFS queue grows large)

---

*Master BFS, conquer trees level by level! 🌊*