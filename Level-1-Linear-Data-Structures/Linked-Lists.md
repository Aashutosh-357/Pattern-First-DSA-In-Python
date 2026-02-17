# 🔗 Linked Lists - The Dynamic Chain

> *"Arrays are like apartment buildings (fixed addresses). Linked Lists are like treasure hunts (follow the clues)."*

🎯 **Mission:** Master the most flexible linear data structure. While arrays give O(1) access, linked lists give O(1) insertion/deletion at known positions. Understanding pointers is the key!

---

## 📚 Table of Contents

| Section | Topics Covered |
|---------|----------------|
| **Part A: Singly Linked List** | Node structure, Traversal, Insert, Delete, Reverse |
| **Part B: Advanced SLL Patterns** | Merge Two Lists, Middle Element, Remove Nth from End |
| **Part C: Doubly Linked List** | Bidirectional traversal, LRU Cache Implementation |
| **Part D: Floyd's Cycle Detection** | Tortoise & Hare, Cycle Start, Palindrome Check |

---

## 🧱 Part A: Singly Linked List (SLL)

### 💡 What is a Linked List?

A **Linked List** is a sequence of nodes where each node contains:
1. **Data** (the value)
2. **Next** (pointer/reference to the next node)

**Visual Representation:**
```
HEAD
 ↓
[10|●]→[20|●]→[30|●]→[40|∅]
       TAIL
```

**Key Differences from Arrays:**

| Feature | Array | Linked List |
|---------|-------|-------------|
| **Memory** | Contiguous | Scattered (anywhere in RAM) |
| **Access** | O(1) by index | O(n) - must traverse |
| **Insert/Delete** | O(n) - shifting | O(1) at known position |
| **Size** | Fixed (or expensive resize) | Dynamic (grow/shrink easily) |

### 🎯 The Train Analogy

Think of a linked list as a **train**:
```
🚂 → 🚃 → 🚃 → 🚃 → ∅
```
- Each car (node) knows about the **next** car
- To reach car #3, you must go through cars #1 and #2
- Adding/removing a car is easy (just reconnect the links!)

### 💻 Python Implementation

#### **Node Class**
```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"Node({self.val})"
```

#### **Basic Operations**

```python
class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
    
    def append(self, val: int) -> None:
        """Add node at the end."""
        new_node = ListNode(val)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, val: int) -> None:
        """Add node at the beginning."""
        new_node = ListNode(val, self.head)
        self.head = new_node
    
    def display(self) -> None:
        """Print the linked list."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" → ".join(elements) + " → ∅")
    
    def search(self, target: int) -> bool:
        """Search for a value."""
        current = self.head
        while current:
            if current.val == target:
                return True
            current = current.next
        return False

# Test
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.display()  # 5 → 10 → 20 → 30 → ∅
```

**Complexity:**
- `append`: O(n) - must traverse to end
- `prepend`: O(1) - direct insertion
- `search`: O(n) - linear scan

---

### 🔥 **Pattern 1: Reverse a Linked List** ⭐⭐⭐

**The Most Asked LL Interview Question!**

```python
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list iteratively.
    
    Visual:
    Before: 1 → 2 → 3 → 4 → ∅
    After:  4 → 3 → 2 → 1 → ∅
    
    Logic: Keep reversing the 'next' pointers.
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Save next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev forward
        current = next_temp       # Move current forward
    
    return prev  # New head

# Recursive version
def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head  # Reverse the link
    head.next = None       # Break old link
    
    return new_head
```

**Complexity:** Time O(n), Space O(1) iterative, O(n) recursive (call stack)

---

### 🔥 **Pattern 2: Delete Node** ⭐

```python
def delete_node(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    Delete first occurrence of a value.
    
    Visual: Delete 20
    Before: 10 → 20 → 30 → ∅
    After:  10 → 30 → ∅
    """
    # Special case: delete head
    if head and head.val == val:
        return head.next
    
    current = head
    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next  # Skip the node
            break
        current = current.next
    
    return head
```

**Complexity:** Time O(n), Space O(1)

---

## 🎪 Part B: Advanced SLL Patterns

### 🔥 **Pattern 3: Merge Two Sorted Lists** ⭐⭐

```python
def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted list.
    
    Example:
    L1: 1 → 3 → 5 → ∅
    L2: 2 → 4 → 6 → ∅
    Result: 1 → 2 → 3 → 4 → 5 → 6 → ∅
    
    Logic: Use a dummy node to simplify edge cases.
    """
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 if l1 else l2
    
    return dummy.next

# Test
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
result = merge_two_lists(l1, l2)
```

**Complexity:** Time O(n + m), Space O(1)

---

### 🔥 **Pattern 4: Find Middle Element** ⭐⭐

**Use Fast & Slow Pointers (Tortoise & Hare)!**

```python
def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node of a linked list.
    
    Visual:
    1 → 2 → 3 → 4 → 5 → ∅
            ↑ (Middle)
    
    Logic: Slow moves 1 step, Fast moves 2 steps.
    When Fast reaches the end, Slow is at the middle.
    """
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Test
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle = find_middle(head)
print(middle.val)  # 3
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 5: Remove Nth Node from End** ⭐⭐

```python
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove the nth node from the end of the list.
    
    Example: Remove 2nd from end
    Before: 1 → 2 → 3 → 4 → 5 → ∅
    After:  1 → 2 → 3 → 5 → ∅ (removed 4)
    
    Logic: Two pointers with n-gap between them.
    """
    dummy = ListNode(0, head)
    first = second = dummy
    
    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the node
    second.next = second.next.next
    
    return dummy.next
```

**Complexity:** Time O(n), Space O(1)

---

## 🔁 Part C: Doubly Linked List (DLL)

### 💡 What is a Doubly Linked List?

Each node has **two pointers**: `prev` and `next`.

**Visual:**
```
     ┌─────┐    ┌─────┐    ┌─────┐
∅ ←─ │ 10  │ ←→ │ 20  │ ←→ │ 30  │ ─→ ∅
     └─────┘    └─────┘    └─────┘
```

**Advantages:**
- ✅ Traverse in **both directions**
- ✅ Delete a node in O(1) if you have its reference

### 💻 Implementation

```python
class DLLNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.prev: Optional[DLLNode] = None
        self.next: Optional[DLLNode] = None

class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DLLNode] = None
        self.tail: Optional[DLLNode] = None
    
    def append(self, val: int) -> None:
        """Add node at the end."""
        new_node = DLLNode(val)
        
        if not self.head:
            self.head = self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    
    def delete_node(self, node: DLLNode) -> None:
        """Delete a node given its reference (O(1)!)"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
```

---

### 🔥 **Pattern 6: LRU Cache** ⭐⭐⭐

**The Ultimate DLL Application!**

```python
class LRUCache:
    """
    Least Recently Used Cache using Doubly Linked List + HashMap.
    
    Operations:
    - get(key): O(1)
    - put(key, value): O(1)
    
    When cache is full, remove the LRU (least recently used) item.
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DLLNode
        
        # Dummy head and tail for easier operations
        self.head = DLLNode(0)
        self.tail = DLLNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: DLLNode) -> None:
        """Remove node from DLL."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_front(self, node: DLLNode) -> None:
        """Add node right after head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        """Get value and mark as recently used."""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        """Put key-value pair into cache."""
        if key in self.cache:
            self._remove(self.cache[key])
        
        new_node = DLLNode(value)
        new_node.key = key  # Store key in node for eviction
        self.cache[key] = new_node
        self._add_to_front(new_node)
        
        # Evict LRU if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

# Test
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))    # 1 (mark as used)
lru.put(3, 3)        # Evicts key 2
print(lru.get(2))    # -1 (not found)
```

**Complexity:** Both `get` and `put` are O(1)!

---

## 🐢🐇 Part D: Floyd's Cycle Detection

### 🎯 The Cycle Problem

**Question:** Does a linked list have a cycle (loop)?

```
Visual with cycle:
1 → 2 → 3 → 4
    ↑       ↓
    6 ← 5 ←┘

Visual without cycle:
1 → 2 → 3 → 4 → ∅
```

### 🔥 **Pattern 7: Detect Cycle (Tortoise & Hare)** ⭐⭐⭐

```python
def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if linked list has a cycle.
    
    Logic: Two pointers at different speeds.
    - Slow (🐢): 1 step at a time
    - Fast (🐇): 2 steps at a time
    
    If there's a cycle, they WILL meet!
    If there's no cycle, fast will reach ∅.
    """
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle detected!
    
    return False

# Test
# Create cycle: 1 → 2 → 3 → 4 → back to 2
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle!

print(has_cycle(head))  # True
```

**Complexity:** Time O(n), Space O(1)

**Why does it work?**
- If there's a cycle, think of it as a circular track
- Fast runner will eventually "lap" the slow runner
- They meet at some point inside the cycle

---

### 🔥 **Pattern 8: Find Cycle Start** ⭐⭐⭐

**Advanced:** Not just detect, but find WHERE the cycle begins!

```python
def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the node where the cycle begins.
    
    Algorithm:
    1. Use Floyd's to detect cycle and find meeting point
    2. Move one pointer to head
    3. Move both pointers 1 step at a time
    4. They meet at the cycle start!
    
    Math proof: Distance(head→cycle_start) = Distance(meet→cycle_start)
    """
    slow = fast = head
    
    # Step 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # Step 2: Find cycle start
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # Cycle start
    
    return None  # No cycle
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 9: Linked List Palindrome** ⭐⭐

**Clever use of Fast & Slow!**

```python
def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is a palindrome.
    
    Example: 1 → 2 → 3 → 2 → 1 → ∅ (True)
    
    Algorithm:
    1. Find middle using slow/fast pointers
    2. Reverse second half
    3. Compare first half with reversed second half
    """
    if not head or not head.next:
        return True
    
    # Step 1: Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse second half
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp
    
    # Step 3: Compare
    left, right = head, prev
    while right:  # right is shorter for odd-length lists
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    
    return True
```

**Complexity:** Time O(n), Space O(1)

---

## 🧪 Challenge Zone

> 🎯 **Master these classic LL problems!**

### 🟢 **Problem 1: Remove Duplicates from Sorted List**
Input: `1 → 1 → 2 → 3 → 3 → ∅`  
Output: `1 → 2 → 3 → ∅`

**💡 Hint:** Single pass, check `current.val == current.next.val`.

<details>
<summary>Click for solution</summary>

```python
def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head
```
</details>

---

### 🟡 **Problem 2: Intersection of Two Lists**
Find the node where two linked lists intersect.

**💡 Hint:** Use two pointers, switch heads when reaching end.

<details>
<summary>Click for solution</summary>

```python
def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Visual:
    A: 1 → 2 ↘
               8 → 9 → ∅
    B: 3 → 4 ↗
    Intersection at node with value 8.
    """
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA  # Either intersection or None
```
</details>

---

### 🟠 **Problem 3: Reorder List**
`L0 → L1 → L2 → ... → Ln-1 → Ln → ∅`  
Reorder to: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

**💡 Hint:** Find middle, reverse second half, merge alternately.

<details>
<summary>Click for solution</summary>

```python
def reorder_list(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # Merge two halves
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
```
</details>

---

### 🔴 **Problem 4: Reverse Nodes in k-Group**
Reverse every k nodes. If remaining < k, leave as is.

**💡 Hint:** Recursive approach or iterative with careful pointer management.

<details>
<summary>Click for solution</summary>

```python
def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Check if we have k nodes left
    curr = head
    for _ in range(k):
        if not curr:
            return head
        curr = curr.next
    
    # Reverse first k nodes
    prev, curr = None, head
    for _ in range(k):
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # Recursively reverse remaining
    head.next = reverse_k_group(curr, k)
    
    return prev
```
</details>

---

## 📈 Complexity Summary

| Operation | Singly LL | Doubly LL | Array |
|-----------|-----------|-----------|-------|
| **Access** | O(n) | O(n) | O(1) |
| **Search** | O(n) | O(n) | O(n) |
| **Insert at Head** | O(1) | O(1) | O(n) |
| **Insert at Tail** | O(n) without tail | O(1) | O(1) amortized |
| **Delete node** | O(n) | O(1) with reference | O(n) |

---

## 🎓 Key Takeaways

✅ **Linked Lists** trade random access for flexible insertion/deletion  
✅ **Dummy Nodes** simplify edge cases (empty list, delete head)  
✅ **Two Pointers** solve 80% of LL problems (slow/fast, left/right)  
✅ **Tortoise & Hare** detects cycles in O(n) time, O(1) space  
✅ **Doubly Linked Lists** enable O(1) deletion and bidirectional traversal  
✅ **LRU Cache** is the ultimate DLL application combining HashMap + DLL  

---

## 🚀 Pattern Recognition Guide

| Problem Type | Pattern to Use |
|--------------|----------------|
| Reverse list | Iterative 3-pointer or Recursive |
| Find middle | Slow/Fast pointers |
| Detect cycle | Floyd's Tortoise & Hare |
| Nth from end | Two pointers with gap |
| Merge sorted lists | Dummy node + comparison |
| Palindrome check | Find middle + Reverse + Compare |

---

## 🔗 Next Steps

Now that you've mastered linked lists:
- **Stacks & Queues** (Can be implemented using LL!)
- **Trees** (Binary trees are linked structures!)
- **Graphs** (Adjacency lists use LL!)

**Remember:** Master pointer manipulation, and you unlock trees, graphs, and advanced data structures! 💪

---

*Happy Linking! 🎉*