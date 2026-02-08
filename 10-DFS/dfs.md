# 🌲 Pattern 8: Tree DFS (Depth-First Search)

## 🎯 **Welcome to Deep Exploration**

> 💡 **Mental Model:** DFS explores trees **branch by branch**, like a spelunker diving deep into cave tunnels before exploring adjacent passages.

---

## 🏔️ **The Mountain Climbing Analogy**

### 🎭 **The Concept**
Imagine climbing a mountain with multiple paths. DFS is like choosing one path and following it to the peak before trying another:

```
         🏔️ Root (Start)
        /  \
       ⛰️  ⛰️  Branches
      / \  / \
     🎯 🎯 🎯 🎯  Leaves (Goals)
```

**DFS Process:**
1. Start at Root
2. Pick a branch (left or right)
3. Go as DEEP as possible
4. Backtrack when you hit a dead end
5. Try the next unexplored branch

### 🔄 **DFS vs BFS**
| Aspect | DFS (Depth-First) | BFS (Breadth-First) |
|--------|-------------------|---------------------|
| **Exploration** | Branch by branch | Level by level |
| **Data Structure** | Stack (LIFO) or Recursion | Queue (FIFO) |
| **Use Case** | Complete exploration, path finding | Shortest path |
| **Space** | O(height) | O(width) |
| **Memory** | More efficient for deep trees | More efficient for wide trees |

---

## 🎯 **The Essential Tool: Stack (or Recursion)**

### 📦 **Why Stack?**
**DFS = Stack** (LIFO: Last In, First Out) or **Recursion** (uses call stack)

```python
Stack Operations:
┌─────────────────────────┐
│  Top → [C, B, A] ← Bottom │
└─────────────────────────┘
     ↑           ↑
   Pop        Push
  (Remove)    (Add)
```

**Key Insight:** Stack ensures we explore the most recently discovered path first (go deep!).

---

## 🎬 **Three DFS Traversal Orders**

### 📝 **The Three Flavors**

DFS has **three different orders** depending on when we process the node:

```
Tree Example:
      1
     / \
    2   3
   / \
  4   5
```

#### 1️⃣ **Preorder (Root → Left → Right)**
```python
Process: 1 → 2 → 4 → 5 → 3
Order: Root FIRST, then children
Use: Copy tree, serialize tree
```

#### 2️⃣ **Inorder (Left → Root → Right)**
```python
Process: 4 → 2 → 5 → 1 → 3
Order: Left child, Root, Right child
Use: BST sorted order
```

#### 3️⃣ **Postorder (Left → Right → Root)**
```python
Process: 4 → 5 → 2 → 3 → 1
Order: Children FIRST, then root
Use: Delete tree, calculate tree properties
```

---

## 🔧 **The Algorithm**

### 📋 **Step-by-Step Process (Recursive)**
1. **Base Case:** If node is null, return
2. **Process Node:** Handle current node (preorder)
3. **Recurse Left:** Explore left subtree
4. **Process Node:** Handle current node (inorder)
5. **Recurse Right:** Explore right subtree
6. **Process Node:** Handle current node (postorder)

### 📋 **Step-by-Step Process (Iterative)**
1. **Initialize:** Create stack, push root
2. **Loop:** While stack is not empty
3. **Pop:** Remove top node
4. **Process:** Handle current node
5. **Push Children:** Add right, then left (LIFO!)
6. **Repeat:** Continue until stack empty

---

## 🎬 **Visual Walkthrough**

### 🌳 **Example Tree**
```
    1
   / \
  2   3
 /
4
```

### 📊 **Preorder Execution Trace (Recursive)**
```python
# Call Stack Visualization
preorder(1):
  Process: 1 → Result: [1]
  Call preorder(2):
    Process: 2 → Result: [1, 2]
    Call preorder(4):
      Process: 4 → Result: [1, 2, 4]
      Call preorder(None): return
      Call preorder(None): return
    Call preorder(None): return
  Call preorder(3):
    Process: 3 → Result: [1, 2, 4, 3]
    Call preorder(None): return
    Call preorder(None): return

Final Result: [1, 2, 4, 3]
```

### 📊 **Preorder Execution Trace (Iterative)**
```python
# Initial State
Stack: [1]
Result: []

# Step 1: Process 1
Pop: 1
Process: 1 → Result: [1]
Push right (3), then left (2)
Stack: [2, 3]

# Step 2: Process 2 (top of stack)
Pop: 2
Process: 2 → Result: [1, 2]
Push left (4)
Stack: [3, 4]

# Step 3: Process 4 (top of stack)
Pop: 4
Process: 4 → Result: [1, 2, 4]
No children
Stack: [3]

# Step 4: Process 3
Pop: 3
Process: 3 → Result: [1, 2, 4, 3]
No children
Stack: []

# Stack empty - Done!
Final Result: [1, 2, 4, 3]
```

---

## 💻 **Core Implementation**

### 🔨 **Preorder Traversal (Recursive)**
```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Preorder: Root → Left → Right
    Time: O(N) | Space: O(H) where H is height
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        result.append(node.val)  # Process root FIRST
        dfs(node.left)           # Then left
        dfs(node.right)          # Then right
    
    dfs(root)
    return result
```

### 🔨 **Preorder Traversal (Iterative)**
```python
def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Preorder using explicit stack
    Time: O(N) | Space: O(H)
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()  # LIFO: Remove from top
        result.append(node.val)
        
        # Push right first (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
```

### 🔨 **Inorder Traversal (Recursive)**
```python
def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder: Left → Root → Right
    Time: O(N) | Space: O(H)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)           # Left first
        result.append(node.val)  # Then root
        dfs(node.right)          # Then right
    
    dfs(root)
    return result
```

### 🔨 **Inorder Traversal (Iterative)**
```python
def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder using explicit stack
    Time: O(N) | Space: O(H)
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left
        
        # Process node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result
```

### 🔨 **Postorder Traversal (Recursive)**
```python
def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Postorder: Left → Right → Root
    Time: O(N) | Space: O(H)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)           # Left first
        dfs(node.right)          # Then right
        result.append(node.val)  # Then root LAST
    
    dfs(root)
    return result
```

### 🔨 **Postorder Traversal (Iterative)**
```python
def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Postorder using two stacks
    Time: O(N) | Space: O(H)
    """
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        # Push left first, then right
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    # Reverse to get postorder
    result = []
    while stack2:
        result.append(stack2.pop().val)
    
    return result
```

---

## 🎯 **DFS Variations & Problems**

### 📊 **Problem 1: Maximum Depth**
```python
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Find the longest path from root to leaf
    DFS is natural for this!
    """
    if not root:
        return 0
    
    # Recursive: depth = 1 + max(left_depth, right_depth)
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return 1 + max(left_depth, right_depth)
```

### 📊 **Problem 2: Path Sum**
```python
def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """
    Check if there's a root-to-leaf path with given sum
    """
    if not root:
        return False
    
    # Leaf node - check if remaining sum equals node value
    if not root.left and not root.right:
        return root.val == target
    
    # Recurse with reduced target
    remaining = target - root.val
    return (has_path_sum(root.left, remaining) or 
            has_path_sum(root.right, remaining))
```

### 📊 **Problem 3: All Root-to-Leaf Paths**
```python
def all_paths(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Find all root-to-leaf paths
    """
    result = []
    
    def dfs(node, path):
        if not node:
            return
        
        # Add current node to path
        path.append(node.val)
        
        # Leaf node - save path
        if not node.left and not node.right:
            result.append(path[:])  # Copy path
        else:
            # Continue exploring
            dfs(node.left, path)
            dfs(node.right, path)
        
        # Backtrack
        path.pop()
    
    dfs(root, [])
    return result
```

### 📊 **Problem 4: Diameter of Binary Tree**
```python
def diameter(root: Optional[TreeNode]) -> int:
    """
    Find longest path between any two nodes
    Path may or may not pass through root
    """
    max_diameter = 0
    
    def height(node):
        nonlocal max_diameter
        
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Update diameter (path through this node)
        max_diameter = max(max_diameter, left_height + right_height)
        
        # Return height
        return 1 + max(left_height, right_height)
    
    height(root)
    return max_diameter
```

### 📊 **Problem 5: Validate Binary Search Tree**
```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Check if tree is a valid BST
    Use inorder traversal - should be sorted!
    """
    def inorder(node, min_val, max_val):
        if not node:
            return True
        
        # Check BST property
        if node.val <= min_val or node.val >= max_val:
            return False
        
        # Check left and right subtrees
        return (inorder(node.left, min_val, node.val) and
                inorder(node.right, node.val, max_val))
    
    return inorder(root, float('-inf'), float('inf'))
```

### 📊 **Problem 6: Lowest Common Ancestor**
```python
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor of two nodes
    """
    if not root or root == p or root == q:
        return root
    
    # Search in left and right subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    # If both found in different subtrees, current node is LCA
    if left and right:
        return root
    
    # Return whichever is not None
    return left if left else right
```

### 📊 **Problem 7: Serialize and Deserialize Tree**
```python
def serialize(root: Optional[TreeNode]) -> str:
    """
    Serialize tree to string using preorder
    """
    result = []
    
    def dfs(node):
        if not node:
            result.append("null")
            return
        
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return ",".join(result)

def deserialize(data: str) -> Optional[TreeNode]:
    """
    Deserialize string to tree
    """
    values = iter(data.split(","))
    
    def dfs():
        val = next(values)
        if val == "null":
            return None
        
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    
    return dfs()
```

---

## 🌍 **Real-World Application: File System**

### 🎯 **Why DFS for File Systems?**

**Perfect Match:** File systems are hierarchical - DFS naturally explores directories!

```python
# Example: Directory Structure
/home
├── user
│   ├── documents
│   │   ├── file1.txt
│   │   └── file2.txt
│   └── downloads
│       └── file3.txt
└── shared
    └── file4.txt

# DFS explores:
/home → /home/user → /home/user/documents → file1.txt → file2.txt
     → /home/user/downloads → file3.txt
     → /home/shared → file4.txt

# Complete exploration of each branch before moving to next!
```

**Why DFS over BFS?**
- **Memory efficient:** Only stores current path (not all siblings)
- **Natural recursion:** Matches directory structure
- **Complete exploration:** Processes entire subdirectory before moving on

---

## 📝 **Drill Questions with Answers**

### ❓ **Question 1: Call Stack Trace**

**Tree:**
```
      A
     / \
    B   C
   /
  D
```

**Question:** Trace the call stack for preorder traversal.

**Answer:**
```python
# Call Stack (grows downward)
preorder(A):
  print(A) → Output: [A]
  ├─ preorder(B):
  │    print(B) → Output: [A, B]
  │    ├─ preorder(D):
  │    │    print(D) → Output: [A, B, D]
  │    │    ├─ preorder(None): return
  │    │    └─ preorder(None): return
  │    └─ preorder(None): return
  └─ preorder(C):
       print(C) → Output: [A, B, D, C]
       ├─ preorder(None): return
       └─ preorder(None): return

Final Output: [A, B, D, C]
```

### ❓ **Question 2: When to Use Each Traversal?**

**Answer:**

```python
traversal_use_cases = {
    "Preorder (Root → Left → Right)": [
        "✅ Copy/clone a tree",
        "✅ Serialize a tree",
        "✅ Prefix expression evaluation",
        "✅ Create a tree from traversal"
    ],
    
    "Inorder (Left → Root → Right)": [
        "✅ Get sorted order from BST",
        "✅ Validate BST",
        "✅ Find kth smallest in BST",
        "✅ Infix expression evaluation"
    ],
    
    "Postorder (Left → Right → Root)": [
        "✅ Delete/free a tree",
        "✅ Calculate tree properties (height, size)",
        "✅ Postfix expression evaluation",
        "✅ Bottom-up processing"
    ]
}
```

### ❓ **Question 3: Space Complexity Comparison**

**Answer:**

```python
# Consider these trees:

# Skewed Tree (Worst for DFS):
#     1
#      \
#       2
#        \
#         3
#          \
#           4
# DFS Space: O(N) - call stack depth = N
# BFS Space: O(1) - queue width = 1

# Complete Binary Tree (Worst for BFS):
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
# DFS Space: O(log N) - call stack depth = height
# BFS Space: O(N/2) = O(N) - queue width at last level

# Conclusion:
# - DFS better for wide, shallow trees
# - BFS better for deep, narrow trees
# - Average case: both O(N) worst case
```

### ❓ **Question 4: Recursive vs Iterative**

**Answer:**

```python
comparison = {
    "Recursive DFS": {
        "Pros": [
            "✅ Cleaner, more readable code",
            "✅ Natural for tree problems",
            "✅ Easy to implement"
        ],
        "Cons": [
            "❌ Stack overflow for very deep trees",
            "❌ Hidden space complexity (call stack)",
            "❌ Harder to debug"
        ]
    },
    
    "Iterative DFS": {
        "Pros": [
            "✅ No stack overflow risk",
            "✅ Explicit control over stack",
            "✅ Easier to debug"
        ],
        "Cons": [
            "❌ More complex code",
            "❌ Harder to implement (especially inorder)",
            "❌ Less intuitive"
        ]
    }
}

# Recommendation:
# - Use RECURSIVE for interviews (cleaner)
# - Use ITERATIVE for production (safer)
```

---

## 🏆 **LeetCode Problems**

### 🟢 **Easy**
1. **Binary Tree Preorder Traversal (LC-144)** - Classic DFS
2. **Binary Tree Inorder Traversal (LC-94)** - BST sorted order
3. **Binary Tree Postorder Traversal (LC-145)** - Bottom-up
4. **Maximum Depth (LC-104)** - Simple recursion
5. **Same Tree (LC-100)** - Compare two trees
6. **Invert Binary Tree (LC-226)** - Swap children
7. **Path Sum (LC-112)** - Root-to-leaf path

### 🟡 **Medium**
8. **Validate BST (LC-98)** - Inorder traversal
9. **Binary Tree Level Order (LC-102)** - Can use DFS with levels
10. **Path Sum II (LC-113)** - All root-to-leaf paths
11. **Lowest Common Ancestor (LC-236)** - Classic DFS
12. **Binary Tree Right Side View (LC-199)** - Rightmost nodes
13. **Diameter of Binary Tree (LC-543)** - Longest path
14. **Serialize and Deserialize (LC-297)** - Tree encoding

### 🔴 **Hard**
15. **Binary Tree Maximum Path Sum (LC-124)** - Any path
16. **Recover BST (LC-99)** - Fix swapped nodes
17. **Binary Tree Cameras (LC-968)** - Greedy + DFS

---

## 🎯 **Key Takeaways**

### ✅ **Core Concepts**
- **DFS explores branch by branch** using stack or recursion
- **Three traversal orders:** Preorder, Inorder, Postorder
- **Stack (LIFO)** or **Recursion** (call stack) is essential
- **Optimal for complete exploration** and path problems

### 📊 **Complexity Analysis**
```python
complexity_guide = {
    "Time Complexity": "O(N) - visit each node once",
    "Space Complexity": "O(H) - height of tree",
    "Best Case Space": "O(log N) - balanced tree",
    "Worst Case Space": "O(N) - skewed tree",
    "Call Stack Depth": "O(H) - recursion depth"
}
```

### 💡 **DFS Templates**

#### **Recursive Template**
```python
def dfs_recursive(root):
    def dfs(node):
        if not node:
            return
        
        # Preorder: process here
        dfs(node.left)
        # Inorder: process here
        dfs(node.right)
        # Postorder: process here
    
    dfs(root)
```

#### **Iterative Template (Preorder)**
```python
def dfs_iterative(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        # Process node
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### 🎯 **When to Use DFS**
✅ **Use DFS when:**
- Exploring all paths
- Finding specific paths (root-to-leaf)
- Tree property calculations (height, diameter)
- Backtracking problems
- Memory is limited (narrow trees)

❌ **Don't use DFS when:**
- Finding shortest path (use BFS)
- Level-by-level processing needed (use BFS)
- Tree is extremely deep (stack overflow risk)

### 🔑 **Traversal Order Cheat Sheet**
```python
# Remember the order:
Preorder:  Root → Left → Right  (Process root FIRST)
Inorder:   Left → Root → Right  (Process root MIDDLE)
Postorder: Left → Right → Root  (Process root LAST)

# Mnemonic:
# PRE-order:  PRE-process root
# IN-order:   Root IN the middle
# POST-order: POST-process root
```

---

## 🎓 **Advanced Concepts**

### 🧠 **Morris Traversal (O(1) Space)**
```python
def morris_inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder traversal with O(1) space using threading
    """
    result = []
    current = root
    
    while current:
        if not current.left:
            # No left child, process and go right
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                # Create thread
                predecessor.right = current
                current = current.left
            else:
                # Remove thread
                predecessor.right = None
                result.append(current.val)
                current = current.right
    
    return result
```

### 🧠 **Backtracking with DFS**
```python
def find_all_paths_with_sum(root: Optional[TreeNode], target: int) -> List[List[int]]:
    """
    Find all root-to-leaf paths with given sum
    Classic backtracking with DFS
    """
    result = []
    
    def backtrack(node, path, remaining):
        if not node:
            return
        
        # Add current node
        path.append(node.val)
        remaining -= node.val
        
        # Check if leaf and sum matches
        if not node.left and not node.right and remaining == 0:
            result.append(path[:])  # Save copy
        
        # Explore children
        backtrack(node.left, path, remaining)
        backtrack(node.right, path, remaining)
        
        # Backtrack: remove current node
        path.pop()
    
    backtrack(root, [], target)
    return result
```

---

*Master DFS, explore every branch with confidence! 🌲*
