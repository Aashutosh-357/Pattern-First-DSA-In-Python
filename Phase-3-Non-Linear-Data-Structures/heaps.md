# 🏔️ Heaps & Priority Queues: Always Know Your Next Best Option

![Heaps](https://img.shields.io/badge/Topic-Heaps_%26_Priority_Queues-blueviolet?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Intermediate_to_Advanced-orange?style=for-the-badge)
![Time](https://img.shields.io/badge/Study_Time-4_Hours-red?style=for-the-badge)
![DE Relevance](https://img.shields.io/badge/DE_Relevance-🔥_Critical-brightgreen?style=for-the-badge)

> **"A Heap doesn't sort everything. It just always knows what comes next."**
>
> A Heap is the data structure that powers your task scheduler, your hospital triage system, your Dijkstra shortest-path algorithm, and your real-time analytics "Top K" dashboards. Whenever you need to repeatedly and efficiently ask *"What is the most important item right now?"* — you reach for a Heap.

---

## 🧠 1. The Blueprint — What Is a Heap?

### 📖 The Analogy — The Hospital Emergency Room

Imagine a hospital emergency room. Patients arrive at random times with varying severity:
- A person with a **sprained ankle** arrives first.
- Then a person with a **broken arm** arrives.
- Then a person in **cardiac arrest** arrives.

A regular queue (FIFO) would treat the sprained ankle first — which is dangerous and wrong. The ER uses a **triage system**: the **most critical patient is always seen first**, regardless of arrival order.

A **Max-Heap** is exactly that triage system:
- New patients (elements) arrive at any time.
- The doctor (you) always pulls the **highest priority** patient next.
- Everything else waits, re-organized automatically behind the scenes.

```
     ER Triage (Max-Heap)
     
     Cardiac Arrest (9/10) ← Always at the top (highest priority)
          /              \
  Broken Arm (6/10)    Broken Leg (5/10)
       /     \
Sprain (3/10) Cold (2/10)

→ No matter who walks in, the worst case is ALWAYS treated first.
```

---

### 🔑 The Two Core Rules of a Heap

A Heap is a **Complete Binary Tree** that satisfies the **Heap Property**:

```
                ┌──────────────────────────────────────┐
                │  RULE 1: SHAPE PROPERTY               │
                │  Always a COMPLETE Binary Tree.        │
                │  Nodes fill level by level,            │
                │  left to right. No gaps in the middle. │
                └──────────────────────────────────────┘

                ┌──────────────────────────────────────┐
                │  RULE 2: HEAP PROPERTY                │
                │  For a MAX-HEAP:                      │
                │    Every parent ≥ its children.       │
                │  For a MIN-HEAP:                      │
                │    Every parent ≤ its children.       │
                └──────────────────────────────────────┘
```

> ⚠️ **Critical Misconception:** A Heap is **NOT sorted**. The only guarantee is the root is the max (or min). Siblings have no defined order relative to each other.

---

### 👁️ Min-Heap vs Max-Heap — Side by Side

```
        MAX-HEAP                   MIN-HEAP
        
           16                         1
          /  \                       / \
        14    10                    2    3
       /  \  /  \                 /  \  / \
      8   7  9   3               4    5  6  7

  ✅ 16 ≥ 14, 10            ✅ 1 ≤ 2, 3
  ✅ 14 ≥ 8, 7              ✅ 2 ≤ 4, 5
  ✅ 10 ≥ 9, 3              ✅ 3 ≤ 6, 7

  Root = MAXIMUM (16)        Root = MINIMUM (1)
  Use: "Give me the best"    Use: "Give me the cheapest/nearest"
```

---

### 🗃️ The Array Trick — How Heaps Are Actually Stored

A heap is conceptually a tree, but **stored as a flat array** in memory (no pointers needed!). The positions encode the parent-child relationships with simple math:

```
        MAX-HEAP Tree:
               16          ← index 0
              /  \
            14    10       ← index 1, 2
           /  \  /  \
          8   7  9   3     ← index 3, 4, 5, 6

        Array representation:
        Index:  [0]  [1]  [2]  [3]  [4]  [5]  [6]
        Value:  [16]  [14] [10]  [8]  [7]  [9]  [3]
```

| Relationship | Formula |
|:-------------|:--------|
| **Parent** of index `i` | `(i - 1) // 2` |
| **Left Child** of index `i` | `2 * i + 1` |
| **Right Child** of index `i` | `2 * i + 2` |

```
Verify: Parent of index 3 (value=8)?
  → (3 - 1) // 2 = 1 → index 1 → value=14 ✅

Left child of index 1 (value=14)?
  → 2*1 + 1 = 3 → index 3 → value=8 ✅
```

---

## 🐍 2. Python's `heapq` — The Built-in Tool

Python's standard library provides `heapq`, which implements a **Min-Heap**. Understanding this is the first step to solving heap problems in interviews.

```python
import heapq
from typing import List

# ─────────────────────────────────────────────────────────────────
# THE BASICS
# ─────────────────────────────────────────────────────────────────

# heapq always gives you a MIN-HEAP
min_heap: List[int] = []

heapq.heappush(min_heap, 5)   # Push 5 → heap: [5]
heapq.heappush(min_heap, 1)   # Push 1 → heap: [1, 5]
heapq.heappush(min_heap, 8)   # Push 8 → heap: [1, 5, 8]
heapq.heappush(min_heap, 3)   # Push 3 → heap: [1, 3, 8, 5]

print(min_heap[0])            # → 1  (Peek: always the MINIMUM, O(1))
print(heapq.heappop(min_heap))# → 1  (Pop minimum, O(log n))
print(heapq.heappop(min_heap))# → 3
print(heapq.heappop(min_heap))# → 5
print(heapq.heappop(min_heap))# → 8

# ─────────────────────────────────────────────────────────────────
# HEAPIFY — Build a heap from an existing list in O(n) time
# ─────────────────────────────────────────────────────────────────
nums: List[int] = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(nums)           # Rearranges IN-PLACE. O(n) — not O(n log n)!
print(nums[0])                # → 1 (minimum is now at the front)

# ─────────────────────────────────────────────────────────────────
# MAX-HEAP TRICK — negate the values!
# Python only has min-heap, so we store -value to simulate max-heap
# ─────────────────────────────────────────────────────────────────
max_heap: List[int] = []

heapq.heappush(max_heap, -5)  # Store -5 to represent 5
heapq.heappush(max_heap, -1)  # Store -1 to represent 1
heapq.heappush(max_heap, -8)  # Store -8 to represent 8

# Peek at max:
print(-max_heap[0])           # → 8  (negate back to get real value)

# Pop max:
print(-heapq.heappop(max_heap))  # → 8
print(-heapq.heappop(max_heap))  # → 5
```

### 📐 Complexity Reference

| Operation | Time | Note |
|:----------|:----:|:-----|
| `heappush` | O(log n) | Sifts up to restore heap property |
| `heappop` | O(log n) | Removes root; sifts down |
| `heapify` | **O(n)** | Smarter than n × heappush |
| Peek (`heap[0]`) | **O(1)** | Root is always at index 0 |
| Search | O(n) | Heaps are NOT for searching |

---

## ⚙️ 3. Core Heap Operations — Under the Hood

Understanding *why* heap operations work is what separates someone who memorizes from someone who *thinks*.

### 🔺 Push (Sift Up)

When you add a new element, it goes to the **end of the array** (maintaining the shape property). Then it "bubbles up" by repeatedly swapping with its parent until the heap property is restored.

**Dry Run — Push `15` into a Min-Heap:**
```
BEFORE push:
Array: [1, 3, 8, 5]
Tree:
        1
       / \
      3    8
     /
    5

Step 1: Append 15 at end
Array: [1, 3, 8, 5, 15]
        1
       / \
      3    8
     / \
    5  15

Step 2: Compare 15 with parent (index 1 = value 3).
        15 > 3 → Min-Heap → No swap needed. ✅ (15 is bigger, stays below 3)

FINAL: [1, 3, 8, 5, 15] — no changes needed since 15 > parent.
```

**Dry Run — Push `2` into the same Min-Heap:**
```
Step 1: Append 2 at end → Array: [1, 3, 8, 5, 15, 2]
                                      1
                                     / \
                                    3    8
                                   / \ /
                                  5 15 2

Step 2: Compare 2 with parent at index (5-1)//2 = 2 → value 8.
        2 < 8 → SWAP! → Array: [1, 3, 2, 5, 15, 8]

Step 3: Compare 2 (now at index 2) with parent at (2-1)//2 = 0 → value 1.
        2 > 1 → Min-Heap satisfied. STOP. ✅

FINAL: [1, 3, 2, 5, 15, 8]
            1
           / \
          3    2    ← 2 bubbled up correctly!
         / \ /
        5 15 8
```

---

### 🔻 Pop (Sift Down)

When you remove the root (the min/max), you:
1. **Swap the root with the last element** (to maintain shape).
2. **Remove the last element** (the old root is now gone).
3. **Sift down** the new root — swap it with its smallest (min-heap) child until heap property is restored.

**Dry Run — Pop from Min-Heap `[1, 3, 2, 5, 15, 8]`:**
```
Step 1: Swap root (1) with last element (8).
        Array: [8, 3, 2, 5, 15, 1]
        Remove last → Array: [8, 3, 2, 5, 15]
        We popped: 1 ✅

Step 2: Sift down 8 from index 0.
        Children: left=3 (idx 1), right=2 (idx 2).
        Smallest child = 2. 8 > 2 → SWAP.
        Array: [2, 3, 8, 5, 15]

Step 3: 8 is now at index 2. Children: left=idx 5 (doesn't exist).
        No children. STOP. ✅

FINAL: [2, 3, 8, 5, 15]
           2
          / \
         3    8
        / \
       5  15
```

---

## 🏗️ 4. Building a Heap from Scratch (The Python Way)

```python
import heapq
from typing import List

# ─────────────────────────────────────────────
# MIN-HEAP from scratch
# ─────────────────────────────────────────────
class MinHeap:
    """
    A clean Min-Heap wrapper using Python's heapq.
    heapq is the engine; this class is the clean interface.
    """
    def __init__(self) -> None:
        self._data: List[int] = []

    def push(self, val: int) -> None:
        heapq.heappush(self._data, val)

    def pop(self) -> int:
        """Remove and return the minimum element. O(log n)"""
        return heapq.heappop(self._data)

    def peek(self) -> int:
        """Return minimum without removing. O(1)"""
        return self._data[0]

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return bool(self._data)


# ─────────────────────────────────────────────
# MAX-HEAP from scratch (using negation trick)
# ─────────────────────────────────────────────
class MaxHeap:
    """
    A Max-Heap built on top of Python's min-heap.
    We negate values on push and un-negate on pop/peek.
    """
    def __init__(self) -> None:
        self._data: List[int] = []

    def push(self, val: int) -> None:
        heapq.heappush(self._data, -val)   # Store as negative

    def pop(self) -> int:
        """Remove and return the MAXIMUM element. O(log n)"""
        return -heapq.heappop(self._data)  # Negate back

    def peek(self) -> int:
        """Return maximum without removing. O(1)"""
        return -self._data[0]              # Negate back

    def __len__(self) -> int:
        return len(self._data)


# ──── Quick Test ────
mh = MaxHeap()
for val in [5, 1, 8, 3, 9, 2]:
    mh.push(val)

while mh:
    print(mh.pop(), end=" ")  # → 9 8 5 3 2 1 (sorted descending!) ✅
```

---

## 🧩 5. Classic Heap Patterns — The Interview Playbook

---

### 🥇 Pattern 1: Top K Elements

> **"Find the K largest (or smallest) elements in a dataset."**

This is the **most common** heap interview pattern. It appears in:
- Real-time analytics dashboards (Top K trending products)
- Log processing (Top K error types)
- Recommendation systems (Top K similar items)

**The Trick:** To find **K largest**, use a **Min-Heap of size K**.
- Keep pushing. When heap size exceeds K, pop the minimum.
- At the end, the heap contains exactly the K largest elements.

```
Why Min-Heap for K LARGEST?
The min-heap's root is always the SMALLEST of our "top K" candidates.
When a new element arrives that's bigger than the smallest in our K-set,
it evicts the smallest. This guarantees we always hold the K largest seen so far.
```

#### 🔍 Problem: K Largest Elements in Array — LeetCode #215 (variant)

```python
import heapq
from typing import List

def find_k_largest(nums: List[int], k: int) -> List[int]:
    """
    🥇 Find K Largest Elements using a Min-Heap of size K.
    Time: O(n log k)  ← much better than O(n log n) sorting for small k
    Space: O(k)       ← the heap never grows beyond k elements
    """
    min_heap: List[int] = []

    for num in nums:
        heapq.heappush(min_heap, num)           # Push every element

        if len(min_heap) > k:
            heapq.heappop(min_heap)             # Evict the smallest

    # min_heap now contains exactly the K largest elements
    return sorted(min_heap, reverse=True)       # Optional: sort for clean output


# ──── Dry Run ────
# nums = [3, 1, 5, 12, 2, 11], k = 3
#
# Push 3  → heap: [3]       size=1 ≤ 3
# Push 1  → heap: [1, 3]    size=2 ≤ 3
# Push 5  → heap: [1, 3, 5] size=3 ≤ 3
# Push 12 → heap: [1, 3, 5, 12] size=4 > 3 → pop min(1) → [3, 12, 5]
# Push 2  → heap: [2, 12, 5, 3] size=4 > 3 → pop min(2) → [3, 12, 5]
# Push 11 → heap: [3, 12, 5, 11] size=4 > 3 → pop min(3) → [5, 12, 11]
#
# Result: [5, 11, 12] ✅

print(find_k_largest([3, 1, 5, 12, 2, 11], k=3))  # → [12, 11, 5]
```

---

### 📊 Pattern 2: Top K Frequent Elements — LeetCode #347

> **"Given an array, find the K most frequently occurring elements."**
> *Crucial for real-time analytics, word count pipelines, recommendation engines.*

**Blueprint:**
1. Count frequencies using a `dict` or `Counter`.
2. Use a **Min-Heap of size K** keyed by frequency.
3. The heap evicts the least-frequent when it exceeds K.

```python
import heapq
from collections import Counter
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    📊 Top K Frequent Elements.
    LeetCode #347. Time: O(n log k) | Space: O(n)
    """
    # Step 1: Count frequencies — O(n)
    freq_map: dict[int, int] = Counter(nums)
    # freq_map = {1: 3, 2: 2, 3: 1} for nums=[1,1,1,2,2,3]

    # Step 2: Min-Heap of (frequency, element) tuples
    # Python compares tuples element-by-element, so (freq, elem)
    # means the heap is ordered by frequency (the first element)
    min_heap: List[tuple[int, int]] = []

    for element, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, element))   # (freq, value)

        if len(min_heap) > k:
            heapq.heappop(min_heap)                 # Evict least frequent

    # Step 3: Extract the elements (drop the frequency)
    return [element for freq, element in min_heap]


# ──── Dry Run ────
# nums = [1, 1, 1, 2, 2, 3], k = 2
# freq_map = {1: 3, 2: 2, 3: 1}
#
# Push (3, 1) → heap: [(3, 1)]         size=1
# Push (2, 2) → heap: [(2, 2), (3, 1)] size=2
# Push (1, 3) → heap: [(1, 3), (3, 1), (2, 2)] size=3 > 2
#   → pop min → (1, 3) evicted → heap: [(2, 2), (3, 1)]
#
# Result: elements from heap = [2, 1] ✅ (top 2 most frequent)

print(top_k_frequent([1, 1, 1, 2, 2, 3], k=2))  # → [2, 1]
```

---

### 🏃 Pattern 3: K-th Largest Element in a Stream — LeetCode #703

> **"Design a class where you can continuously add numbers to a data stream and always query the K-th largest element."**
>
> *This is the real-time analytics problem — stock prices, sensor readings, live leaderboards.*

**The Insight:** A Min-Heap of size K is a **live window** of the K largest elements seen so far. Its root (the minimum) is always the K-th largest.

```python
import heapq
from typing import List

class KthLargest:
    """
    🏃 K-th Largest Element in a Stream.
    LeetCode #703.
    
    Invariant: self.heap always holds exactly the K largest elements seen.
    Therefore, self.heap[0] (the minimum of the K largest) = K-th largest.
    
    Time: O(log k) per add() call  |  Space: O(k)
    """
    def __init__(self, k: int, nums: List[int]) -> None:
        self.k: int = k
        self.heap: List[int] = []

        for num in nums:
            self.add(num)   # Use add() to enforce the size invariant from the start

    def add(self, val: int) -> int:
        """Add a new number; return the current K-th largest."""
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)   # Evict the smallest (below K-th)

        return self.heap[0]            # Root = K-th largest


# ──── Dry Run ────
# k=3, nums=[4, 5, 8, 2]
# After init: heap=[4, 5, 8] (3 largest of [2, 4, 5, 8])
# add(3)   → push 3 → heap=[3, 5, 8, 4] → pop min(3) → heap=[4, 5, 8] → return 4
# add(5)   → push 5 → heap=[4, 5, 8, 5] → pop min(4) → heap=[5, 5, 8] → return 5
# add(10)  → push 10 → heap=[5, 5, 8, 10] → pop min(5) → heap=[5, 8, 10] → return 5
# add(9)   → push 9 → heap=[5, 8, 10, 9] → pop min(5) → heap=[8, 9, 10] → return 8
# add(4)   → push 4 → heap=[4, 9, 10, 8] → pop min(4) → heap=[8, 9, 10] → return 8

kth = KthLargest(3, [4, 5, 8, 2])
print(kth.add(3))   # → 4
print(kth.add(5))   # → 5
print(kth.add(10))  # → 5
print(kth.add(9))   # → 8
print(kth.add(4))   # → 8
```

---

### 🔗 Pattern 4: Merge K Sorted Lists — LeetCode #23

> **"You have K sorted linked lists. Merge them into one sorted linked list."**
>
> *Classic pattern for merge steps in distributed data pipelines (Hadoop/Spark merge phases).*

**The Insight:** Use a Min-Heap to always pick the globally smallest unmerged element next. Push one element from each list, and whenever you pop an element, push the next element from *that same list*.

```python
import heapq
from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val: int = val
        self.next: Optional['ListNode'] = next

def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    🔗 Merge K Sorted Linked Lists.
    LeetCode #23. 
    Time: O(N log k) where N = total nodes, k = number of lists
    Space: O(k) — heap holds at most one node per list
    """
    # Dummy head to simplify edge cases
    dummy: ListNode = ListNode(0)
    current: ListNode = dummy

    # Min-Heap: (node_value, list_index, node)
    # list_index is used as a tiebreaker to avoid comparing ListNode objects
    min_heap: List[tuple[int, int, ListNode]] = []

    # Seed the heap with the head of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    while min_heap:
        val, i, node = heapq.heappop(min_heap)   # Get globally smallest

        current.next = node                       # Attach to result
        current = current.next

        if node.next:                             # Push next element from same list
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next


# ──── Dry Run ────
# lists = [1→4→5, 1→3→4, 2→6]
#
# Initial heap: [(1,0,node1), (1,1,node1'), (2,2,node2)]
#
# Pop (1,0,1) → result: 1 → Push (4,0,node4)
# Pop (1,1,1) → result: 1→1 → Push (3,1,node3)
# Pop (2,2,2) → result: 1→1→2 → Push (6,2,node6)
# Pop (3,1,3) → result: 1→1→2→3 → Push (4,1,node4')
# Pop (4,0,4) → result: ...→4 → Push (5,0,node5)
# Pop (4,1,4)→result:...→4→4 → no next
# Pop (5,0,5) → result:...→5 → no next
# Pop (6,2,6) → result:...→6 → no next
#
# Final: 1→1→2→3→4→4→5→6 ✅
```

---

### 📅 Pattern 5: Task Scheduler — LeetCode #621

> **"Given a list of CPU tasks and a cooldown period `n`, find the minimum time to finish all tasks."**
>
> *OS scheduling, batch job processing, rate-limited API queues.*

**Blueprint:**
1. Always execute the **most frequent remaining task** next (greedy + Max-Heap).
2. If no task is ready (all on cooldown), the CPU sits **idle**.
3. Use a cooldown queue to track when tasks become available again.

```python
import heapq
from collections import Counter, deque
from typing import List

def least_interval(tasks: List[str], n: int) -> int:
    """
    📅 Task Scheduler — Minimum CPU time with cooldown n.
    LeetCode #621. Time: O(T log 26) ≈ O(T) | Space: O(26) ≈ O(1)
    where T = total number of tasks.
    """
    freq_map: dict[str, int] = Counter(tasks)

    # Max-Heap: store negative frequencies (Python only has min-heap)
    max_heap: List[int] = [-freq for freq in freq_map.values()]
    heapq.heapify(max_heap)

    # Cooldown queue: (available_at_time, -remaining_freq)
    cooldown: deque[tuple[int, int]] = deque()
    time: int = 0

    while max_heap or cooldown:
        time += 1

        if max_heap:
            freq: int = heapq.heappop(max_heap) + 1  # Execute task (reduce freq)
            if freq < 0:                              # Task still has remaining count
                cooldown.append((time + n, freq))    # Put it on cooldown

        # Check if any cooled-down task is ready
        if cooldown and cooldown[0][0] == time:
            heapq.heappush(max_heap, cooldown.popleft()[1])

    return time


# ──── Quick Check ────
# tasks = ["A", "A", "A", "B", "B", "B"], n = 2
# Frequencies: A=3, B=3
# Optimal: A B _ A B _ A B  (where _ is idle)
# Time = 8

print(least_interval(["A", "A", "A", "B", "B", "B"], n=2))  # → 8
```

---

### ⚖️ Pattern 6: Find Median from Data Stream — LeetCode #295

> **"Design a structure that inserts numbers and always returns the current median in O(log n)."**
>
> *Real-time statistics, sliding window analytics, financial data streams.*

**The Brilliant Insight — Two Heaps:**

Partition all numbers into two halves:
- **Left half** → Max-Heap (gives the largest of the smaller half instantly)
- **Right half** → Min-Heap (gives the smallest of the larger half instantly)

Keep them balanced: `len(left) == len(right)` or `len(left) == len(right) + 1`

The median is either `left.peek()` (odd total) or `(left.peek() + right.peek()) / 2` (even total).

```
Example with stream [1, 2, 3, 4, 5]:

After inserting 1, 2, 3:
       left (max-heap)  |  right (min-heap)
            [2, 1]      |       [3]
             ↑                   ↑
           max=2              min=3
Median = (2 + 3) / 2 = 2.5 ✅

After inserting 4:
       left (max-heap)  |  right (min-heap)
          [2, 1]        |     [3, 4]
...wait, sizes differ by 2! Rebalance:
       left (max-heap)  |  right (min-heap)
          [2, 1]        |    [3, 4]  ← size=len(left)+1? No, rebalance by moving 3 left
          [3, 2, 1]     |      [4]
Median = left.peek() = 3 ✅
```

```python
import heapq

class MedianFinder:
    """
    ⚖️ Find Median from Data Stream — Two Heap approach.
    LeetCode #295.
    add_num: O(log n) | find_median: O(1) | Space: O(n)
    """
    def __init__(self) -> None:
        # Max-heap for LEFT half (store negative values)
        self.left_max: list[int] = []
        # Min-heap for RIGHT half
        self.right_min: list[int] = []

    def add_num(self, num: int) -> None:
        """Push to left first, then rebalance sizes."""
        # Step 1: Push to left (max-heap)
        heapq.heappush(self.left_max, -num)

        # Step 2: Ensure left's max ≤ right's min (cross-contamination check)
        if self.right_min and (-self.left_max[0] > self.right_min[0]):
            val: int = -heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, val)

        # Step 3: Balance sizes: left can be at most 1 ahead of right
        if len(self.left_max) > len(self.right_min) + 1:
            val = -heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, val)
        elif len(self.right_min) > len(self.left_max):
            val = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -val)

    def find_median(self) -> float:
        """Return current median in O(1)."""
        if len(self.left_max) > len(self.right_min):
            return float(-self.left_max[0])       # Odd count: left has the middle
        return (-self.left_max[0] + self.right_min[0]) / 2.0  # Even count: average


# ──── Test ────
mf = MedianFinder()
mf.add_num(1);  print(mf.find_median())  # → 1.0
mf.add_num(2);  print(mf.find_median())  # → 1.5
mf.add_num(3);  print(mf.find_median())  # → 2.0
mf.add_num(4);  print(mf.find_median())  # → 2.5
mf.add_num(5);  print(mf.find_median())  # → 3.0
```

---

## 🗺️ 6. Heaps in Graph Algorithms — Dijkstra's Shortest Path

Heaps are the core engine of **Dijkstra's algorithm** — the gold standard for finding shortest paths in weighted graphs. Every time your GPS calculates a route, this is running.

```
Graph:
    1 ──(4)── 2
    │          │
   (1)        (2)
    │          │
    3 ──(5)── 4
         ↑
    (weight on edge)

Shortest path from 1 to 4?
Naive: Try every path. Exponential.
Dijkstra + Min-Heap: O((V + E) log V). Near-linear.
```

```python
import heapq
from typing import List, Dict, Tuple
from collections import defaultdict
from math import inf

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, float]:
    """
    🗺️ Dijkstra's Shortest Path Algorithm.
    
    graph format: {node: [(neighbor, weight), ...]}
    Returns: {node: shortest_distance_from_start}
    
    Time: O((V + E) log V)  |  Space: O(V)
    """
    # Min-heap: (distance_from_start, node)
    min_heap: List[Tuple[float, int]] = [(0, start)]
    distances: Dict[int, float] = defaultdict(lambda: inf)
    distances[start] = 0

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        # Skip if we've already found a shorter path to this node
        if dist > distances[node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph.get(node, []):
            new_dist: float = dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dict(distances)


# ──── Test ────
graph: Dict[int, List[Tuple[int, int]]] = {
    1: [(2, 4), (3, 1)],
    2: [(4, 2)],
    3: [(4, 5)],
    4: []
}
print(dijkstra(graph, start=1))
# → {1: 0, 2: 4, 3: 1, 4: 6}
# Shortest to 4: 1→2→4 = 4+2=6  OR  1→3→4 = 1+5=6. Tie! ✅
```

---

## 📊 7. Pattern Recognition Cheat Sheet

Use this to instantly identify which heap pattern applies in an interview:

| Signal in the Problem | Pattern | Heap Type |
|:----------------------|:--------|:----------|
| "K largest / K smallest" | Top K Elements | Min-Heap of size K |
| "K most frequent" | Top K Frequent | Min-Heap of size K (keyed by frequency) |
| "K-th largest in a stream" | Kth Largest in Stream | Min-Heap of size K |
| "Merge K sorted arrays/lists" | Merge K Lists | Min-Heap with (val, list_idx) |
| "Median from stream" | Two Heaps | Max-Heap + Min-Heap |
| "Minimum cost / Greedy scheduling" | Greedy + Heap | Min-Heap |
| "Shortest path in weighted graph" | Dijkstra | Min-Heap of (dist, node) |
| "Most frequent task / Schedule" | Task Scheduler | Max-Heap (by frequency) |

---

## 🧮 8. Complexity Summary

| Operation | Time | Space |
|:----------|:----:|:-----:|
| Build Heap (`heapify`) | **O(n)** | O(1) |
| Push | O(log n) | O(1) |
| Pop | O(log n) | O(1) |
| Peek (min/max) | **O(1)** | O(1) |
| Top K Elements | O(n log k) | O(k) |
| Merge K Lists (N total) | O(N log k) | O(k) |
| Dijkstra (V vertices, E edges) | O((V+E) log V) | O(V) |
| Kth Largest Stream | O(log k) per insert | O(k) |
| Median from Stream | O(log n) per insert | O(n) |

---

## 🚀 9. Quick Reference — The Heap Toolkit

```python
import heapq

heap = []                        # Empty min-heap
heapq.heappush(heap, val)        # Push: O(log n)
heapq.heappop(heap)              # Pop minimum: O(log n)
heap[0]                          # Peek minimum: O(1)
heapq.heapify(list)              # Build heap in-place: O(n)
heapq.nlargest(k, iterable)      # Top K largest: O(n log k)
heapq.nsmallest(k, iterable)     # Top K smallest: O(n log k)

# Max-Heap: negate values
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)

# Heap of tuples: heapq compares by first element
heapq.heappush(heap, (priority, value))
```

---

> 💡 **The Meta-Pattern:** Whenever a problem needs *repeated access to the current best (min or max)* from a dynamic set — **think Heap**. It's the only structure that gives O(1) peek and O(log n) update simultaneously.