# 🧠 Memory Management: How Python Stores Your Data

> *"Understanding memory is like understanding the floor plan of your house — once you know where everything lives, you can find and move things in ways you never thought possible."*

🎯 **Mission:** Understand how computers store data in memory, the difference between **Static** and **Dynamic** arrays, and why Python's `list` is one of the cleverest pieces of engineering in modern programming.

---

## 📚 Table of Contents

| Section | Topics Covered |
|---------|----------------|
| **Part A: Memory Fundamentals** | RAM, Addresses, Bits & Bytes |
| **Part B: Static Arrays** | Fixed-size, contiguous memory, C-style |
| **Part C: Dynamic Arrays** | Resizing strategy, amortized O(1) |
| **Part D: Python's `list` Deep Dive** | How CPython manages memory under the hood |
| **Part E: Stack vs Heap** | Where variables actually live |
| **Part F: Complexity Analysis** | Time & Space, side by side |
| **Part G: Practice Problems** | LeetCode-style challenges |

---

## 🧱 Part A: Memory Fundamentals

### 💡 What is RAM?

**RAM (Random Access Memory)** is your computer's short-term workspace. Think of it as a **massive row of numbered lockers** in a school hallway.

```
Memory (RAM) - Visualized as lockers:

Address:  0x0000  0x0001  0x0002  0x0003  0x0004  ...
          +------+------+------+------+------+
Value:    |  72  |  65  |  76  |  76  |  79  |  ...
          +------+------+------+------+------+
            'H'    'e'    'l'    'l'    'o'
```

- Every locker has a **unique address** (like a house number)
- Each locker stores **1 byte** (8 bits) of data
- The CPU can jump to **any address instantly** — hence "Random Access"

### 📦 Bits, Bytes & Data Sizes

```python
# Size reference chart
size_reference = {
    "1 bit"     : "Stores 0 or 1",
    "1 byte"    : "8 bits — stores one character (e.g., 'A')",
    "4 bytes"   : "32-bit integer (e.g., 42 or -1,000,000)",
    "8 bytes"   : "64-bit float or Python object reference",
    "1 KB"      : "1,024 bytes — a short paragraph of text",
    "1 MB"      : "1,048,576 bytes — a small image",
    "1 GB"      : "1,073,741,824 bytes — a movie",
}
```

### 🎯 The Key Idea: Contiguous vs Non-Contiguous Memory

```
Contiguous (Array):               Non-Contiguous (Linked List):
+----+----+----+----+            +----+     +----+     +----+
| 10 | 20 | 30 | 40 |            | 10 |---> | 20 |---> | 30 |
+----+----+----+----+            +----+     +----+     +----+
  [0]  [1]  [2]  [3]            addr:100   addr:350   addr:820

✅ Fast access by index            ✅ Easy insert/delete
❌ Hard to resize                  ❌ Slow index access (must traverse)
```

**Bottom line:** Arrays are fast to read, tricky to grow. Linked lists are easy to grow, slow to random-access.

---

## 📏 Part B: Static Arrays

### 💡 What is a Static Array?

A **Static Array** is a **fixed-size, contiguous block of memory** allocated at creation time. You must declare exactly how many elements it will hold — no more, no less.

**Real-World Analogy 🏢:** Imagine a parking garage with **exactly 10 floors**. It was built with 10 floors and it will always have 10 floors. You cannot add an 11th floor without demolishing and rebuilding.

```
Static Array of size 5, storing integers (4 bytes each):

Memory Address:  1000   1004   1008   1012   1016
                  ↓      ↓      ↓      ↓      ↓
                +----+  +----+  +----+  +----+  +----+
                | 10 |  | 25 |  | 07 |  | 42 |  | 00 |
                +----+  +----+  +----+  +----+  +----+
Index:            0      1      2      3      4

Formula: address(i) = base_address + (i × element_size)
Example: address(3) = 1000 + (3 × 4) = 1012 ✓
```

### ⚡ Why O(1) Random Access?

Because of the formula above! The CPU doesn't **search** for index 3. It **calculates** the exact address in one arithmetic operation. That's why array access is always `O(1)`.

```python
# Simulating how static arrays work (in Python for illustration)
from typing import List

class StaticArray:
    """Simulates a fixed-size array (like C/C++ arrays)."""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity  # Pre-allocate all memory
        self.size = 0
    
    def get(self, index: int) -> int:
        """O(1) - Direct address calculation."""
        if index < 0 or index >= self.capacity:
            raise IndexError(f"Index {index} out of bounds for capacity {self.capacity}")
        return self.data[index]
    
    def set(self, index: int, value: int) -> None:
        """O(1) - Direct address calculation."""
        if index < 0 or index >= self.capacity:
            raise IndexError(f"Index {index} out of bounds for capacity {self.capacity}")
        self.data[index] = value
        self.size = max(self.size, index + 1)
    
    def is_full(self) -> bool:
        return self.size == self.capacity


# Example Usage
arr = StaticArray(5)
arr.set(0, 10)
arr.set(1, 25)
arr.set(2, 7)

print(arr.get(0))   # 10 — O(1)
print(arr.get(2))   # 7  — O(1)
print(arr.is_full()) # False
```

### 📊 Static Array Complexity

| Operation | Time | Why? |
|-----------|------|------|
| **Access** `arr[i]` | `O(1)` | Direct address formula |
| **Search** (unsorted) | `O(N)` | Must scan every element |
| **Search** (sorted, binary) | `O(log N)` | Halve search space each step |
| **Insert** (at end, if space) | `O(1)` | Direct write to known address |
| **Insert** (at middle) | `O(N)` | Must shift all elements right |
| **Delete** (at middle) | `O(N)` | Must shift all elements left |

### ❌ The Fatal Flaw: Rigid Size

```python
# The problem: What happens when you need more space?

# In C (static array, no auto-resize):
# int arr[5] = {1, 2, 3, 4, 5};
# arr[5] = 6;  ← BUFFER OVERFLOW! Undefined behavior / crash!

# You'd have to manually:
# 1. Allocate a new array of size 10
# 2. Copy all 5 elements over
# 3. Free the old array
# 4. Use the new array
# This is O(N) every time you run out of space!
```

---

## 🚀 Part C: Dynamic Arrays

### 💡 What is a Dynamic Array?

A **Dynamic Array** solves the rigid-size problem by **automatically resizing** when it gets full. But it's smarter than just growing by 1 each time — it uses a **doubling strategy** that makes the average append cost `O(1)`.

**Real-World Analogy 🏠→🏡→🏰:** Imagine renting an apartment. When your stuff outgrows it, you don't move to an apartment that's 1 room bigger — you move to one that's **twice as big**, so you have room to grow for a long time before you need to move again.

### 📐 The Doubling Strategy (Amortized Analysis)

```
Step-by-step growth of a dynamic array:

Append 1: [1]             capacity=1,  size=1  (full!)
Append 2: [1, 2, _, _]    capacity=2→4,size=2  (resize: copy 1 elem)
Append 3: [1, 2, 3, _]    capacity=4,  size=3
Append 4: [1, 2, 3, 4]    capacity=4,  size=4  (full!)
Append 5: [1,2,3,4,5,_,_,_,_,_,_,_,_,_,_,_] capacity=4→8, size=5 (resize: copy 4 elems)
...

Resize events happen at sizes: 1, 2, 4, 8, 16, 32 ...
Cost of resizes: 1 + 2 + 4 + 8 + ... + N = 2N (geometric series)
Total cost for N appends: N (actual appends) + 2N (copies) = 3N = O(N)
Cost PER append: O(N) / N = O(1) — This is "Amortized O(1)"!
```

### 🔬 Building a Dynamic Array from Scratch

```python
from typing import Any, Optional

class DynamicArray:
    """
    A fully functional Dynamic Array implementation.
    Mirrors how Python's list works under the hood.
    """
    
    GROWTH_FACTOR = 2  # Double capacity on resize
    
    def __init__(self):
        self._capacity: int = 1
        self._size: int = 0
        self._data: list = [None] * self._capacity
    
    # ─── Core Operations ────────────────────────────────────────────
    
    def append(self, value: Any) -> None:
        """
        Add element to the end.
        Time: O(1) amortized — occasionally O(N) for resize
        Space: O(1) amortized
        """
        if self._size == self._capacity:
            self._resize()               # ← expensive but rare!
        
        self._data[self._size] = value
        self._size += 1
    
    def get(self, index: int) -> Any:
        """
        Access element by index.
        Time: O(1) — direct address calculation
        """
        self._validate_index(index)
        return self._data[index]
    
    def set(self, index: int, value: Any) -> None:
        """
        Update element at index.
        Time: O(1)
        """
        self._validate_index(index)
        self._data[index] = value
    
    def insert(self, index: int, value: Any) -> None:
        """
        Insert element at given index (shifts all elements right).
        Time: O(N) — shifting elements
        """
        self._validate_index_for_insert(index)
        if self._size == self._capacity:
            self._resize()
        
        # Shift elements right to make space
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        
        self._data[index] = value
        self._size += 1
    
    def delete(self, index: int) -> Any:
        """
        Delete element at index (shifts all elements left).
        Time: O(N) — shifting elements
        """
        self._validate_index(index)
        removed = self._data[index]
        
        # Shift elements left to fill the gap
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        
        self._data[self._size - 1] = None  # Prevent memory leak
        self._size -= 1
        return removed
    
    def pop(self) -> Any:
        """
        Remove and return the last element.
        Time: O(1)
        """
        if self._size == 0:
            raise IndexError("pop from empty array")
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value
    
    # ─── Internal Resize Logic ──────────────────────────────────────
    
    def _resize(self) -> None:
        """
        Double the internal capacity and copy all elements.
        Time: O(N) — but happens logarithmically rarely
        
        Visual:
        Before: [1, 2, 3, 4]  capacity=4 (FULL)
        After:  [1, 2, 3, 4, _, _, _, _]  capacity=8
        """
        new_capacity = self._capacity * self.GROWTH_FACTOR
        new_data = [None] * new_capacity
        
        for i in range(self._size):        # Copy all elements
            new_data[i] = self._data[i]
        
        self._data = new_data
        self._capacity = new_capacity
    
    # ─── Helpers ────────────────────────────────────────────────────
    
    def _validate_index(self, index: int) -> None:
        if not (0 <= index < self._size):
            raise IndexError(f"Index {index} out of range for size {self._size}")
    
    def _validate_index_for_insert(self, index: int) -> None:
        if not (0 <= index <= self._size):
            raise IndexError(f"Index {index} out of range for insert")
    
    def __len__(self) -> int:
        return self._size
    
    def __repr__(self) -> str:
        items = [str(self._data[i]) for i in range(self._size)]
        return f"DynamicArray([{', '.join(items)}], size={self._size}, capacity={self._capacity})"


# ─── Usage Demo ──────────────────────────────────────────────────────
da = DynamicArray()

da.append(10); da.append(20); da.append(30)
print(da)             # DynamicArray([10, 20, 30], size=3, capacity=4)

da.insert(1, 99)
print(da)             # DynamicArray([10, 99, 20, 30], size=4, capacity=4)

da.delete(0)
print(da)             # DynamicArray([99, 20, 30], size=3, capacity=4)

print(da.get(1))      # 20
print(len(da))        # 3
```

### ⚖️ Amortized Analysis — The Math Behind O(1) Append

```
Let's track the TOTAL cost of N appends (each is either free or costs a resize):

N = 8 appends:
  Append 1: cost = 1 (no resize)
  Append 2: cost = 1 (no resize)  ← capacity was 1, RESIZE (1 copy) → capacity 2
  Append 3: cost = 1              ← RESIZE (2 copies) → capacity 4
  Append 4: cost = 1
  Append 5: cost = 1              ← RESIZE (4 copies) → capacity 8
  Append 6: cost = 1
  Append 7: cost = 1
  Append 8: cost = 1

  Total append cost:  8
  Total resize cost:  1 + 2 + 4 = 7  (geometric: 2N - 1)
  Total combined:     8 + 7 = 15 ≈ 2N

  Average per append: 15/8 ≈ 2 = O(1) amortized! 🎉
```

---

## 🐍 Part D: Python's `list` Deep Dive

### 💡 Python `list` = Dynamic Array on Steroids

Python's `list` is a **dynamic array of pointers** (object references), not raw data. This is crucial to understand!

```
Python list: my_list = [42, "hello", 3.14]

Under the hood (CPython):

my_list object:
  ob_size    = 3          (current size)
  allocated  = 4          (capacity)
  ob_item --→ [ptr₁, ptr₂, ptr₃, ___]
                ↓      ↓      ↓
               42   "hello" 3.14   ← Separate objects in heap memory

Each pointer = 8 bytes (64-bit system)
The list only stores POINTERS, not the actual values!
```

### 🔍 How Python Grows Its List

Python's resizing is slightly more nuanced than simple doubling. CPython uses the formula:

```python
# CPython's actual growth formula (simplified):
def new_capacity(current_size: int) -> int:
    """
    Grows by ~12.5% + a base factor.
    Balances memory efficiency against resize frequency.
    """
    return current_size + (current_size >> 3) + (3 if current_size < 9 else 6)

# Growth pattern:
for size in [0, 4, 8, 16, 25, 35, 46, 58, 72, 88]:
    print(f"size={size} → next_capacity={new_capacity(size)}")

# Output:
# size=0  → next_capacity=3
# size=4  → next_capacity=8
# size=8  → next_capacity=15
# size=16 → next_capacity=22
# size=25 → next_capacity=34
```

### 🕵️ Observing List Growth in Action

```python
import sys

def observe_list_growth(n: int = 20) -> None:
    """
    Watch Python's list grow and track when it reallocates memory.
    Uses sys.getsizeof() to detect capacity changes.
    """
    lst = []
    prev_size = sys.getsizeof(lst)
    
    print(f"{'Elements':>10} | {'Memory (bytes)':>15} | {'Status':>15}")
    print("-" * 50)
    
    for i in range(n):
        lst.append(i)
        current_size = sys.getsizeof(lst)
        
        status = "✅ RESIZE!" if current_size > prev_size else "      "
        print(f"{len(lst):>10} | {current_size:>15} | {status:>15}")
        
        prev_size = current_size

observe_list_growth(20)

# Expected output (CPython 3.x, 64-bit):
# Elements   Memory (bytes)          Status
# --------------------------------------------------
#        1               88
#        2               96
#        3              104
#        4              112
#        5              120        ✅ RESIZE!
#        6              128
#       ...
```

### 🔑 Key Facts About Python `list`

```python
# ✅ What Python lists are GOOD at:
fast_operations = {
    "append()":         "O(1) amortized — add to end",
    "pop()":            "O(1) — remove from end",
    "lst[i]":           "O(1) — random access by index",
    "lst[i] = val":     "O(1) — update by index",
    "len(lst)":         "O(1) — stored as an attribute",
}

# ❌ What Python lists are SLOW at:
slow_operations = {
    "insert(0, val)":   "O(N) — shifts everything right",
    "pop(0)":           "O(N) — shifts everything left",
    "del lst[i]":       "O(N) — shifts elements after i",
    "val in lst":       "O(N) — linear scan",
    "lst.remove(val)":  "O(N) — finds then removes",
}

# ⚡ Pro tip: Use collections.deque for O(1) front/back operations!
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)   # O(1) ← lists would be O(N) here!
dq.popleft()       # O(1)
```

---

## 🏗️ Part E: Stack vs Heap Memory

### 💡 Where Do Variables Actually Live?

Your program has two massive memory regions it works with:

```
Process Memory Layout:
┌───────────────────────────────────┐  ← High Address
│         STACK MEMORY              │
│  • Function call frames           │
│  • Local variables                │
│  • Fixed-size, fast allocation    │
│  • Grows DOWNWARD ↓               │
├───────────────────────────────────┤
│                                   │
│   (Free Space — grows/shrinks)    │
│                                   │
├───────────────────────────────────┤
│          HEAP MEMORY              │
│  • Dynamically allocated objects  │
│  • Python objects live here!      │
│  • Grows UPWARD ↑                 │
│  • Managed by Garbage Collector   │
├───────────────────────────────────┤
│       BSS / Data Segment          │
│  • Global & static variables      │
├───────────────────────────────────┤
│          Code Segment             │  ← Low Address
└───────────────────────────────────┘
```

### 🐍 In Python: Everything is on the Heap

```python
# Python hides the stack/heap distinction from you.
# But here's what's happening under the hood:

def my_function():
    x = 42           # x is a reference stored on the stack
                     # The integer object 42 lives on the HEAP
    
    lst = [1, 2, 3]  # lst is a reference on the stack
                     # The list object lives on the HEAP
                     # The integers 1, 2, 3 each live on the HEAP too!
    
    return lst       # The reference is passed back, the HEAP object survives

# Python's Garbage Collector uses Reference Counting:
import sys

lst = [1, 2, 3]
print(sys.getrefcount(lst))   # 2 (lst + getrefcount's argument)

lst2 = lst
print(sys.getrefcount(lst))   # 3 (lst, lst2, + getrefcount)

del lst2
print(sys.getrefcount(lst))   # 2 again
# When count hits 0, object is freed from heap!
```

### 🔁 Call Stack Visualization

```
Python call stack for: factorial(3)

┌──────────────────────────────┐  ← TOP of Stack (most recent call)
│  factorial(n=1)              │
│    Locals: n=1               │
│    Returns: 1                │
├──────────────────────────────┤
│  factorial(n=2)              │
│    Locals: n=2               │
│    Waiting for factorial(1)  │
├──────────────────────────────┤
│  factorial(n=3)              │
│    Locals: n=3               │
│    Waiting for factorial(2)  │
├──────────────────────────────┤
│  __main__                    │  ← BOTTOM of Stack
└──────────────────────────────┘

Each "frame" takes space → Recursion too deep = StackOverflow!
Python's default recursion limit: sys.getrecursionlimit() = 1000
```

```python
import sys

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Space Complexity: O(N) — N frames on the call stack
# Deepening recursion = growing the stack

# Check Python's recursion limit:
print(sys.getrecursionlimit())  # 1000

# Increase if needed (use with caution!):
# sys.setrecursionlimit(5000)
```

---

## 📊 Part F: Complexity Summary

### ⏱️ Time Complexity Comparison

```
Operation         Static Array   Dynamic Array   Python list
─────────────────────────────────────────────────────────────
Access  [i]          O(1)           O(1)            O(1)   ✅
Append to end        N/A            O(1)*           O(1)*  ✅
Prepend (index 0)    N/A            O(N)            O(N)   ❌
Insert at middle     O(N)           O(N)            O(N)   ❌
Delete at middle     O(N)           O(N)            O(N)   ❌
Pop from end         N/A            O(1)            O(1)   ✅
Pop from front       N/A            O(N)            O(N)   ❌
Search (unsorted)    O(N)           O(N)            O(N)   ❌
Search (sorted)      O(log N)       O(log N)        O(log N) ✅
Contains (x in lst)  O(N)           O(N)            O(N)   ❌

* = Amortized O(1)
```

### 💾 Space Complexity

```python
space_analysis = {
    "Static Array of N ints":      "O(N) — exactly N * element_size bytes",
    "Dynamic Array (Python list)": "O(N) to O(2N) — capacity grows in jumps",
    "Python list overhead":        "~56 bytes base + 8 bytes per element slot",
}

# Memory footprint demo:
import sys

for n in [0, 10, 100, 1_000, 10_000]:
    lst = list(range(n))
    print(f"n={n:>6,} → {sys.getsizeof(lst):>8,} bytes")

# Output:
# n=     0 →       56 bytes
# n=    10 →      184 bytes
# n=   100 →      920 bytes
# n= 1,000 →    8,056 bytes
# n=10,000 →   80,056 bytes
```

---

## 🧪 Part G: Practice Problems

> 🎯 **Test your understanding of memory and array internals!**

---

### 🟢 **Problem 1: Implement a Circular Buffer — Easy**

A circular buffer (ring buffer) is a fixed-size array that wraps around. When full, new writes overwrite the oldest data.

**Use case:** Audio streaming, log systems, OS kernel buffers.

```
Visual: Circular Buffer of size 4

Step 1: Write 1  →  [1, _, _, _]  head=0, tail=1
Step 2: Write 2  →  [1, 2, _, _]  head=0, tail=2
Step 3: Write 3  →  [1, 2, 3, _]  head=0, tail=3
Step 4: Write 4  →  [1, 2, 3, 4]  head=0, tail=0 (wrapped!)
Step 5: Write 5  →  [5, 2, 3, 4]  head=1, tail=1 (overwrote oldest!)
Step 6: Read     →  returns 2,    head=2
```

<details>
<summary>📖 Click to reveal solution</summary>

```python
class CircularBuffer:
    """
    Fixed-size circular buffer.
    Write overwrites oldest data when full.
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0   # Next read position
        self.tail = 0   # Next write position
        self.size = 0
    
    def write(self, value: int) -> None:
        """Write a value. Overwrites oldest if full."""
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity  # Wrap around!
        
        if self.size < self.capacity:
            self.size += 1
        else:
            # Overwriting oldest data — advance head too
            self.head = (self.head + 1) % self.capacity
    
    def read(self) -> int:
        """Read (and remove) the oldest value."""
        if self.size == 0:
            raise IndexError("Buffer is empty")
        
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def is_full(self) -> bool:
        return self.size == self.capacity
    
    def __repr__(self) -> str:
        return f"CircularBuffer({self.buffer}, head={self.head}, tail={self.tail})"


# Test
cb = CircularBuffer(4)
cb.write(1); cb.write(2); cb.write(3); cb.write(4)
print(cb)        # [1, 2, 3, 4], head=0, tail=0

cb.write(5)      # Overwrites 1!
print(cb.read()) # 2 (oldest remaining)
print(cb.read()) # 3
```

**Complexity:** Write O(1), Read O(1), Space O(capacity)

</details>

---

### 🟡 **Problem 2: Design a Stack with O(1) getMin() — Medium**

Design a stack that supports `push()`, `pop()`, and `getMin()` — all in O(1) time.

**LeetCode:** [155. Min Stack](https://leetcode.com/problems/min-stack/)

```
Trace:
push(5)  → stack=[5],     min_stack=[5]
push(3)  → stack=[5,3],   min_stack=[5,3]
push(7)  → stack=[5,3,7], min_stack=[5,3,3]  ← min stays 3!
getMin() → 3
pop()    → stack=[5,3],   min_stack=[5,3]
getMin() → 3
pop()    → stack=[5],     min_stack=[5]
getMin() → 5
```

<details>
<summary>📖 Click to reveal solution</summary>

```python
class MinStack:
    """
    Stack with O(1) getMin() using an auxiliary min-tracking stack.
    Key insight: Track the current minimum at each level.
    """
    
    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []  # Tracks min at each level
    
    def push(self, val: int) -> None:
        """O(1) — push to both stacks."""
        self.stack.append(val)
        
        # New min is either val or the current minimum
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)
    
    def pop(self) -> None:
        """O(1) — pop from both stacks in sync."""
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self) -> int:
        """O(1) — peek top of stack."""
        return self.stack[-1]
    
    def getMin(self) -> int:
        """O(1) — current minimum is always at top of min_stack."""
        return self.min_stack[-1]


# Test
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)

print(ms.getMin())  # 3 ✓
ms.pop()
print(ms.getMin())  # 3 ✓
ms.pop()
print(ms.getMin())  # 5 ✓
```

**Complexity:** All operations O(1) Time, O(N) Space

</details>

---

### 🟠 **Problem 3: Rotate Array In-Place — Medium**

Given an array of `n` elements and a value `k`, rotate the array to the right by `k` steps **in-place** (O(1) extra space).

**LeetCode:** [189. Rotate Array](https://leetcode.com/problems/rotate-array/)

```
Example: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Result:         [5, 6, 7, 1, 2, 3, 4]

The Reverse Trick:
Step 1: Reverse entire array  → [7, 6, 5, 4, 3, 2, 1]
Step 2: Reverse first k=3     → [5, 6, 7, 4, 3, 2, 1]
Step 3: Reverse last n-k=4    → [5, 6, 7, 1, 2, 3, 4] ✓
```

<details>
<summary>📖 Click to reveal solution</summary>

```python
from typing import List

def rotate_array(nums: List[int], k: int) -> None:
    """
    Rotate array right by k steps in-place.
    Uses the elegant 3-reversal trick.
    
    Time:  O(N)
    Space: O(1) — truly in-place!
    """
    n = len(nums)
    k = k % n  # Handle k > n (full rotations cancel out)
    
    def reverse(left: int, right: int) -> None:
        """Reverse a subarray in-place."""
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    reverse(0, n - 1)       # Step 1: reverse entire array
    reverse(0, k - 1)       # Step 2: reverse first k elements
    reverse(k, n - 1)       # Step 3: reverse remaining n-k elements


# Test
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums, 3)
print(nums)  # [5, 6, 7, 1, 2, 3, 4] ✓

nums = [1, 2]
rotate_array(nums, 3)  # k=3, n=2 → k=3%2=1 (smart!)
print(nums)  # [2, 1] ✓
```

</details>

---

### 🔴 **Problem 4: LRU Cache — Hard**

Design a data structure that implements an **LRU (Least Recently Used) Cache** with `O(1)` get and put operations.

**LeetCode:** [146. LRU Cache](https://leetcode.com/problems/lru-cache/)

```
LRU Cache (capacity=3):

put(1,A): Cache = {1:A}           ← 1 is most recent
put(2,B): Cache = {1:A, 2:B}      ← 2 is most recent
put(3,C): Cache = {1:A, 2:B, 3:C} ← 3 is most recent
get(1):   Cache = {2:B, 3:C, 1:A} ← 1 moved to front (recently used!)
put(4,D): Cache = {3:C, 1:A, 4:D} ← 2 EVICTED (least recently used!)
```

<details>
<summary>📖 Click to reveal solution</summary>

```python
from collections import OrderedDict

class LRUCache:
    """
    LRU Cache using Python's OrderedDict.
    OrderedDict maintains insertion order + supports move_to_end().
    
    Time:  O(1) for both get and put
    Space: O(capacity)
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()
    
    def get(self, key: int) -> int:
        """
        Retrieve value. Returns -1 if not found.
        Move accessed key to end (most recently used).
        """
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.
        If at capacity, evict the LEAST recently used (front).
        """
        if key in self.cache:
            self.cache.move_to_end(key)  # Update → mark as recent
        
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Evict LRU (front)


# Test
cache = LRUCache(3)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")

print(cache.get(1))  # "A" — and 1 is now most recent!
cache.put(4, "D")    # Evicts 2 (LRU)

print(cache.get(2))  # -1 (evicted!)
print(cache.get(3))  # "C"
print(cache.get(4))  # "D"
```

**Complexity:** `get` O(1), `put` O(1), Space O(capacity)

</details>

---

## 🗺️ Concept Map

```
                    MEMORY MANAGEMENT
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
      STATIC ARRAY    DYNAMIC ARRAY    CALL STACK
           │               │               │
     Fixed size       Grows by 2x     Function frames
     O(1) access      Amortized O(1)  Recursion depth
     Fast but rigid   Flexible        Limited (default 1000)
           │               │
           └───────┬───────┘
                   ▼
            Python's list
                   │
          ┌────────┴────────┐
          ▼                 ▼
    Array of pointers    GC manages
    8 bytes each         object lifetime
    on the HEAP          via ref counting
```

---

## 🏅 Key Takeaways

| Concept | The Golden Rule |
|---------|-----------------|
| **Static Array** | Fixed size, but blazing fast `O(1)` access via address formula |
| **Dynamic Array** | Amortized `O(1)` append via doubling strategy — rare O(N) resizes average out |
| **Python `list`** | Dynamic array of 8-byte object pointers — `append/pop` is O(1), everything else on ends/middle is O(N) |
| **Stack Memory** | Automatic, fast, limited — holds local variables and call frames |
| **Heap Memory** | Managed by GC, unlimited (in theory), slower — where Python objects live |
| **Amortized O(1)** | Some operations are expensive occasionally, but averaged over many calls, cost per call = O(1) |

> 💡 **Interview Tip:** When asked "What is the time complexity of `list.append()` in Python?", say **"O(1) amortized"** and explain the doubling strategy. This instantly signals deep knowledge!

---

*Part of the [DSA Pattern-First](../../README.md) learning path — Phase 1: Foundations*