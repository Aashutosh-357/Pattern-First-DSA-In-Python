# 🌀 Recursion & Backtracking
> **Phase 4 — Advanced Logic** | Week 8–10
> *"To understand recursion, you must first understand recursion."*

---

## 📌 What You'll Master Here

| Topic | Concept | Classic Problems |
|---|---|---|
| 🔁 Recursion Core | Call stack, base case, tree of calls | Factorial, Fibonacci, Power |
| 🧩 Combinatorics | Permutations & Combinations | Generate all arrangements |
| ♟️ Backtracking | Explore → Fail → Undo → Try Again | N-Queens, Sudoku, Subsets |

---

## 🧠 Part 1 — Recursion: The Mental Model

### 🚫 Don't Think of It as "A Function Calling Itself"

That definition is technically correct but **mentally useless**. Instead, think of it like this:

> **Recursion is delegating the smaller version of the same problem to a "mini-me".**

You handle the *current step*, and you trust your *mini-me* to handle the rest.

---

### 🪆 The Russian Doll Analogy

Imagine a set of Russian dolls (Matryoshka). Each doll contains a smaller version of itself inside. You want to count how many dolls there are.

**You** open the first doll → find another doll → hand it to your **mini-me**.  
Your mini-me opens it → finds another → hands to *their* mini-me.  
This continues until one doll is **empty** — that's the **base case**.

```
count_dolls(doll)
├── if doll is empty → return 0          ← BASE CASE
└── else → 1 + count_dolls(inner_doll)  ← RECURSIVE CASE
```

---

### 🏗️ The Anatomy of Every Recursive Function

Every recursive function has **exactly two parts**:

```python
def recursive_function(problem):
    # 1. BASE CASE — When do we STOP?
    if problem is small enough:
        return answer_directly

    # 2. RECURSIVE CASE — How do we SHRINK the problem?
    smaller_problem = shrink(problem)
    return combine(result, recursive_function(smaller_problem))
```

> ⚠️ **Missing the base case = infinite loop = Stack Overflow.** Always write the base case FIRST.

---

### 📞 The Call Stack — What Actually Happens

Python maintains a **call stack** — a stack of function calls waiting to complete.

**Example: `factorial(4)`**

```
factorial(4)
  └── 4 * factorial(3)
            └── 3 * factorial(2)
                      └── 2 * factorial(1)
                                └── BASE CASE → returns 1
                      returns 2 * 1 = 2
            returns 3 * 2 = 6
  returns 4 * 6 = 24
```

**Visualization of the call stack (builds up, then unwinds):**

```
PUSH (growing) →          UNWIND (returning) →
┌─────────────┐           ┌─────────────┐
│ factorial(1)│ → 1       │             │
├─────────────┤           │             │
│ factorial(2)│ → 2*1=2   │             │
├─────────────┤           │             │
│ factorial(3)│ → 3*2=6   │             │
├─────────────┤           │             │
│ factorial(4)│ → 4*6=24  │ ✅ RESULT   │
└─────────────┘           └─────────────┘
```

---

### 🐍 Implementation: Classic Recursion Problems

#### ✅ Problem 1 — Factorial

```python
def factorial(n: int) -> int:
    """Returns n! = n * (n-1) * ... * 1"""
    # Base case: 0! = 1, 1! = 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)


# --- Test ---
print(factorial(5))   # Output: 120
print(factorial(0))   # Output: 1
```

**Complexity:**
- ⏱️ Time: `O(n)` — n recursive calls
- 💾 Space: `O(n)` — n frames on the call stack

---

#### ✅ Problem 2 — Fibonacci (Naive vs. Memoized)

**Naive Recursion (Exponential — BAD for large n):**

```python
def fib_naive(n: int) -> int:
    """Fibonacci: fib(n) = fib(n-1) + fib(n-2)"""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)
```

**Why is it slow?** The same subproblems are solved over and over:

```
fib(5)
├── fib(4)
│   ├── fib(3)          ← computed twice!
│   │   ├── fib(2)
│   │   └── fib(1)
│   └── fib(2)          ← computed multiple times!
└── fib(3)              ← computed twice!
    ├── fib(2)
    └── fib(1)
```

**Optimized with Memoization (Linear — GOOD):**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """Memoized Fibonacci — each subproblem solved exactly once."""
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


# --- Test ---
print(fib_memo(10))   # Output: 55
print(fib_memo(50))   # Output: 12586269025 (try this with naive — it'll hang!)
```

**Complexity (Memoized):**
- ⏱️ Time: `O(n)` — each unique subproblem computed once
- 💾 Space: `O(n)` — memo cache + call stack

---

## 🧩 Part 2 — Combinatorics: Permutations & Combinations

### 🗺️ The Big Picture

Think of combinatorics as **choices at each step**:

```
PERMUTATIONS                    COMBINATIONS
[1, 2, 3] → all orderings      [1, 2, 3] → all subsets (order doesn't matter)
─────────────────────────────  ──────────────────────────────────────────────
[1,2,3], [1,3,2], [2,1,3],     [1], [2], [3],
[2,3,1], [3,1,2], [3,2,1]      [1,2], [1,3], [2,3],
                                [1,2,3], []
Total: n! = 3! = 6             Total: 2^n = 2^3 = 8
```

---

### 🔁 Generating Permutations — The "Choose & Recurse" Pattern

**Mental Model:** At each step, pick one unused element. Recurse on the rest. When nothing is left, you've found a permutation.

```
Start: [1, 2, 3]

Pick 1 → recurse([2,3])
  Pick 2 → recurse([3])
    Pick 3 → recurse([]) → ✅ [1,2,3]
  Pick 3 → recurse([2])
    Pick 2 → recurse([]) → ✅ [1,3,2]

Pick 2 → recurse([1,3])
  ...and so on
```

```python
from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    """Generate all permutations of a list of unique integers."""
    result: List[List[int]] = []

    def backtrack(current: List[int], remaining: List[int]) -> None:
        # Base case: nothing left to pick → we have a full permutation
        if not remaining:
            result.append(current[:])  # append a copy
            return

        # Recursive case: try each remaining element as the next pick
        for i in range(len(remaining)):
            # Choose: pick remaining[i]
            current.append(remaining[i])
            # Recurse: on everything except remaining[i]
            backtrack(current, remaining[:i] + remaining[i+1:])
            # Un-choose (backtrack): remove last pick and try the next
            current.pop()

    backtrack([], nums)
    return result


# --- Test ---
print(permutations([1, 2, 3]))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

**Complexity:**
- ⏱️ Time: `O(n! × n)` — n! permutations, each of length n to copy
- 💾 Space: `O(n)` — recursion depth is at most n

---

### 🔁 Generating All Subsets — The "Include or Exclude" Pattern

**Mental Model:** For every element, make a binary choice: **include** it or **exclude** it.

```
nums = [1, 2, 3]

                      []
          /                  \
       [1]                    []
      /    \                /    \
  [1,2]   [1]           [2]      []
  /  \    /  \          /  \    /  \
[1,2,3][1,2][1,3][1] [2,3][2] [3] []

All leaf nodes are valid subsets!
```

```python
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """Generate all 2^n subsets of a list."""
    result: List[List[int]] = []

    def backtrack(index: int, current: List[int]) -> None:
        # Every state is a valid subset — record it
        result.append(current[:])

        for i in range(index, len(nums)):
            # Include nums[i]
            current.append(nums[i])
            # Recurse on next elements (index = i+1 avoids duplicates)
            backtrack(i + 1, current)
            # Exclude nums[i] (backtrack)
            current.pop()

    backtrack(0, [])
    return result


# --- Test ---
print(subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
```

**Complexity:**
- ⏱️ Time: `O(2^n × n)` — 2^n subsets, each up to length n to copy
- 💾 Space: `O(n)` — recursion depth

---

## ♟️ Part 3 — Backtracking: The Explore & Undo Pattern

### 🗺️ The Core Mental Model

> **Backtracking = Depth-First Search on a Decision Tree, with the ability to UNDO bad choices.**

Think of it like navigating a maze:
1. **Explore** a path.
2. Hit a **dead end**? Mark it and **undo** your last step.
3. **Try** the next available path.
4. Repeat until you find the exit — or exhaust all paths.

```
The Backtracking Template:
────────────────────────────────────────
def backtrack(state):
    if is_solution(state):        # ← Goal check
        record(state)
        return

    for choice in get_choices(state):
        if is_valid(choice, state):   # ← Prune invalid paths early
            make_choice(choice, state)
            backtrack(state)              # ← Explore deeper
            undo_choice(choice, state)    # ← UNDO (this is the "backtrack")
────────────────────────────────────────
```

---

### ♟️ Classic Problem 1 — N-Queens

**Problem:** Place N queens on an N×N chessboard such that no two queens attack each other.

**Rules:** No two queens can share the same row, column, or diagonal.

**Visual for N=4:**

```
. Q . .      . . Q .
. . . Q      Q . . .
Q . . .      . . . Q
. . Q .      . Q . .

Solution 1   Solution 2
```

**Strategy — Place one queen per row:**

For each row, try placing the queen in each column. If safe, move to the next row. If stuck, backtrack.

```python
from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """
    Returns all distinct solutions to the N-Queens puzzle.
    Each solution is a list of strings representing the board.
    'Q' = Queen, '.' = Empty cell.
    """
    results: List[List[str]] = []
    # Track which columns and diagonals are occupied
    cols: set = set()
    pos_diag: set = set()   # row - col is constant on a positive diagonal
    neg_diag: set = set()   # row + col is constant on a negative diagonal

    board: List[List[str]] = [['.' for _ in range(n)] for _ in range(n)]

    def backtrack(row: int) -> None:
        # Base case: placed queens in all n rows → valid solution found
        if row == n:
            results.append([''.join(r) for r in board])
            return

        for col in range(n):
            # Skip if this column or either diagonal is already attacked
            if col in cols or (row - col) in pos_diag or (row + col) in neg_diag:
                continue

            # Place queen: mark attacked lines
            cols.add(col)
            pos_diag.add(row - col)
            neg_diag.add(row + col)
            board[row][col] = 'Q'

            backtrack(row + 1)  # Move to next row

            # Remove queen: unmark attacked lines (BACKTRACK)
            cols.remove(col)
            pos_diag.remove(row - col)
            neg_diag.remove(row + col)
            board[row][col] = '.'

    backtrack(0)
    return results


# --- Test ---
solutions = solve_n_queens(4)
print(f"Total solutions for N=4: {len(solutions)}")  # Output: 2
for sol in solutions:
    for row in sol:
        print(row)
    print()
```

**Complexity:**
- ⏱️ Time: `O(n!)` — n choices in row 1, n-1 in row 2, etc.
- 💾 Space: `O(n)` — recursion depth + sets for tracking

---

### 🔢 Classic Problem 2 — Sudoku Solver

**Problem:** Given a partially filled 9×9 Sudoku grid, fill it completely following the rules.

**Rules:**
- Each row must contain digits 1–9, no repeats.
- Each column must contain digits 1–9, no repeats.
- Each of the 9 sub-boxes (3×3) must contain digits 1–9, no repeats.

**Strategy — Fill one empty cell at a time:**

```
Find the first empty cell (marked '.').
Try digits 1–9:
  → Is this digit valid here? (check row, col, 3×3 box)
  → Yes: Fill it in, recurse to the next empty cell.
  → Recurse returned True: puzzle solved! ✅
  → Recurse returned False (dead end): undo, try the next digit.
  → No digit worked: return False (backtrack to parent).
```

```python
from typing import List


def solve_sudoku(board: List[List[str]]) -> None:
    """
    Solves a 9x9 Sudoku board in-place.
    Empty cells are represented by '.'.
    """

    def is_valid(row: int, col: int, num: str) -> bool:
        """Check if placing `num` at board[row][col] is valid."""
        # Check the row
        if num in board[row]:
            return False
        # Check the column
        if num in [board[r][col] for r in range(9)]:
            return False
        # Check the 3x3 sub-box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False
        return True

    def backtrack() -> bool:
        """Find the next empty cell and try digits. Returns True if solved."""
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    # Try each digit
                    for num in '123456789':
                        if is_valid(row, col, num):
                            board[row][col] = num       # Place digit
                            if backtrack():             # Recurse
                                return True             # ✅ Solved!
                            board[row][col] = '.'       # Undo (backtrack)
                    return False  # No digit worked → dead end
        return True  # No empty cell found → puzzle is complete!

    backtrack()


# --- Test ---
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]
solve_sudoku(board)
for row in board:
    print(row)
```

**Complexity:**
- ⏱️ Time: `O(9^m)` where m = number of empty cells. In the worst case, m = 81.
- 💾 Space: `O(m)` — recursion depth equals the number of empty cells.

---

## 🔢 Part 4 — Combinations (a.k.a. "Pick K from N")

**Problem:** Given a set of numbers, find all combinations of size `k`.

**Mental Model:** It's like subsets, but we only record when the subset has exactly `k` elements. We also avoid revisiting previous elements (start from `index` forward).

```
nums = [1,2,3,4], k = 2

                    []
         /      /       \      \
       [1]    [2]       [3]    [4]
      / | \    | \       |
  [1,2][1,3][1,4] [2,3][2,4]  [3,4]
  ✅  ✅   ✅   ✅   ✅    ✅
```

```python
from typing import List


def combinations(n: int, k: int) -> List[List[int]]:
    """
    Return all combinations of k numbers from 1 to n.
    LeetCode 77. Combinations.
    """
    result: List[List[int]] = []

    def backtrack(start: int, current: List[int]) -> None:
        # Goal: collected exactly k elements
        if len(current) == k:
            result.append(current[:])
            return

        # Optimization: only iterate if enough elements remain
        # i can go up to n - (k - len(current)) + 1
        for i in range(start, n - (k - len(current)) + 2):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return result


# --- Test ---
print(combinations(4, 2))
# [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
```

---

## 🔑 Part 5 — The Backtracking Pattern Encyclopedia

### 🗂️ When to Use Backtracking?

| Signal in Problem | Pattern to Use |
|---|---|
| "Find **all** solutions" | Backtracking |
| "Generate all **permutations/combinations/subsets**" | Backtracking |
| "Fill a **grid** with constraints" | Backtracking + Constraint Check |
| "Is there **any** valid arrangement?" | Backtracking (return True on first solution) |
| "Count the number of solutions" | Backtracking + Counter |

---

### 🧹 The Pruning Principle — Cut Bad Branches Early

The key to efficient backtracking is **pruning**: never explore a path you already know is invalid.

```
Without Pruning:               With Pruning:
Explore ALL branches           Skip invalid branches instantly

  [1,2,3,4,5]                   [1,2,3,4,5]
  └── try all                   └── try only valid ones
      └── check at the end          └── check before going deeper
      
Result: SLOW 🐢                Result: FAST 🐇
```

In N-Queens, we use sets (`cols`, `pos_diag`, `neg_diag`) to check in `O(1)` instead of scanning the board — this is pruning.

---

## 📊 Complexity Summary

| Problem | Time | Space | Notes |
|---|---|---|---|
| Factorial | `O(n)` | `O(n)` | Linear call depth |
| Fibonacci (Naive) | `O(2^n)` | `O(n)` | Exponential — use memo! |
| Fibonacci (Memo) | `O(n)` | `O(n)` | Linear with caching |
| Permutations | `O(n! × n)` | `O(n)` | n! results × n to copy each |
| Subsets | `O(2^n × n)` | `O(n)` | 2^n results × n to copy each |
| Combinations | `O(C(n,k) × k)` | `O(k)` | Pruned search tree |
| N-Queens | `O(n!)` | `O(n)` | With constraint sets (O(1) lookup) |
| Sudoku | `O(9^m)` | `O(m)` | m = number of empty cells |

---

## 🎯 LeetCode Practice Problems

### 🟢 Easy — Build the Foundation

| # | Problem | Core Idea |
|---|---|---|
| 509 | Fibonacci Number | Direct recursion |
| 70 | Climbing Stairs | Fibonacci in disguise |
| 344 | Reverse String | Recursion with two pointers |
| 206 | Reverse Linked List | Recursive pointer manipulation |

### 🟡 Medium — The Backtracking Core

| # | Problem | Core Idea |
|---|---|---|
| 78 | Subsets | Include/Exclude pattern |
| 90 | Subsets II | Subsets with duplicates |
| 46 | Permutations | Choose & Recurse |
| 47 | Permutations II | Permutations with duplicates |
| 77 | Combinations | Pick K from N |
| 39 | Combination Sum | Unbounded combinations |
| 40 | Combination Sum II | Combinations with duplicates |
| 22 | Generate Parentheses | Valid string construction |
| 79 | Word Search | Grid-based backtracking |

### 🔴 Hard — The Full Challenge

| # | Problem | Core Idea |
|---|---|---|
| 51 | N-Queens | Constraint-pruned backtracking |
| 52 | N-Queens II | Count of N-Queens solutions |
| 37 | Sudoku Solver | Grid filling with constraint checks |
| 131 | Palindrome Partitioning | String segmentation backtracking |
| 212 | Word Search II | Backtracking + Trie |

---

## 🚀 The "3-Step" Problem-Solving Checklist for Backtracking

Before writing any code, answer these three questions:

```
1. WHAT IS MY DECISION?
   └── "At each step, what choices do I have?"
       (e.g., "Which digit to place in this cell?")

2. WHAT IS MY GOAL STATE?
   └── "When do I record/return a solution?"
       (e.g., "When all 9 rows are filled with queens.")

3. WHAT MAKES A CHOICE INVALID?
   └── "What should I check BEFORE making a choice?"  (Pruning)
       (e.g., "Does this digit already exist in the row/col/box?")
```

Write the template, answer these three questions, and the code writes itself. ✅

---

> 📝 **Next Up:** [02-Dynamic-Programming.md](./02-Dynamic-Programming.md) — Where we turn exponential backtracking into polynomial solutions using Memoization & Tabulation.