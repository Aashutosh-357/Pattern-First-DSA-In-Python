# ⏱️ Time & Space Complexity: The Complete Guide

## 🎯 **Welcome to Algorithm Analysis**

> 💡 **Mental Model:** Complexity analysis is like **predicting how your code will perform** as your data grows from 10 items to 10 million items.

---

## 🚀 **Why Complexity Matters**

### 🎭 **The Real-World Impact**

```python
# Scenario: Processing user data
users = 1,000,000  # 1 million users

# Algorithm A: O(N²) - Nested loops
time_A = 1,000,000² = 1,000,000,000,000 operations
# At 1 billion ops/sec: ~277 hours (11+ days!)

# Algorithm B: O(N log N) - Merge sort
time_B = 1,000,000 * log(1,000,000) ≈ 20,000,000 operations
# At 1 billion ops/sec: ~0.02 seconds

# Difference: 11 days vs 0.02 seconds! 🤯
```

**Key Insight:** The right algorithm can mean the difference between **instant response** and **waiting days**!

---

## 📊 **Big O Notation: The Language of Complexity**

### 🎯 **What is Big O?**

**Big O** describes how runtime or space grows as input size increases.

```python
# Think of Big O as:
"In the WORST case, as N grows large,
 how does my algorithm's performance scale?"
```

### 📈 **The Complexity Hierarchy (Best to Worst)**

```python
O(1)         < O(log N)    < O(N)        < O(N log N)  < 
O(N²)        < O(N³)       < O(2^N)      < O(N!)

Constant     Logarithmic   Linear        Linearithmic
Quadratic    Cubic         Exponential   Factorial

🚀 Fast                                   🐌 Slow
```

### 🎨 **Visual Comparison**

```
Operations vs Input Size (N)

1,000,000 |                                          O(N!)
          |                                    O(2^N)
          |                              O(N³)
          |                        O(N²)
  100,000 |                  O(N log N)
          |            O(N)
          |      O(log N)
   10,000 | O(1)
          |___________________________________________
            10    100   1,000  10,000  100,000    N

Notice: O(1) and O(log N) barely grow!
```

---

## 🔍 **Common Time Complexities Explained**

### 1️⃣ **O(1) - Constant Time**

**Definition:** Performance doesn't change with input size.

```python
def get_first_element(arr):
    """Always takes same time, regardless of array size"""
    return arr[0]  # O(1)

def hash_lookup(hash_map, key):
    """Dictionary lookup is O(1)"""
    return hash_map[key]  # O(1)

# Examples:
- Array access: arr[5]
- Dictionary get/set: dict[key]
- Math operations: a + b
- Variable assignment: x = 10
```

**Real-World Analogy:** Opening a book to page 1 - doesn't matter if book has 10 or 1000 pages!

---

### 2️⃣ **O(log N) - Logarithmic Time**

**Definition:** Cuts problem in half each step.

```python
def binary_search(arr, target):
    """Halves search space each iteration"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Eliminate left half
        else:
            right = mid - 1  # Eliminate right half
    
    return -1

# Time: O(log N)
# N = 1,000,000 → ~20 comparisons
# N = 1,000,000,000 → ~30 comparisons
```

**Real-World Analogy:** Finding a name in a phone book by opening to the middle, then middle of the half, etc.

**Examples:**
- Binary search
- Balanced BST operations
- Heap operations (insert, delete)
- Finding power: `x^n` using divide & conquer

---

### 3️⃣ **O(N) - Linear Time**

**Definition:** Performance grows directly with input size.

```python
def find_max(arr):
    """Must check every element once"""
    max_val = arr[0]
    
    for num in arr:  # O(N)
        if num > max_val:
            max_val = num
    
    return max_val

def sum_array(arr):
    """Visit each element exactly once"""
    total = 0
    for num in arr:  # O(N)
        total += num
    return total
```

**Real-World Analogy:** Reading every page in a book - twice as many pages = twice the time.

**Examples:**
- Array traversal
- Finding min/max
- Linear search
- Counting elements

---

### 4️⃣ **O(N log N) - Linearithmic Time**

**Definition:** Combination of linear and logarithmic.

```python
def merge_sort(arr):
    """Divide (log N) and merge (N) at each level"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # O(log N) levels
    right = merge_sort(arr[mid:])
    
    return merge(left, right)        # O(N) work per level

# Total: O(N log N)
```

**Real-World Analogy:** Organizing a deck of cards by repeatedly splitting and merging.

**Examples:**
- Merge sort
- Quick sort (average case)
- Heap sort
- Most efficient sorting algorithms

---

### 5️⃣ **O(N²) - Quadratic Time**

**Definition:** Nested loops over the data.

```python
def bubble_sort(arr):
    """Compare each element with every other"""
    n = len(arr)
    
    for i in range(n):           # O(N)
        for j in range(n - i - 1):  # O(N)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
    # Total: O(N²)

def find_duplicates_naive(arr):
    """Check every pair"""
    duplicates = []
    
    for i in range(len(arr)):        # O(N)
        for j in range(i + 1, len(arr)):  # O(N)
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    
    return duplicates
    # Total: O(N²)
```

**Real-World Analogy:** Comparing every person in a room with every other person (handshakes).

**Examples:**
- Bubble sort, Selection sort, Insertion sort
- Nested loops
- Checking all pairs

---

### 6️⃣ **O(N³) - Cubic Time**

**Definition:** Three nested loops.

```python
def three_sum_naive(arr, target):
    """Find three numbers that sum to target"""
    n = len(arr)
    
    for i in range(n):           # O(N)
        for j in range(i + 1, n):   # O(N)
            for k in range(j + 1, n):  # O(N)
                if arr[i] + arr[j] + arr[k] == target:
                    return [arr[i], arr[j], arr[k]]
    
    return None
    # Total: O(N³)
```

**Examples:**
- Triple nested loops
- Matrix multiplication (naive)
- Some dynamic programming problems

---

### 7️⃣ **O(2^N) - Exponential Time**

**Definition:** Doubles with each additional input.

```python
def fibonacci_recursive(n):
    """Each call branches into two more calls"""
    if n <= 1:
        return n
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    # Total: O(2^N)

# Call tree for fib(5):
#           fib(5)
#          /      \
#      fib(4)    fib(3)
#      /   \      /   \
#   fib(3) fib(2) ...
#   Exponential growth!

# N = 10 → 1,024 calls
# N = 20 → 1,048,576 calls
# N = 30 → 1,073,741,824 calls (1 billion!)
```

**Real-World Analogy:** Chain letters - each person sends to 2 people, who each send to 2 more...

**Examples:**
- Recursive Fibonacci (naive)
- Generating all subsets
- Solving Tower of Hanoi
- Brute force password cracking

---

### 8️⃣ **O(N!) - Factorial Time**

**Definition:** Generates all permutations.

```python
def generate_permutations(arr):
    """Generate all possible orderings"""
    if len(arr) <= 1:
        return [arr]
    
    perms = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in generate_permutations(rest):
            perms.append([arr[i]] + p)
    
    return perms
    # Total: O(N!)

# Growth:
# N = 3 → 6 permutations
# N = 5 → 120 permutations
# N = 10 → 3,628,800 permutations
# N = 20 → 2,432,902,008,176,640,000 (quintillion!)
```

**Examples:**
- Generating all permutations
- Traveling Salesman Problem (brute force)
- Solving N-Queens (brute force)

---

## 🎯 **Analyzing Time Complexity: Step-by-Step**

### 📋 **The Analysis Process**

```python
# Step 1: Identify basic operations
# Step 2: Count how many times they execute
# Step 3: Express as function of N
# Step 4: Drop constants and lower-order terms
# Step 5: Express in Big O notation
```

### 🔍 **Example 1: Simple Loop**

```python
def example_1(arr):
    total = 0                    # O(1) - once
    
    for num in arr:              # O(N) - N times
        total += num             # O(1) - N times
    
    return total                 # O(1) - once

# Analysis:
# Total = O(1) + N * O(1) + O(1)
#       = O(1) + O(N) + O(1)
#       = O(N)  ← Drop constants
```

### 🔍 **Example 2: Nested Loops**

```python
def example_2(arr):
    count = 0
    
    for i in range(len(arr)):           # O(N)
        for j in range(len(arr)):       # O(N)
            if arr[i] == arr[j]:        # O(1)
                count += 1              # O(1)
    
    return count

# Analysis:
# Outer loop: N iterations
# Inner loop: N iterations per outer
# Total = N * N * O(1) = O(N²)
```

### 🔍 **Example 3: Multiple Loops (Sequential)**

```python
def example_3(arr):
    # First loop
    for i in range(len(arr)):    # O(N)
        print(arr[i])
    
    # Second loop
    for i in range(len(arr)):    # O(N)
        print(arr[i] * 2)
    
    # Third loop
    for i in range(len(arr)):    # O(N)
        print(arr[i] * 3)

# Analysis:
# Total = O(N) + O(N) + O(N)
#       = 3 * O(N)
#       = O(N)  ← Drop constant 3
```

### 🔍 **Example 4: Different Input Sizes**

```python
def example_4(arr1, arr2):
    # Loop over arr1
    for i in arr1:               # O(N)
        print(i)
    
    # Loop over arr2
    for j in arr2:               # O(M)
        print(j)
    
    # Nested loops
    for i in arr1:               # O(N)
        for j in arr2:           # O(M)
            print(i, j)

# Analysis:
# Total = O(N) + O(M) + O(N * M)
#       = O(N * M)  ← Dominant term
# Note: Can't simplify to O(N²) because N ≠ M
```

### 🔍 **Example 5: Logarithmic**

```python
def example_5(n):
    i = 1
    
    while i < n:
        print(i)
        i *= 2  # Double each time

# Trace:
# i = 1, 2, 4, 8, 16, ..., N
# How many doublings to reach N?
# 2^k = N → k = log₂(N)
# Time: O(log N)
```

---

## 🧮 **Space Complexity**

### 🎯 **What is Space Complexity?**

**Space Complexity** measures the **total memory** used by an algorithm.

```python
space_components = {
    "Input Space": "Memory for input data (usually not counted)",
    "Auxiliary Space": "Extra space used by algorithm",
    "Total Space": "Input Space + Auxiliary Space"
}

# Usually we analyze AUXILIARY space
```

### 📊 **Common Space Complexities**

#### **O(1) - Constant Space**
```python
def sum_array(arr):
    """Only uses a few variables"""
    total = 0        # O(1) space
    
    for num in arr:
        total += num
    
    return total

# Auxiliary Space: O(1)
# Only stores: total, num (fixed number of variables)
```

#### **O(N) - Linear Space**
```python
def create_copy(arr):
    """Creates a new array of same size"""
    result = []      # O(N) space
    
    for num in arr:
        result.append(num)
    
    return result

# Auxiliary Space: O(N)
# Stores: result array with N elements
```

#### **O(N²) - Quadratic Space**
```python
def create_matrix(n):
    """Creates 2D matrix"""
    matrix = []
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    
    return matrix

# Auxiliary Space: O(N²)
# Stores: N × N matrix
```

#### **O(log N) - Logarithmic Space (Recursion)**
```python
def binary_search_recursive(arr, target, left, right):
    """Recursive binary search"""
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Auxiliary Space: O(log N)
# Call stack depth: log N levels
```

#### **O(N) - Linear Space (Recursion)**
```python
def factorial_recursive(n):
    """Recursive factorial"""
    if n <= 1:
        return 1
    
    return n * factorial_recursive(n - 1)

# Auxiliary Space: O(N)
# Call stack depth: N levels
# factorial(5) → factorial(4) → ... → factorial(1)
```

---

## 🎯 **Best, Average, and Worst Case**

### 📊 **The Three Cases**

```python
cases = {
    "Best Case (Ω)": "Minimum time/space needed",
    "Average Case (Θ)": "Expected time/space for typical input",
    "Worst Case (O)": "Maximum time/space needed"
}
```

### 🔍 **Example: Linear Search**

```python
def linear_search(arr, target):
    """Search for target in array"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Best Case: Ω(1)
# - Target is first element
# - Only 1 comparison

# Average Case: Θ(N/2) = Θ(N)
# - Target is in middle on average
# - N/2 comparisons on average

# Worst Case: O(N)
# - Target is last element or not present
# - N comparisons
```

### 🔍 **Example: Quick Sort**

```python
def quick_sort(arr):
    """Sort using quick sort"""
    # Implementation details...
    pass

# Best Case: Ω(N log N)
# - Pivot always splits array evenly
# - Balanced partitions

# Average Case: Θ(N log N)
# - Random pivot selection
# - Mostly balanced partitions

# Worst Case: O(N²)
# - Pivot is always smallest/largest
# - Unbalanced partitions (sorted array)
```

---

## 🎓 **Advanced Concepts**

### 🧠 **Amortized Analysis**

**Definition:** Average time per operation over a sequence of operations.

```python
class DynamicArray:
    """Array that grows when full"""
    
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity
    
    def append(self, item):
        if self.size == self.capacity:
            # Resize: O(N)
            self._resize()
        
        self.array[self.size] = item
        self.size += 1
    
    def _resize(self):
        """Double capacity"""
        self.capacity *= 2
        new_array = [None] * self.capacity
        
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array

# Individual append:
# - Usually O(1)
# - Sometimes O(N) when resizing

# Amortized Analysis:
# - N appends total: O(N)
# - Average per append: O(N)/N = O(1)
# - Amortized time: O(1) per append
```

### 🧠 **Recursion Tree Method**

```python
def merge_sort(arr):
    """Analyze using recursion tree"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

"""
Recursion Tree:
                    N                    ← Level 0: O(N)
                  /   \
                N/2   N/2                ← Level 1: O(N)
               / \   / \
             N/4 N/4 N/4 N/4             ← Level 2: O(N)
             
Height: log N levels
Work per level: O(N)
Total: O(N log N)
"""
```

### 🧠 **Master Theorem**

**For recurrences:** `T(N) = a * T(N/b) + f(N)`

```python
"""
Master Theorem Cases:

1. If f(N) = O(N^c) where c < log_b(a):
   T(N) = Θ(N^(log_b(a)))

2. If f(N) = Θ(N^c) where c = log_b(a):
   T(N) = Θ(N^c * log N)

3. If f(N) = Ω(N^c) where c > log_b(a):
   T(N) = Θ(f(N))
"""

# Example: Merge Sort
# T(N) = 2 * T(N/2) + O(N)
# a = 2, b = 2, f(N) = N
# log_b(a) = log_2(2) = 1
# f(N) = N^1 → Case 2
# T(N) = Θ(N log N) ✓

# Example: Binary Search
# T(N) = 1 * T(N/2) + O(1)
# a = 1, b = 2, f(N) = 1
# log_b(a) = log_2(1) = 0
# f(N) = N^0 → Case 2
# T(N) = Θ(log N) ✓
```

---

## 🎯 **Complexity Cheat Sheet**

### 📊 **Data Structure Operations**

```python
data_structure_complexity = {
    "Array": {
        "Access": "O(1)",
        "Search": "O(N)",
        "Insert": "O(N)",
        "Delete": "O(N)"
    },
    
    "Linked List": {
        "Access": "O(N)",
        "Search": "O(N)",
        "Insert": "O(1)",  # at head
        "Delete": "O(1)"   # at head
    },
    
    "Hash Table": {
        "Access": "N/A",
        "Search": "O(1) avg, O(N) worst",
        "Insert": "O(1) avg, O(N) worst",
        "Delete": "O(1) avg, O(N) worst"
    },
    
    "Binary Search Tree (Balanced)": {
        "Access": "O(log N)",
        "Search": "O(log N)",
        "Insert": "O(log N)",
        "Delete": "O(log N)"
    },
    
    "Heap": {
        "Find Min/Max": "O(1)",
        "Insert": "O(log N)",
        "Delete Min/Max": "O(log N)",
        "Build Heap": "O(N)"
    },
    
    "Stack/Queue": {
        "Access": "O(N)",
        "Search": "O(N)",
        "Insert": "O(1)",
        "Delete": "O(1)"
    }
}
```

### 📊 **Sorting Algorithms**

```python
sorting_complexity = {
    "Bubble Sort": {
        "Best": "O(N)",
        "Average": "O(N²)",
        "Worst": "O(N²)",
        "Space": "O(1)"
    },
    
    "Selection Sort": {
        "Best": "O(N²)",
        "Average": "O(N²)",
        "Worst": "O(N²)",
        "Space": "O(1)"
    },
    
    "Insertion Sort": {
        "Best": "O(N)",
        "Average": "O(N²)",
        "Worst": "O(N²)",
        "Space": "O(1)"
    },
    
    "Merge Sort": {
        "Best": "O(N log N)",
        "Average": "O(N log N)",
        "Worst": "O(N log N)",
        "Space": "O(N)"
    },
    
    "Quick Sort": {
        "Best": "O(N log N)",
        "Average": "O(N log N)",
        "Worst": "O(N²)",
        "Space": "O(log N)"
    },
    
    "Heap Sort": {
        "Best": "O(N log N)",
        "Average": "O(N log N)",
        "Worst": "O(N log N)",
        "Space": "O(1)"
    },
    
    "Counting Sort": {
        "Best": "O(N + K)",
        "Average": "O(N + K)",
        "Worst": "O(N + K)",
        "Space": "O(K)"
    }
}
```

### 📊 **Graph Algorithms**

```python
graph_complexity = {
    "BFS/DFS": {
        "Time": "O(V + E)",
        "Space": "O(V)"
    },
    
    "Dijkstra (Binary Heap)": {
        "Time": "O(E log V)",
        "Space": "O(V)"
    },
    
    "Bellman-Ford": {
        "Time": "O(V * E)",
        "Space": "O(V)"
    },
    
    "Floyd-Warshall": {
        "Time": "O(V³)",
        "Space": "O(V²)"
    },
    
    "Kruskal's MST": {
        "Time": "O(E log E)",
        "Space": "O(V)"
    },
    
    "Prim's MST": {
        "Time": "O(E log V)",
        "Space": "O(V)"
    }
}
```

---

## 🎯 **Common Patterns & Rules**

### 📋 **Drop Rules**

```python
# Rule 1: Drop Constants
O(2N) → O(N)
O(N/2) → O(N)
O(100) → O(1)

# Rule 2: Drop Non-Dominant Terms
O(N² + N) → O(N²)
O(N + log N) → O(N)
O(N! + N³) → O(N!)

# Rule 3: Different Variables
O(A + B) → O(A + B)  # Don't simplify!
O(A * B) → O(A * B)  # Don't simplify!
```

### 📋 **Pattern Recognition**

```python
patterns = {
    "Single loop": "O(N)",
    "Nested loops (same size)": "O(N²)",
    "Halving each iteration": "O(log N)",
    "Divide and conquer": "O(N log N)",
    "Two separate loops": "O(N + M)",
    "Loop inside loop (different)": "O(N * M)",
    "Recursive calls (2 branches)": "O(2^N)",
    "All permutations": "O(N!)"
}
```

### 📋 **Quick Identification**

```python
# If you see:
for i in range(N):              → O(N)

for i in range(N):
    for j in range(N):          → O(N²)

while N > 1:
    N = N // 2                  → O(log N)

def recursive(N):
    if N <= 1: return
    recursive(N-1)              → O(N) time, O(N) space

def recursive(N):
    if N <= 1: return
    recursive(N-1)
    recursive(N-1)              → O(2^N) time, O(N) space
```

---

## 📝 **Practice Problems**

### ❓ **Problem 1: Analyze This Code**

```python
def mystery_1(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(i, n):
            print(arr[i], arr[j])

# Question: What's the time complexity?
```

**Answer:**
```python
# Outer loop: N iterations
# Inner loop: 
#   i=0: N iterations
#   i=1: N-1 iterations
#   i=2: N-2 iterations
#   ...
#   i=N-1: 1 iteration

# Total: N + (N-1) + (N-2) + ... + 1
#      = N(N+1)/2
#      = (N² + N)/2
#      = O(N²)  ← Drop constants and lower terms
```

### ❓ **Problem 2: Analyze This Code**

```python
def mystery_2(n):
    i = 1
    
    while i < n:
        j = 0
        while j < n:
            print(i, j)
            j += 1
        i *= 2

# Question: What's the time complexity?
```

**Answer:**
```python
# Outer loop: i doubles each time
# i = 1, 2, 4, 8, ..., N
# Iterations: log N

# Inner loop: Always N iterations

# Total: log N * N = O(N log N)
```

### ❓ **Problem 3: Analyze This Code**

```python
def mystery_3(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mystery_3(arr[:mid])
    right = mystery_3(arr[mid:])
    
    return left + right

# Question: What's the time complexity?
```

**Answer:**
```python
# Recurrence: T(N) = 2*T(N/2) + O(N)
# - Two recursive calls on half the data
# - O(N) for slicing and concatenation

# Using Master Theorem:
# a=2, b=2, f(N)=N
# log_b(a) = log_2(2) = 1
# f(N) = N^1 → Case 2
# T(N) = O(N log N)

# Space: O(N log N) due to slicing creating new arrays
```

### ❓ **Problem 4: Space Complexity**

```python
def mystery_4(n):
    result = []
    
    for i in range(n):
        row = []
        for j in range(i):
            row.append(j)
        result.append(row)
    
    return result

# Question: What's the space complexity?
```

**Answer:**
```python
# result contains:
# Row 0: 0 elements
# Row 1: 1 element
# Row 2: 2 elements
# ...
# Row N-1: N-1 elements

# Total elements: 0 + 1 + 2 + ... + (N-1)
#               = N(N-1)/2
#               = O(N²)

# Space Complexity: O(N²)
```

---

## 🎯 **Key Takeaways**

### ✅ **Essential Concepts**

```python
key_concepts = {
    "Big O": "Upper bound (worst case)",
    "Big Ω": "Lower bound (best case)",
    "Big Θ": "Tight bound (average case)",
    
    "Time Complexity": "How runtime scales with input",
    "Space Complexity": "How memory scales with input",
    "Auxiliary Space": "Extra space beyond input",
    
    "Amortized": "Average over sequence of operations",
    "Recursion": "Don't forget call stack space!"
}
```

### 💡 **Analysis Tips**

```python
tips = [
    "✅ Focus on worst case (Big O) for interviews",
    "✅ Count loops: nested = multiply, sequential = add",
    "✅ Halving → O(log N), Doubling → O(log N)",
    "✅ Recursion → draw tree, count levels",
    "✅ Drop constants and non-dominant terms",
    "✅ Different inputs → different variables (N, M)",
    "✅ Space = variables + data structures + recursion stack",
    "✅ Practice, practice, practice!"
]
```

### 🎯 **Common Mistakes**

```python
mistakes = {
    "❌ Counting operations instead of growth": {
        "Wrong": "This has 5 operations, so O(5)",
        "Right": "This has constant operations, so O(1)"
    },
    
    "❌ Not considering all inputs": {
        "Wrong": "O(N) for two arrays",
        "Right": "O(N + M) for arrays of size N and M"
    },
    
    "❌ Forgetting recursion stack space": {
        "Wrong": "Recursive factorial is O(1) space",
        "Right": "Recursive factorial is O(N) space (call stack)"
    },
    
    "❌ Confusing best and worst case": {
        "Wrong": "Quick sort is always O(N log N)",
        "Right": "Quick sort is O(N log N) average, O(N²) worst"
    }
}
```

---

## 🏆 **Complexity Decision Tree**

```python
"""
How to choose the right complexity:

N ≤ 10:
    → O(N!) is acceptable
    → Can try all permutations

N ≤ 20:
    → O(2^N) is acceptable
    → Can try all subsets

N ≤ 500:
    → O(N³) is acceptable
    → Triple nested loops OK

N ≤ 5,000:
    → O(N²) is acceptable
    → Double nested loops OK

N ≤ 100,000:
    → O(N log N) required
    → Use efficient sorting

N ≤ 1,000,000:
    → O(N) or O(log N) required
    → Single pass or binary search

N > 1,000,000:
    → O(log N) or O(1) required
    → Must be very efficient
"""
```

---

*Master complexity analysis, write efficient code! ⏱️*