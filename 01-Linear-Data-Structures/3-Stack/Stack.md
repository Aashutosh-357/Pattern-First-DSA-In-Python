# 📚 Stacks: The Tower of Control

![Stack](https://img.shields.io/badge/Topic-Stack-red?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Foundation-green?style=for-the-badge)
![Time](https://img.shields.io/badge/Study_Time-2_Hours-orange?style=for-the-badge)

> **"The power of discipline"**
> 
> If the Array is a row of lockers and the Linked List is a scavenger hunt, the **Stack** is a narrow, vertical tube. Here we learn that sometimes restrictions create power.

Welcome to the world of **LIFO** - where the last one in is the first one out.

---

## 🧠 1. The Blueprint (Concept & Memory)

### 🍽️ The Analogy
Imagine a **stack of dinner plates** or a **can of tennis balls**:
- You can only add a new plate to the **top**
- You can only remove the plate that is currently on the **top**
- Want the bottom plate? Remove every plate above it first
- This is **LIFO**: Last-In, First-Out

### 🧮 The RAM View
A Stack is a **"restricted"** structure built on existing foundations:

#### 📦 Array-Based Stack
```
Stack (Array Implementation):
┌─────┬─────┬─────┬─────┬─────┐
│  5  │ 12  │  8  │ 23  │     │
├─────┼─────┼─────┼─────┼─────┤
│ [0] │ [1] │ [2] │ [3] │ [4] │
└─────┴─────┴─────┴─────┴─────┘
                    ↑
                   TOP
```

#### 🔗 Linked List-Based Stack
```
Stack (Linked List Implementation):
TOP → [23] → [8] → [12] → [5] → NULL
      ↑
   Only access point
```

### 🖥️ The System Stack
Your computer uses a physical stack in RAM:
- `functionA()` calls `functionB()` → push return address
- `functionB()` finishes → pop to return to `functionA()`

### ⚡ Why Stacks?
Perfect when **order of reversal matters**:
- Prevents accidental access to middle elements
- Ensures process integrity (like "Undo" operations)

---

## ⚙️ 2. The Operations (Push & Pop Logic)

In Stacks, we don't use CRUD - we use **Push** and **Pop**:

| 🔧 Operation | 🧠 Logic | ⏱️ Time Complexity |
|:-------------|:---------|:-------------------|
| **📤 Push** | Place new element on the very top | **O(1)** ⚡ |
| **📥 Pop** | Remove top element and return it | **O(1)** ⚡ |
| **👁️ Peek** | Look at top element without removing | **O(1)** ⚡ |
| **🔍 Search** | Must pop everything above target | **O(n)** 🐌 |

### 📊 Visual: Stack Operations
```
Initial: Empty Stack

Push 5:     Push 12:    Push 8:     Pop:        Pop:
┌─────┐     ┌─────┐     ┌─────┐     ┌─────┐     ┌─────┐
│     │     │     │     │  8  │ ←   │     │     │     │
├─────┤     ├─────┤     ├─────┤     ├─────┤     ├─────┤
│     │     │ 12  │     │ 12  │     │ 12  │     │     │
├─────┤     ├─────┤     ├─────┤     ├─────┤     ├─────┤
│  5  │ ←   │  5  │     │  5  │     │  5  │     │  5  │ ←
└─────┘     └─────┘     └─────┘     └─────┘     └─────┘
 TOP         TOP         TOP         TOP         TOP
```

---

## 🐍 3. The Python Construction

Using **Linked List** approach for guaranteed O(1) operations without resizing:

### 🧱 Node Class
```python
from typing import Any, Optional

class Node:
    """🔗 Stack node"""
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional['Node'] = None
```

### 📚 Stack Implementation
```python
class Stack:
    """📚 The Tower of Control"""
    
    def __init__(self) -> None:
        self.top: Optional[Node] = None
        self.size = 0

    def push(self, data: Any) -> None:
        """📤 Add to the top - O(1)"""
        new_node = Node(data)
        new_node.next = self.top  # Point to old top
        self.top = new_node       # Become new top
        self.size += 1

    def pop(self) -> Any:
        """📥 Remove from the top - O(1)"""
        if self.is_empty():
            raise IndexError("🚨 Stack Underflow: The tube is empty")
        
        popped_data = self.top.data
        self.top = self.top.next  # Move top down
        self.size -= 1
        return popped_data

    def peek(self) -> Any:
        """👁️ View the top - O(1)"""
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None

    def __len__(self) -> int:
        return self.size

    def display(self) -> None:
        """👁️ Visualize the stack"""
        if self.is_empty():
            print("📚 Empty Stack")
            return
        
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("📚 Stack (top → bottom):")
        for i, element in enumerate(elements):
            prefix = "TOP → " if i == 0 else "      "
            print(f"{prefix}[{element}]")
```

### 🧪 Quick Test
```python
# Test our Stack
history = Stack()
history.push("google.com")
history.push("github.com")
history.push("stackoverflow.com")

history.display()
# 📚 Stack (top → bottom):
# TOP → [stackoverflow.com]
#       [github.com]
#       [google.com]

print(f"Back button: {history.pop()}")  # stackoverflow.com
print(f"Current page: {history.peek()}")  # github.com
```

---

## 🎯 4. The Engineer's Choice

### ✅ **USE Stacks when:**
- ↩️ **Undo/Redo mechanisms** - Every action pushed, undo pops last state
- 🧮 **Expression evaluation** - Balanced parentheses `(){}[]`, math expressions
- 🔄 **Backtracking** - Maze solving, AI pathfinding (save current path)
- 🌳 **Depth-First Search (DFS)** - Go as deep as possible first
- 📞 **Function call management** - System stack for recursion

### ❌ **AVOID Stacks when:**
- 🎯 Need to **access middle elements** - Use Array instead
- 🚶‍♂️ Need **First-Come, First-Served** processing - Use Queue instead
- 🔍 Frequent **searching** through elements - Wrong tool choice
- 📊 Need **random access** to any position

---

## 📈 5. Complexity Summary

| Operation | Time Complexity | Space Complexity |
|:----------|:---------------:|:----------------:|
| Push      | O(1) ⚡         | O(1)             |
| Pop       | O(1) ⚡         | O(1)             |
| Peek      | O(1) ⚡         | O(1)             |
| Search    | O(n) 🐌         | O(1)             |

---

## 🌟 6. Real-World Applications

### 🌐 Browser History
```python
browser_history = Stack()
browser_history.push("google.com")
browser_history.push("github.com")
# Back button = pop()
```

### 🧮 Expression Evaluation
```python
def is_balanced(expression: str) -> bool:
    """Check if parentheses are balanced"""
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()

print(is_balanced("({[]})"))  # True
print(is_balanced("({[})"))   # False
```

---

## 🚀 Next Adventure

> **"From the Tower of Control to the Line of Fairness"**

The Stack teaches us discipline through restriction. But what happens when we want to be **fair**? What if the first person to arrive should be the first person served?

**Coming Next:** 🚶‍♂️ **Queue** - The Line of Fairness (FIFO)

---


*Happy Coding! 🎉*