# ⚡ Dynamic Programming (DP)
> **Phase 4 — Advanced Logic** | Week 8–10
> *"Those who cannot remember the past are condemned to repeat it."* — George Santayana (and also recursion)

---

## 📌 What You'll Master Here

| Topic | Concept | Classic Problems |
|---|---|---|
| 🧠 The DP Mindset | Why DP? Overlapping subproblems + Optimal substructure | Fibonacci |
| 📥 Memoization | Top-Down: recursion + a cache | Climbing Stairs, Coin Change |
| 📤 Tabulation | Bottom-Up: build the answer table iteratively | Fibonacci, Grid paths |
| 🎒 0/1 Knapsack | The "take it or leave it" decision pattern | Classic Knapsack, Subset Sum |
| 🧵 LCS | Matching subsequences in two strings | DNA alignment, Diff tools |

---

## 🧠 Part 1 — The DP Mindset: Why Does It Exist?

### 🚫 The Problem with Naive Recursion

In the previous section, we saw that naive Fibonacci has **exponential** time complexity.

```
fib(5)
├── fib(4)
│   ├── fib(3) ← computed here...
│   └── fib(2)
└── fib(3) ← ...AND computed again here! (wasted work)
    ├── fib(2)
    └── fib(1)
```

We are solving **the same subproblems over and over again**. This is the root of all evil in naive recursion.

> **DP is the antidote.** It says: *"Solve each subproblem exactly ONCE, then store the answer."*

---

### ✅ Two Prerequisites for DP

A problem is solvable with DP only if it has **both** of these properties:

| Property | Meaning | Example |
|---|---|---|
| **Overlapping Subproblems** | The same smaller problems appear multiple times | `fib(3)` is called thousands of times |
| **Optimal Substructure** | The optimal answer to the big problem is built from the optimal answers to subproblems | `fib(5) = fib(4) + fib(3)` |

> ⚠️ **Counterexample:** Finding the shortest path in a graph (Dijkstra) has optimal substructure, but Merge Sort does NOT have overlapping subproblems — so only the shortest path problem uses DP.

---

### 🗺️ The Two Flavours of DP

```
THE SAME GOAL: Solve each subproblem only once.
TWO DIFFERENT APPROACHES:

  TOP-DOWN (Memoization)          BOTTOM-UP (Tabulation)
  ──────────────────────          ──────────────────────
  Start from the big problem.     Start from the smallest
  Recurse down to base cases.     subproblems. Build up.

  fib(5) → fib(4) → fib(3)...    fib(1), fib(2), fib(3)...
  Cache each result.              Fill a table iteratively.

  Feels like: Recursion + memo    Feels like: A for-loop filling
              dict                            an array

  ✅ Easier to write              ✅ No recursion overhead
  ✅ Only solves needed parts     ✅ Better space optimization
  ❌ Recursion call stack         ❌ Must figure out order upfront
```

---

## 📥 Part 2 — Memoization (Top-Down DP)

### 🪄 The Recipe

```
1. Write the naive recursive solution.
2. Add a cache (dictionary or @lru_cache).
3. Before computing, check: "Have I solved this before?"
   → YES: return the cached answer.
   → NO: compute it, store it, then return it.
```

---

### 🐍 Example 1 — Fibonacci with Memoization

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Top-Down DP: Fibonacci with automatic memoization via @lru_cache."""
    # Base cases
    if n <= 1:
        return n
    # Recursive case (result is automatically cached by @lru_cache)
    return fib(n - 1) + fib(n - 2)


# --- Manual memo dict version (same idea, more explicit) ---
def fib_manual(n: int, memo: dict = {}) -> int:
    if n in memo:           # ← Cache hit: skip recomputation
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_manual(n - 1, memo) + fib_manual(n - 2, memo)
    return memo[n]


print(fib(50))        # Output: 12586269025 (instant!)
print(fib_manual(50)) # Output: 12586269025
```

**Call Tree After Memoization — each node computed only once:**

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   └── fib(0) → 0
│   │   └── fib(1) → [cache hit ✅]
│   └── fib(2) → [cache hit ✅]
└── fib(3) → [cache hit ✅]
```

**Complexity:**
- ⏱️ Time: `O(n)` — each unique `fib(i)` computed exactly once
- 💾 Space: `O(n)` — cache stores n values + O(n) call stack

---

### 🐍 Example 2 — Climbing Stairs (LeetCode 70)

**Problem:** You're climbing a staircase with `n` steps. You can climb 1 or 2 steps at a time. How many distinct ways can you reach the top?

**Mental Model:**

```
To reach step n, you came from either:
  → step (n-1)  [took 1 step]
  → step (n-2)  [took 2 steps]

∴ ways(n) = ways(n-1) + ways(n-2)   ← This IS Fibonacci!

Base cases:
  ways(1) = 1   (only one way: 1 step)
  ways(2) = 2   (two ways: 1+1 or 2)
```

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def climb_stairs(n: int) -> int:
    """
    LeetCode 70. Climbing Stairs.
    Returns the number of distinct ways to climb n stairs.
    """
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)


print(climb_stairs(10))  # Output: 89
```

---

## 📤 Part 3 — Tabulation (Bottom-Up DP)

### 🪄 The Recipe

```
1. Identify all subproblems and their order (smallest → largest).
2. Create a table (array or 2D array) to store results.
3. Fill the table from the base cases up to the final answer.
4. Return dp[n] (or the relevant cell).
```

> 💡 **Intuition:** Tabulation is DP without recursion. You're filling a grid of answers, and each cell depends only on previously filled cells.

---

### 🐍 Example 1 — Fibonacci with Tabulation

```python
def fib_tabulation(n: int) -> int:
    """Bottom-Up DP: Build Fibonacci answers from the ground up."""
    if n <= 1:
        return n

    # Create a table of size n+1 initialized to 0
    dp = [0] * (n + 1)

    # Fill in the base cases
    dp[0] = 0
    dp[1] = 1

    # Fill from smallest to largest
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fib_tabulation(10))  # Output: 55
```

**Filling the table for n=6:**

```
Index:  0   1   2   3   4   5   6
dp:    [0 | 1 | 1 | 2 | 3 | 5 | 8]
            ↑   ↑
         base cases
```

**Space Optimization** — We only ever look back 2 cells, so we can ditch the array:

```python
def fib_optimized(n: int) -> int:
    """Space-optimized Bottom-Up DP: O(1) space."""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


print(fib_optimized(10))  # Output: 55
```

**Complexity (Optimized):**
- ⏱️ Time: `O(n)`
- 💾 Space: `O(1)` ← Much better than memoization!

---

### 🐍 Example 2 — Unique Paths in a Grid (LeetCode 62)

**Problem:** A robot is in the top-left corner of an `m × n` grid. It can only move **right** or **down**. How many unique paths are there to the bottom-right corner?

**Visual (3×3 grid):**

```
  ┌────┬────┬────┐
  │ S  │    │    │        S = Start (top-left)
  ├────┼────┼────┤        E = End (bottom-right)
  │    │    │    │
  ├────┼────┼────┤
  │    │    │ E  │
  └────┴────┴────┘
```

**Recurrence:** `paths(r, c) = paths(r-1, c) + paths(r, c-1)`

```
The number of ways to reach any cell = ways from the cell above + ways from the cell to the left.
```

```
dp table for m=3, n=3:

  ┌───┬───┬───┐
  │ 1 │ 1 │ 1 │  ← Top row: only one way (keep going right)
  ├───┼───┼───┤
  │ 1 │ 2 │ 3 │
  ├───┼───┼───┤
  │ 1 │ 3 │ 6 │  ← Answer is 6
  └───┴───┴───┘
```

```python
from typing import List


def unique_paths(m: int, n: int) -> int:
    """
    LeetCode 62. Unique Paths.
    Returns the number of unique paths from top-left to bottom-right.
    m = rows, n = columns.
    """
    # Initialize dp grid: all cells start at 0
    dp: List[List[int]] = [[0] * n for _ in range(m)]

    # Base case: first row and first column all have exactly 1 path
    for r in range(m):
        dp[r][0] = 1
    for c in range(n):
        dp[0][c] = 1

    # Fill the rest of the table
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[m - 1][n - 1]


print(unique_paths(3, 3))   # Output: 6
print(unique_paths(3, 7))   # Output: 28
```

**Complexity:**
- ⏱️ Time: `O(m × n)`
- 💾 Space: `O(m × n)` — can be reduced to `O(n)` with a rolling row

---

## 🎒 Part 4 — 0/1 Knapsack: The "Take It or Leave It" Pattern

### 🗺️ The Problem Setup

Imagine you're a thief with a **backpack** that holds at most `W` kg. You have `n` items, each with a **weight** and a **value**. What's the maximum value you can steal?

**The catch: you cannot break items** (0/1 = either take the whole item or leave it).

```
Items:
  Item 1: weight=1, value=1
  Item 2: weight=3, value=4
  Item 3: weight=4, value=5
  Item 4: weight=5, value=7

Knapsack capacity: W = 7

Best choice: Item 2 (w=3, v=4) + Item 3 (w=4, v=5) → total value = 9 ✅
```

---

### 🧠 The Recurrence — The "Take It or Leave It" Decision

For each item `i` with capacity `w`:

```
Option A: LEAVE item i → value = dp[i-1][w]
           (ignore this item; use the best solution from previous items)

Option B: TAKE item i (only if weight[i] <= w)
           → value = value[i] + dp[i-1][w - weight[i]]
           (take this item; add its value to the best solution with remaining capacity)

dp[i][w] = max(Option A, Option B)
```

---

### 🗂️ Filling the DP Table

```
Items: (weight, value) = [(1,1), (3,4), (4,5), (5,7)]
Capacity W = 7

         w=0  w=1  w=2  w=3  w=4  w=5  w=6  w=7
i=0 (—)  [ 0 | 0  | 0  | 0  | 0  | 0  | 0  | 0  ]
i=1 (1,1)[ 0 | 1  | 1  | 1  | 1  | 1  | 1  | 1  ]
i=2 (3,4)[ 0 | 1  | 1  | 4  | 5  | 5  | 5  | 5  ]
i=3 (4,5)[ 0 | 1  | 1  | 4  | 5  | 6  | 6  | 9  ]  ← dp[3][7]=9
i=4 (5,7)[ 0 | 1  | 1  | 4  | 5  | 7  | 8  | 9  ]

Answer: dp[4][7] = 9 ✅
```

---

### 🐍 Implementation

```python
from typing import List


def knapsack_01(
    weights: List[int],
    values: List[int],
    capacity: int
) -> int:
    """
    Classic 0/1 Knapsack — Bottom-Up DP.
    Returns the maximum value achievable without exceeding `capacity`.
    """
    n = len(weights)
    # dp[i][w] = max value using first i items with capacity w
    dp: List[List[int]] = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_weight = weights[i - 1]
        item_value = values[i - 1]

        for w in range(capacity + 1):
            # Option A: Leave item i
            leave = dp[i - 1][w]

            # Option B: Take item i (only if it fits)
            take = 0
            if item_weight <= w:
                take = item_value + dp[i - 1][w - item_weight]

            dp[i][w] = max(leave, take)

    return dp[n][capacity]


# --- Test ---
weights = [1, 3, 4, 5]
values  = [1, 4, 5, 7]
capacity = 7

print(knapsack_01(weights, values, capacity))  # Output: 9
```

**Complexity:**
- ⏱️ Time: `O(n × W)` — fill every cell of the n×W table
- 💾 Space: `O(n × W)` — the dp table (can be optimized to `O(W)`)

---

### 🏎️ Space-Optimized 0/1 Knapsack — `O(W)` Space

Since `dp[i][w]` only depends on `dp[i-1][...]`, we can use a single 1D array, but we **must iterate `w` in reverse** to avoid using updated values from the current row.

```python
def knapsack_01_optimized(
    weights: List[int],
    values: List[int],
    capacity: int
) -> int:
    """Space-optimized 0/1 Knapsack: O(W) space."""
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # Traverse BACKWARDS to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


print(knapsack_01_optimized(weights, values, capacity))  # Output: 9
```

> ⚠️ **Why iterate backwards?** If we iterated forward, `dp[w - weight[i]]` might already have been updated in this same pass (i.e., we'd be using the item twice, turning it into an Unbounded Knapsack).

---

## 🧵 Part 5 — Longest Common Subsequence (LCS)

### 🗺️ The Problem

**Problem:** Given two strings `s1` and `s2`, find the length of their **longest common subsequence** (LCS).

> A **subsequence** is a sequence derived by deleting some (or no) characters without changing the order. It doesn't need to be contiguous.

```
s1 = "ABCBDAB"
s2 = "BDCAB"

LCS = "BCAB" or "BDAB"  (length = 4) ✅

Not a subsequence: "BAC" (order violated in s1)
```

**Real-world uses:**
- 🧬 **DNA sequence alignment** (bioinformatics)
- 📄 **`git diff`** — comparing file versions
- 🔍 **Spell checkers** — finding edit distance

---

### 🧠 The Recurrence

```
If s1[i] == s2[j]:
    dp[i][j] = 1 + dp[i-1][j-1]   ← Both characters match → extend the LCS

If s1[i] != s2[j]:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])  ← Skip one character from either string
```

---

### 🗂️ Filling the DP Table

```
s1 = "ABCB",  s2 = "BCB"

       ""  B   C   B
  ""  [ 0 | 0 | 0 | 0 ]
  A   [ 0 | 0 | 0 | 0 ]
  B   [ 0 | 1 | 1 | 1 ]
  C   [ 0 | 1 | 2 | 2 ]
  B   [ 0 | 1 | 2 | 3 ]  ← LCS length = 3

LCS = "BCB" ✅
```

---

### 🐍 Implementation

```python
def lcs(s1: str, s2: str) -> int:
    """
    Longest Common Subsequence — Bottom-Up DP.
    Returns the length of the LCS of s1 and s2.
    """
    m, n = len(s1), len(s2)
    # dp[i][j] = LCS length of s1[:i] and s2[:j]
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # Characters match → extend the common subsequence
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # No match → take the best of skipping either character
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(s1: str, s2: str) -> str:
    """Reconstruct the actual LCS string by backtracking through dp table."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to reconstruct the LCS
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])   # This character is in the LCS
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1                      # Move up
        else:
            j -= 1                      # Move left

    return ''.join(reversed(result))


# --- Test ---
print(lcs("ABCBDAB", "BDCAB"))          # Output: 4
print(lcs_string("ABCBDAB", "BDCAB"))   # Output: "BCAB" or "BDAB"
```

**Complexity:**
- ⏱️ Time: `O(m × n)` — fill every cell
- 💾 Space: `O(m × n)` — the dp table (can be reduced to `O(n)`)

---

## 🗂️ Part 6 — The DP Pattern Encyclopedia

### 🔑 Classic DP Problem Categories

| Category | Problems | Key Recurrence Shape |
|---|---|---|
| **Linear DP** | Fibonacci, Climbing Stairs, House Robber | `dp[i] = f(dp[i-1], dp[i-2])` |
| **Grid DP** | Unique Paths, Minimum Path Sum | `dp[r][c] = f(dp[r-1][c], dp[r][c-1])` |
| **Knapsack DP** | 0/1 Knapsack, Subset Sum, Coin Change | `dp[i][w] = max(leave, take)` |
| **Sequence DP** | LCS, LIS, Edit Distance | `dp[i][j] = f(match/mismatch)` |
| **Interval DP** | Burst Balloons, Matrix Chain Multiply | `dp[i][j] = min/max over split point k` |
| **Tree DP** | House Robber III, Diameter of Tree | Recursion on children, two states |

---

### 🧹 Memoization vs Tabulation — When to Use Which?

| Criteria | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|---|---|---|
| **Ease of coding** | ✅ Easier (convert recursion + add cache) | ❌ Harder (must work out fill order) |
| **Solving only needed parts** | ✅ Only computes required subproblems | ❌ Always fills entire table |
| **Stack overflow risk** | ❌ Yes, for very large `n` | ✅ No recursion → no stack risk |
| **Space optimization** | ❌ Harder | ✅ Easy (rolling array trick) |
| **Interview preference** | Good for explanation | Good for optimized solution |

> 💡 **Strategy in interviews:** Start with memoization (easier to derive), then convert to tabulation for optimization if time allows.

---

## 📊 Complexity Summary

| Problem | Time | Space (Standard) | Space (Optimized) |
|---|---|---|---|
| Fibonacci (Memoized) | `O(n)` | `O(n)` | `O(1)` with tabulation |
| Climbing Stairs | `O(n)` | `O(n)` | `O(1)` |
| Unique Paths | `O(m×n)` | `O(m×n)` | `O(n)` rolling row |
| 0/1 Knapsack | `O(n×W)` | `O(n×W)` | `O(W)` reverse iteration |
| LCS | `O(m×n)` | `O(m×n)` | `O(n)` rolling row |
| Coin Change | `O(n×amount)` | `O(amount)` | Already optimal |
| Edit Distance | `O(m×n)` | `O(m×n)` | `O(n)` rolling row |

---

## 🎯 LeetCode Practice Problems

### 🟢 Easy — Build the Intuition

| # | Problem | Pattern |
|---|---|---|
| 509 | Fibonacci Number | Linear DP |
| 70 | Climbing Stairs | Linear DP (disguised Fibonacci) |
| 746 | Min Cost Climbing Stairs | Linear DP with choice |
| 198 | House Robber | Linear DP (skip or take) |
| 338 | Counting Bits | Linear DP with bit trick |

### 🟡 Medium — The Core Patterns

| # | Problem | Pattern |
|---|---|---|
| 62 | Unique Paths | Grid DP |
| 64 | Minimum Path Sum | Grid DP |
| 322 | Coin Change | Unbounded Knapsack |
| 416 | Partition Equal Subset Sum | 0/1 Knapsack |
| 1143 | Longest Common Subsequence | Sequence DP |
| 300 | Longest Increasing Subsequence | Sequence DP |
| 139 | Word Break | Linear DP + hashing |
| 5 | Longest Palindromic Substring | Interval DP / expand around center |
| 213 | House Robber II | Circular Linear DP |
| 91 | Decode Ways | Linear DP |

### 🔴 Hard — The Full Challenge

| # | Problem | Pattern |
|---|---|---|
| 72 | Edit Distance | Sequence DP (LCS sibling) |
| 312 | Burst Balloons | Interval DP |
| 10 | Regular Expression Matching | Sequence DP |
| 115 | Distinct Subsequences | Sequence DP |
| 188 | Best Time to Buy Stock IV | State Machine DP |
| 123 | Best Time to Buy Stock III | State Machine DP |

---

## 🚀 The "3-Step" DP Problem-Solving Framework

Before writing any code, answer these three questions:

```
STEP 1 — DEFINE THE SUBPROBLEM
   └── "What does dp[i] (or dp[i][j]) represent?"
       Write it out in plain English.
       Example: "dp[i] = the max profit using the first i items
                          with a bag capacity of i."

STEP 2 — WRITE THE RECURRENCE
   └── "How is dp[i] related to smaller subproblems?"
       Think about the last decision made.
       Example: "dp[i][w] = max(leave item i, take item i)"

STEP 3 — IDENTIFY THE BASE CASES
   └── "What are the smallest subproblems I can answer directly?"
       Example: dp[0][w] = 0 for all w (zero items → zero value)
                dp[i][0] = 0 for all i (zero capacity → zero value)
```

> ✏️ **Pro Tip:** Draw the DP table on paper before coding. Fill in a few cells manually. Once you see the pattern, translating it to code becomes mechanical.

---

## 🔗 The DP ↔ Backtracking Connection

DP and Backtracking solve similar problems — but with a key difference:

```
BACKTRACKING                         DYNAMIC PROGRAMMING
────────────────────────────────     ────────────────────────────────
Explores all possibilities           Remembers already-solved parts
Generates EXACT solutions            Generates OPTIMAL values
Good when: constraints are tight     Good when: optimal value is enough
           and we need all answers               and n is large

Example: "Find all arrangements"     Example: "Find the MAX value"

Time: Exponential in worst case      Time: Polynomial (n×W, m×n, etc.)
```

> 💡 **When you see "minimum", "maximum", "count the number of ways", or "is it possible?" — think DP first.**

---

> 📝 **Previous:** [01-Recursion&Backtracking.md](./01-Recursion%26Backtracking.md) — The foundation of exploring decision trees.
> 📝 **Next Up:** [03-Tries&Segment-Trees.md](./03-Tries%26Segment-Trees.md) — Prefix matching for autocomplete and range queries.