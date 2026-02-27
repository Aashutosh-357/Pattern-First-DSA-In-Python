# 🔭 Binary Search: The Art of Intelligent Elimination

![Binary Search](https://img.shields.io/badge/Topic-Binary_Search-blueviolet?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)
![Time](https://img.shields.io/badge/Study_Time-3_Hours-orange?style=for-the-badge)

> **"Don't search everything — eliminate half."**
>
> If Linear Search is a librarian reading every single book title one by one, **Binary Search** is a genius who opens the book *right in the middle* first and instantly decides which half to throw away. It is the most elegant application of the **Divide & Conquer** mindset.

---

## 🧠 1. The Blueprint (Concept & Memory)

### 📖 The Analogy — The Dictionary Game

Imagine you want to find the word **"Python"** in a physical dictionary.

Would you start from **page 1** and read every word? Of course not! You:
1. **Open the middle** of the dictionary → land on "M"
2. "Python" comes *after* "M" → **throw away the entire left half**
3. Open the middle of the remaining right half → land on "S"
4. "Python" comes *before* "S" → **throw away the right half**
5. Repeat until you find it.

This is **exactly** what Binary Search does — but on a sorted array.

> **🔑 The Golden Rule:** Binary Search only works on **sorted** data. The ability to say *"it must be in this half"* depends entirely on order.

---

### 👁️ Visual Dry Run

**Target:** Find `23` in the array `[2, 5, 8, 12, 16, 23, 38, 45, 56, 72]`

```
Array:   [ 2,  5,  8, 12, 16, 23, 38, 45, 56, 72 ]
Index:     0   1   2   3   4   5   6   7   8   9
           L                   M                   R

Step 1: low=0, high=9 → mid = (0+9)//2 = 4
        arr[4] = 16 → 16 < 23 → target is in RIGHT half
        low = mid + 1 = 5

────────────────────────────────────────────────────
Array:   [ 2,  5,  8, 12, 16, 23, 38, 45, 56, 72 ]
                             L    M           R
Step 2: low=5, high=9 → mid = (5+9)//2 = 7
        arr[7] = 45 → 45 > 23 → target is in LEFT half
        high = mid - 1 = 6

────────────────────────────────────────────────────
Array:   [ 2,  5,  8, 12, 16, 23, 38, 45, 56, 72 ]
                             L  M  R
Step 3: low=5, high=6 → mid = (5+6)//2 = 5
        arr[5] = 23 → ✅ FOUND at index 5!
```

**Result:** `3 comparisons` instead of `6` (Linear Search worst case). On `1,000,000` elements, Binary Search takes only **~20 steps**. Linear Search would take **1,000,000**.

---

### ⚡ Why Binary Search? — The Logarithmic Superpower

| Array Size (n) | Linear Search | Binary Search |
|:--------------:|:-------------:|:-------------:|
| 8              | 8 steps       | 3 steps       |
| 1,024          | 1,024 steps   | 10 steps      |
| 1,000,000      | 1,000,000 steps | 20 steps   |
| 1,000,000,000  | 1B steps      | 30 steps      |

> Binary Search reduces the problem in **half** at every step → **O(log n)** time complexity.
> `log₂(1,000,000) ≈ 20` — twenty steps to search a million items.

---

## ⚙️ 2. The Operations — Standard Binary Search

### 🔑 The Core Template (Iterative)

The **Iterative** approach is preferred in interviews — no recursion stack overhead.

```python
from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    🔭 Standard Binary Search — Iterative
    Finds the INDEX of target in a sorted array.
    Returns -1 if not found.
    Time:  O(log n) | Space: O(1)
    """
    low: int = 0
    high: int = len(arr) - 1

    while low <= high:              # ← Note: <= not just <
        mid: int = low + (high - low) // 2  # ← Safe mid (avoids int overflow)

        if arr[mid] == target:
            return mid              # ✅ Found!
        elif arr[mid] < target:
            low = mid + 1           # Target is in RIGHT half
        else:
            high = mid - 1          # Target is in LEFT half

    return -1                       # ❌ Not found
```

> **⚠️ Common Pitfall:** Always use `mid = low + (high - low) // 2` instead of `(low + high) // 2`.
> In languages with fixed integer sizes (C++, Java), `low + high` can **overflow**. Python handles big ints gracefully, but the safe form is a professional habit.

---

### 🔄 The Recursive Version

```python
def binary_search_recursive(arr: List[int], target: int,
                             low: int, high: int) -> int:
    """
    🔄 Recursive Binary Search
    Time:  O(log n) | Space: O(log n) — call stack
    """
    if low > high:
        return -1               # Base case: search space exhausted

    mid: int = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
```

### 🧪 Quick Test

```python
nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]

print(binary_search(nums, 23))   # → 5
print(binary_search(nums, 100))  # → -1

# Recursive approach
print(binary_search_recursive(nums, 8, 0, len(nums) - 1))   # → 2
```

---

### 🧮 Complexity: Standard Binary Search

| Metric            | Value       | Why?                                     |
|:------------------|:-----------:|:-----------------------------------------|
| ⏱️ Time (Best)    | **O(1)**    | Target is the first `mid`                |
| ⏱️ Time (Average) | **O(log n)**| Halves the search space each iteration   |
| ⏱️ Time (Worst)   | **O(log n)**| Reaches the last single element          |
| 💾 Space (Iter)   | **O(1)**    | Only 3 pointers: `low`, `mid`, `high`    |
| 💾 Space (Recur)  | **O(log n)**| Recursion call stack depth = log n       |

---

## 🌀 3. Advanced Variants — Finding the Boundary

Standard Binary Search finds *if* something exists. Advanced variants find *where* something begins or ends. This is the real power behind **Optimization Problems**.

### 🎯 Variant 1: `lower_bound` — First Position of Target

> *"Find the leftmost index where `arr[index] >= target`"*

```python
def lower_bound(arr: List[int], target: int) -> int:
    """
    📍 Lower Bound — First occurrence of target (or insertion point).
    Returns the LEFTMOST index where arr[index] >= target.
    Time: O(log n) | Space: O(1)
    """
    low, high = 0, len(arr)  # Note: high = len(arr) for insertion-point logic
    result = len(arr)        # Default: target is beyond all elements

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:
            result = mid        # ← Potential answer, but keep going LEFT
            high = mid
        else:
            low = mid + 1

    return result
```

**Dry Run:** `arr = [1, 2, 2, 2, 4, 5]`, `target = 2`
```
Step 1: low=0, high=6, mid=3 → arr[3]=2 >= 2 → result=3, high=3
Step 2: low=0, high=3, mid=1 → arr[1]=2 >= 2 → result=1, high=1
Step 3: low=0, high=1, mid=0 → arr[0]=1 < 2  → low=1
Step 4: low=1 == high=1      → STOP
Result: 1 ✅ (first position of 2)
```

---

### 🎯 Variant 2: `upper_bound` — Position After Last Target

> *"Find the leftmost index where `arr[index] > target`"* — i.e., one past the last occurrence.

```python
def upper_bound(arr: List[int], target: int) -> int:
    """
    📍 Upper Bound — One past the last occurrence of target.
    Useful to count occurrences: upper_bound - lower_bound.
    Time: O(log n) | Space: O(1)
    """
    low, high = 0, len(arr)
    result = len(arr)

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            result = mid
            high = mid
        else:
            low = mid + 1   # ← arr[mid] <= target, push RIGHT

    return result
```

### 🧪 Count Occurrences Using Both Bounds

```python
def count_occurrences(arr: List[int], target: int) -> int:
    """Count how many times target appears in sorted arr."""
    return upper_bound(arr, target) - lower_bound(arr, target)

arr = [1, 2, 2, 2, 4, 5]
print(count_occurrences(arr, 2))   # → 3
print(count_occurrences(arr, 6))   # → 0
```

---

### 🎯 Variant 3: Search in Rotated Sorted Array

> *"An array like `[4, 5, 6, 7, 0, 1, 2]` was once sorted, then rotated. Find the target."*
>
> Real interview classic: **LeetCode #33**

```
Original:  [0, 1, 2, 4, 5, 6, 7]
Rotated:   [4, 5, 6, 7, 0, 1, 2]
                   ↑
              rotation point
```

**Key Insight:** After a rotation, at least **one half** of the array is always sorted. We check *which half* is sorted, then decide where the target can be.

```python
def search_rotated(arr: List[int], target: int) -> int:
    """
    🔄 Binary Search on a Rotated Sorted Array.
    LeetCode #33. Time: O(log n) | Space: O(1)
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        # Check if LEFT half is sorted
        if arr[low] <= arr[mid]:
            # Is target in the sorted left half?
            if arr[low] <= target < arr[mid]:
                high = mid - 1   # Search left
            else:
                low = mid + 1    # Search right
        else:
            # RIGHT half must be sorted
            # Is target in the sorted right half?
            if arr[mid] < target <= arr[high]:
                low = mid + 1    # Search right
            else:
                high = mid - 1   # Search left

    return -1
```

**Dry Run:** `arr = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`
```
Step 1: low=0, high=6, mid=3 → arr[3]=7 ≠ 0
        Left half [4,5,6,7] is sorted (arr[0]=4 <= arr[3]=7)
        Is 0 in [4..7)? NO → low = 4

Step 2: low=4, high=6, mid=5 → arr[5]=1 ≠ 0
        Left half [0,1] is NOT sorted relative check fails
        Right half [1,2] is sorted (arr[5]=1 <= arr[6]=2)
        Is 0 in (1..2]? NO → high = 4

Step 3: low=4, high=4, mid=4 → arr[4]=0 == 0 ✅ FOUND at index 4!
```

---

## 🚀 4. Binary Search on Answer Space (Optimization)

This is the **most powerful** application of Binary Search — you're not searching for a value *in* an array; you're searching for the **optimal answer** in a range of possible values.

> **The Trick:** Instead of asking *"Is X in the array?"*, ask *"Is it feasible to achieve X?"*

### 🧩 The Pattern Template

```python
def solve_optimization_problem(data) -> int:
    """
    🎯 Binary Search on Answer Space Template
    Use when: "minimize/maximize X such that condition is met"
    """
    low = minimum_possible_answer
    high = maximum_possible_answer
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if is_feasible(mid, data):   # ← Custom check function
            result = mid             # ← Record potential answer
            high = mid - 1           # ← Try to minimize (or low = mid+1 to maximize)
        else:
            low = mid + 1

    return result
```

---

### 🏋️ Example: Koko Eating Bananas (LeetCode #875)

> *Koko has `piles` of bananas. She has `h` hours. Find the minimum eating speed `k` (bananas/hour) such that she finishes all bananas within `h` hours.*

**Answer Space:** `k` ranges from `1` (slowest) to `max(piles)` (fastest).

```python
import math

def min_eating_speed(piles: List[int], h: int) -> int:
    """
    🍌 Koko Eating Bananas — Binary Search on Answer Space
    LeetCode #875. Time: O(n log m) | Space: O(1)
    where m = max(piles)
    """
    def can_finish(speed: int) -> bool:
        """Can Koko finish all piles at this speed within h hours?"""
        hours_needed = sum(math.ceil(pile / speed) for pile in piles)
        return hours_needed <= h

    low: int = 1
    high: int = max(piles)
    result: int = high

    while low <= high:
        mid = low + (high - low) // 2

        if can_finish(mid):
            result = mid        # ← Valid speed, try SLOWER (minimize)
            high = mid - 1
        else:
            low = mid + 1       # ← Too slow, try FASTER

    return result

# Test
piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h))   # → 4
```

---

### 🏗️ Example: Allocate Books (Classic Interview Problem)

> *Given `pages[]` representing books and `m` students, allocate books such that the maximum pages assigned to any student is **minimized**.*

```python
def allocate_books(pages: List[int], m: int) -> int:
    """
    📚 Book Allocation — Binary Search on Answer Space
    Time: O(n log(sum)) | Space: O(1)
    """
    def is_feasible(max_pages: int) -> bool:
        """Can we allocate with no student getting more than max_pages?"""
        students_needed = 1
        current_pages = 0

        for page in pages:
            if page > max_pages:
                return False    # Single book exceeds limit — impossible
            if current_pages + page > max_pages:
                students_needed += 1
                current_pages = page
                if students_needed > m:
                    return False
            else:
                current_pages += page

        return True

    low: int = max(pages)          # Min possible: largest single book
    high: int = sum(pages)         # Max possible: one student gets everything
    result: int = high

    while low <= high:
        mid = low + (high - low) // 2

        if is_feasible(mid):
            result = mid
            high = mid - 1         # Try to minimize max pages
        else:
            low = mid + 1

    return result

# Test
pages = [12, 34, 67, 90]
m = 2
print(allocate_books(pages, m))   # → 113
```

---

## 🎯 5. The Engineer's Choice

### ✅ **USE Binary Search when:**
- 📊 Data is **sorted** (or can be reasoned about monotonically)
- 🎯 You need to find an exact element in **O(log n)**
- 📐 You need to find the **first/last** occurrence of a value
- 🏋️ You're solving **min/max optimization** problems ("minimize the maximum..." or "find the smallest X such that...")
- 🔄 Searching in a **rotated/modified sorted** structure
- 🌐 The **answer space** has a monotonic property (feasible vs. not feasible)

### ❌ **AVOID Binary Search when:**
- 🔀 Data is **unsorted** and sorting is too expensive
- 🔗 Data is in a **Linked List** (no O(1) random access — use two pointers instead)
- 📦 The dataset is **tiny** (n < 10) — linear search is fine and simpler
- 🌊 You need to search **all** elements, not just find one

---

## 📈 6. Complexity Full Summary

| Variant                      | Time           | Space    |
|:-----------------------------|:--------------:|:--------:|
| Standard Binary Search (Iter)| O(log n) ⚡    | O(1) ✅  |
| Standard Binary Search (Rec) | O(log n) ⚡    | O(log n) |
| Lower Bound                  | O(log n) ⚡    | O(1) ✅  |
| Upper Bound                  | O(log n) ⚡    | O(1) ✅  |
| Search in Rotated Array      | O(log n) ⚡    | O(1) ✅  |
| Binary Search on Answer Space| O(n log m) ⚡ | O(1) ✅  |

> `m` = size of answer space (e.g., `max(piles)`, `sum(pages)`, etc.)

---

## 🌟 7. Real-World Applications

### 🖥️ Git Bisect — Finding the Bug Commit
```
# Git uses binary search to find which commit introduced a bug!
# 100 commits → finds the bad one in ~7 steps (log₂ 100 ≈ 7)

$ git bisect start
$ git bisect bad             # Current commit is bad
$ git bisect good <hash>     # This old commit was fine
# Git automatically checks out the middle commit each time
```

### 📦 Database Indexing
```
B-Tree Index: Binary search-like traversal
Finding "user_id = 5001" in 10,000,000 rows:
Linear scan:  10,000,000 reads
B-Tree index: ~24 reads (log₂ 10,000,000 ≈ 24)
```

### 🎮 Guess the Number Game (Python)
```python
import random

def guess_number_game() -> None:
    """🎮 The computer uses Binary Search to always win."""
    secret = random.randint(1, 100)
    low, high = 1, 100
    attempts = 0

    print("🎮 I'm thinking of a number between 1 and 100...")

    while low <= high:
        guess = low + (high - low) // 2
        attempts += 1
        print(f"   Attempt {attempts}: Guessing {guess}...")

        if guess == secret:
            print(f"   ✅ Found {secret} in {attempts} attempts! (Max possible: 7)")
            return
        elif guess < secret:
            low = guess + 1
        else:
            high = guess - 1
```

---

## 🚀 Next Adventure

> **"From the art of elimination to the science of organization."**

Binary Search showed you the power of **divide & conquer thinking** — cutting problems in half. Now, what if the *data itself* could self-organize to always be efficiently searchable?

**Coming Next:** 🌳 **Trees & BST** — Where every node makes a binary decision.

---

*Happy Coding! 🎉*