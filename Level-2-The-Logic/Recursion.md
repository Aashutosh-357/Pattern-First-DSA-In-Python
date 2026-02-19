# 🌀 Recursion - The Art of Self-Reference

> *"To understand recursion, you must first understand recursion."*

🎯 **Mission:** Recursion is the backbone of Trees, Graphs, Dynamic Programming, and Backtracking. Nail this, and the rest of Level 2 will feel natural. The secret: **stop trying to trace it all — trust the math.**

---

## 📚 Table of Contents

| Section | Topics Covered |
|---------|----------------|
| **Part A: The Mental Model** | What is recursion, The Call Stack, The "Leap of Faith" |
| **Part B: Base Cases** | Why they exist, Missing them, Common patterns |
| **Part C: Types of Recursion** | Linear, Tail, Tree, Mutual |
| **Part D: Classic Problems** | Factorial, Fibonacci, Binary Search, Power |
| **Part E: Tree Recursion** | Subsets, Permutations, Flood Fill |
| **Part F: The Stack Memory** | Stack frames, Stack overflow, Space complexity |

---

## 🧠 Part A: The Mental Model

### 💡 What IS Recursion?

A function that **calls itself** with a **smaller version of the same problem**, until it hits a condition small enough to solve directly.

```
solve(BIG_PROBLEM)
  = solve(SMALLER_PROBLEM) + some_work
    = solve(EVEN_SMALLER) + some_work
      = solve(BASE_CASE) ← returns directly!
      ↑ results bubble back up the chain
```

### 🎯 The Russian Doll Analogy

```
🪆 Open the big doll
   🪆 Open the next doll
      🪆 Open the next doll
         🎉 Found the smallest doll! (Base Case)
      🪆 Put this doll back
   🪆 Put this doll back
🪆 Done!
```

Every recursive call **opens a new doll**. The base case is the **smallest doll**. Results are collected as you **close each doll back up**.

---

### 🎯 The "Leap of Faith" — The Most Important Mindset

> *You do NOT need to trace the entire recursion. Just trust that your function works correctly for smaller inputs.*

**Example:** Reversing a linked list recursively.

```
Assume reverse(2 → 3 → 4) correctly gives 4 → 3 → 2
Then reverse(1 → 2 → 3 → 4) just needs:
  - Call reverse(2 → 3 → 4)  → [trust it] → 4 → 3 → 2
  - Tack 1 to the end
  - Done! 4 → 3 → 2 → 1
```

This mindset is called **The Leap of Faith** and is *essential* for writing recursive code naturally.

---

## 🛑 Part B: Base Cases

### 💡 What is a Base Case?

The **termination condition** — the case so simple it can be answered *without* recursion.

**Every recursive function MUST have:**
1. ✅ A **base case** (termination)
2. ✅ A **recursive call** with a **smaller/simpler input**

### ⚠️ What Happens Without a Base Case?

```python
def infinite(n):
    return infinite(n - 1)  # ❌ No base case!

# Result:
# RecursionError: maximum recursion depth exceeded
```

The function calls itself forever until Python hits its **recursion limit** (~1000 calls).

### 🔥 Identifying Base Cases

Ask yourself: **"What is the simplest possible input to this problem?"**

| Problem | Base Case |
|---------|-----------|
| Factorial of n | `n == 0` or `n == 1` → return 1 |
| Length of a list | `list is empty` → return 0 |
| Binary search | `left > right` → return -1 |
| Tree traversal | `node is None` → return |
| Fibonacci | `n <= 1` → return n |

---

## 🌿 Part C: Types of Recursion

### 1️⃣ Linear Recursion

One recursive call per function call. Like a **straight chain**.

```
fact(5)
  → fact(4)
    → fact(3)
      → fact(2)
        → fact(1) ← base case
```

```python
def factorial(n: int) -> int:
    if n <= 1:        # Base case
        return 1
    return n * factorial(n - 1)  # Linear recursion
```

---

### 2️⃣ Tail Recursion

The recursive call is the **very last operation**. Nothing happens after it returns. Python doesn't optimize this (unlike some languages), but the pattern matters.

```python
# ❌ Not tail-recursive (multiplication happens AFTER the call)
def factorial(n, acc=1):
    if n <= 1:
        return acc
    return factorial(n - 1, n * acc)  # ✅ Tail-recursive (acc carries the result)
```

---

### 3️⃣ Tree Recursion ⭐

**Two or more** recursive calls per function call. Calls branch like a tree.

```
fib(4)
├── fib(3)
│   ├── fib(2)
│   │   ├── fib(1) ← 1
│   │   └── fib(0) ← 0
│   └── fib(1) ← 1
└── fib(2)
    ├── fib(1) ← 1
    └── fib(0) ← 0
```

```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)  # TWO calls → Tree recursion
```

---

### 4️⃣ Mutual Recursion

Two functions that **call each other**.

```python
def is_even(n: int) -> bool:
    if n == 0: return True
    return is_odd(n - 1)

def is_odd(n: int) -> bool:
    if n == 0: return False
    return is_even(n - 1)
```

---

## 🏆 Part D: Classic Problems (Dry-Run Traces)

### 🔥 **Problem 1: Factorial** ⭐

```
factorial(4)
= 4 × factorial(3)
      = 3 × factorial(2)
            = 2 × factorial(1)
                  = 1  ← base case
            = 2 × 1 = 2
      = 3 × 2 = 6
= 4 × 6 = 24
```

```python
def factorial(n: int) -> int:
    """
    n! = n × (n-1) × (n-2) × ... × 1

    Base:      n <= 1 → return 1
    Recursive: n × factorial(n - 1)
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Test
print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(10))  # 3628800
```

**Complexity:** Time O(n), Space O(n) — n frames on the call stack.

---

### 🔥 **Problem 2: Fibonacci (Naive & Memoized)** ⭐⭐

**Naive — The Exponential Monster:**

```python
def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# fib_naive(40) → takes SECONDS  ❌
```

**Why is it slow?**  
`fib(5)` calls `fib(4)` and `fib(3)`, `fib(4)` calls `fib(3)` and `fib(2)`, etc.  
`fib(3)` is computed **multiple times** — pure waste!

**Memoized — The Speed Demon:**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """
    Store subproblem results. Never recompute.
    
    fib(5) call tree WITH memo:
    fib(5) → fib(4) → fib(3) → fib(2) → fib(1) ← 1
                                        ← fib(0) ← 0
                               ← 1
                      ← fib(2) → CACHE HIT! ← 1
             ← fib(3) → CACHE HIT!
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# fib(100) → instant  ✅
print(fib(10))   # 55
print(fib(50))   # 12586269025
```

| Version | Time | Space |
|---------|------|-------|
| Naive | O(2ⁿ) | O(n) |
| Memoized | O(n) | O(n) |

---

### 🔥 **Problem 3: Recursive Binary Search** ⭐⭐

```python
from typing import List

def binary_search(arr: List[int], target: int, left: int, right: int) -> int:
    """
    Divide the search space in half each call.

    Dry Run: arr=[1,3,5,7,9], target=7
    Call 1: left=0, right=4, mid=2, arr[2]=5 < 7 → search right
    Call 2: left=3, right=4, mid=3, arr[3]=7 == 7 → return 3 ✓
    """
    if left > right:    # Base case: not found
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

# Test
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7, 0, len(arr) - 1))   # 3
print(binary_search(arr, 6, 0, len(arr) - 1))   # -1
```

**Complexity:** Time O(log n), Space O(log n) — log n frames on the stack.

---

### 🔥 **Problem 4: Power (Fast Exponentiation)** ⭐⭐

```python
def power(base: float, exp: int) -> float:
    """
    Calculate base^exp using recursive divide & conquer.

    Insight:
    x^8 = (x^4) × (x^4)     → Only compute x^4 ONCE!
    x^7 = (x^3) × (x^3) × x → Odd: one extra multiply

    Dry Run: power(2, 10)
    = power(2, 5)²
      = power(2, 2)² × 2
        = power(2, 1)²
          = power(2, 0) × 2 → 2
        = 2² = 4
      = 4² × 2 = 32
    = 32² = 1024
    """
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)

    half = power(base, exp // 2)

    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base

# Test
print(power(2, 10))   # 1024
print(power(3, 5))    # 243
print(power(2, -3))   # 0.125
```

**Complexity:** Time O(log n), Space O(log n) — much better than naive O(n)!

---

### 🔥 **Problem 5: Sum of Digits** ⭐

```python
def sum_of_digits(n: int) -> int:
    """
    Sum all digits of n recursively.

    sum_of_digits(1234)
    = 4 + sum_of_digits(123)
        = 3 + sum_of_digits(12)
            = 2 + sum_of_digits(1)
                = 1 + sum_of_digits(0) = 1
            = 2 + 1 = 3
        = 3 + 3 = 6
    = 4 + 6 = 10
    """
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))  # 10
print(sum_of_digits(9999))  # 36
```

---

## 🌳 Part E: Tree Recursion Patterns

### 🔥 **Pattern 1: Generate All Subsets** ⭐⭐⭐

For each element, we make a **binary choice**: include it or skip it.

```
Elements: [1, 2, 3]

                    []
            /              \
         [1]               []
        /     \           /    \
    [1,2]    [1]       [2]     []
    /   \    /  \      /  \    /  \
[1,2,3][1,2][1,3][1][2,3][2][3]  []
```

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all 2^n subsets using include/exclude recursion.
    """
    result = []

    def backtrack(index: int, current: List[int]) -> None:
        # Base case: we've decided on every element
        if index == len(nums):
            result.append(current[:])
            return

        # Choice 1: Include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()  # Undo

        # Choice 2: Exclude nums[index]
        backtrack(index + 1, current)

    backtrack(0, [])
    return result

# Test
print(subsets([1, 2, 3]))
# [[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]]
```

**Complexity:** Time O(2ⁿ × n), Space O(n) call stack + O(2ⁿ × n) output.

---

### 🔥 **Pattern 2: Generate All Permutations** ⭐⭐⭐

```python
def permutations(nums: List[int]) -> List[List[int]]:
    """
    Generate all n! permutations.

    For [1, 2, 3]:
    Fix 1 → permute [2,3] → [1,2,3], [1,3,2]
    Fix 2 → permute [1,3] → [2,1,3], [2,3,1]
    Fix 3 → permute [1,2] → [3,1,2], [3,2,1]
    """
    result = []

    def backtrack(current: List[int], remaining: List[int]) -> None:
        if not remaining:       # Base case: nothing left to place
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()       # Undo

    backtrack([], nums)
    return result

# Test
print(permutations([1, 2, 3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Complexity:** Time O(n! × n), Space O(n).

---

### 🔥 **Pattern 3: Flood Fill (Recursive DFS on Grid)** ⭐⭐

```python
def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    Color a connected region like the MS Paint bucket tool.

    image = [[1,1,1],
             [1,1,0],
             [1,0,1]]
    Start (sr=1, sc=1), new color=2

    Result: [[2,2,2],
             [2,2,0],
             [2,0,1]]
    """
    original_color = image[sr][sc]

    if original_color == color:   # Avoid infinite loop
        return image

    def dfs(r: int, c: int) -> None:
        # Base cases: out of bounds or wrong color
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        if image[r][c] != original_color:
            return

        image[r][c] = color       # Paint this cell

        # Recurse in all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image
```

---

## 📦 Part F: The Stack Memory — What Happens Under the Hood

### 💡 The Call Stack

Every function call creates a **stack frame** in memory:

```
factorial(4) calls factorial(3)
  └── factorial(3) calls factorial(2)
        └── factorial(2) calls factorial(1)
              └── factorial(1) returns 1  ← TOP of stack
              ↑ Stack unwinds from here
        └── factorial(2) = 2 × 1 = 2
  └── factorial(3) = 3 × 2 = 6
factorial(4) = 4 × 6 = 24
```

**Visualization:**
```
│ factorial(1) │ ← TOP (most recent)
│──────────────│
│ factorial(2) │
│──────────────│
│ factorial(3) │
│──────────────│
│ factorial(4) │ ← BOTTOM (first call)
└──────────────┘
     STACK
```

### ⚠️ Stack Overflow

Python's default recursion limit is **~1000**.

```python
import sys
print(sys.getrecursionlimit())  # 1000

# Increase if needed (use carefully!)
sys.setrecursionlimit(10000)
```

**Rule of thumb:** If your input can be > 1000 and you're using recursion, consider converting to an **iterative solution with an explicit stack**.

### 📊 Space Complexity of Recursion

| Pattern | Space (Stack) | Why |
|---------|---------------|-----|
| Linear recursion on n | O(n) | n frames deep |
| Binary search | O(log n) | Halves each time |
| Tree recursion (fib) | O(n) | Max depth is n |
| Subsets | O(n) | Max depth is n |
| Permutations | O(n) | Max depth is n |

---

## 🧪 Challenge Zone

> 🎯 **Test your recursive thinking!**

### 🟢 **Problem 1: Palindrome Check**
Check if a string is a palindrome using recursion.  
`is_palindrome("racecar")` → `True`

**💡 Hint:** Compare first and last character, recurse on middle.

<details>
<summary>Click for solution</summary>

```python
def is_palindrome(s: str) -> bool:
    if len(s) <= 1:     # Base: 0 or 1 chars → always palindrome
        return True
    if s[0] != s[-1]:   # Mismatch → not palindrome
        return False
    return is_palindrome(s[1:-1])  # Check middle

print(is_palindrome("racecar"))    # True
print(is_palindrome("hello"))      # False
```
</details>

---

### 🟡 **Problem 2: Tower of Hanoi**
Move n disks from peg A to peg C using peg B as helper.

**Rules:**
1. Move only one disk at a time
2. Never place a larger disk on a smaller one

**💡 Hint:** Move (n-1) disks to B, move largest to C, move (n-1) from B to C.

<details>
<summary>Click for solution</summary>

```python
def hanoi(n: int, source: str, destination: str, auxiliary: str) -> None:
    """
    Dry run for n=3:
    Move disk 1: A → C
    Move disk 2: A → B
    Move disk 1: C → B
    Move disk 3: A → C
    Move disk 1: B → A
    Move disk 2: B → C
    Move disk 1: A → C
    Total: 2^n - 1 = 7 moves
    """
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return

    hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} → {destination}")
    hanoi(n - 1, auxiliary, destination, source)

hanoi(3, 'A', 'C', 'B')
```
</details>

---

### 🟠 **Problem 3: Merge Sort**
Sort an array using the divide-and-conquer recursive approach.

**💡 Hint:** Split in half, sort each half recursively, merge the two sorted halves.

<details>
<summary>Click for solution</summary>

```python
def merge_sort(arr: List[int]) -> List[int]:
    """
    Divide: split into halves
    Conquer: sort each half (recursively)
    Combine: merge the sorted halves
    """
    if len(arr) <= 1:   # Base case
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge two sorted halves
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

print(merge_sort([5, 3, 8, 1, 9, 2]))  # [1, 2, 3, 5, 8, 9]
```
</details>

---

### 🔴 **Problem 4: Count Ways to Climb Stairs**
You can climb 1 or 2 steps at a time. How many ways to reach step `n`?

**💡 Hint:** `ways(n) = ways(n-1) + ways(n-2)`. It's Fibonacci in disguise!

<details>
<summary>Click for solution</summary>

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def climb_stairs(n: int) -> int:
    """
    ways(1) = 1   → [1]
    ways(2) = 2   → [1+1, 2]
    ways(3) = 3   → [1+1+1, 1+2, 2+1]
    ways(4) = 5   → ...
    Pattern: Fibonacci!
    """
    if n <= 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)

print(climb_stairs(5))    # 8
print(climb_stairs(10))   # 89
```
</details>

---

### 🏆 **Problem 5: N-Queens (Count Solutions)**
Place N queens on an N×N chessboard so no two queens attack each other.

**💡 Hint:** Place one queen per row, recurse to next row, backtrack if conflict.

<details>
<summary>Click for solution</summary>

```python
def n_queens(n: int) -> int:
    """
    Returns number of valid arrangements.

    For n=4:
    . Q . .    . . Q .
    . . . Q    Q . . .
    Q . . .    . . . Q
    . . Q .    . Q . .
    Answer: 2
    """
    def is_safe(row, col, queens):
        for r, c in enumerate(queens):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(row, queens):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(row, col, queens):
                count += backtrack(row + 1, queens + [col])
        return count

    return backtrack(0, [])

print(n_queens(4))   # 2
print(n_queens(8))   # 92
```
</details>

---

## 📈 When to Use Recursion

| ✅ Use Recursion | ❌ Avoid Recursion |
|-------------------|-------------------|
| Tree/Graph traversal | Input n > 10,000 without memoization |
| Divide & conquer (Merge Sort) | Simple loops (sum of array) |
| Backtracking (Subsets, N-Queens) | When stack overflow risk is high |
| Problems with natural sub-structure | When iterative is equally clear |

---

## 🎓 Key Takeaways

✅ **Base Case** — Every recursive function MUST have one. It's the exit condition.  
✅ **Leap of Faith** — Trust your function works for smaller inputs. Don't trace everything.  
✅ **Stack Memory** — Each call adds a frame. Deep recursion → large space usage.  
✅ **Memoization** — Eliminates redundant calls in tree recursion (O(2ⁿ) → O(n)).  
✅ **Tree Recursion** — Multiple recursive calls per level — power of backtracking.  

---

## 🚀 Next Steps

With recursion mastered, you're ready for the most powerful techniques:
- **Backtracking** — Recursion + constraint checking + undo (N-Queens, Sudoku)
- **Dynamic Programming** — Memoized recursion → tabulation optimization
- **Trees & Graphs** — Almost entirely solved through recursive patterns!

**Remember:** Every recursive problem is just a tree of decisions. Draw the tree, identify the base cases, trust the recursion. 🌳

---

*Happy Recursing! 🎉*