# 🚶♂️ Queues: The Line of Fairness

![Queue](https://img.shields.io/badge/Topic-Queue-teal?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Foundation-green?style=for-the-badge)
![Time](https://img.shields.io/badge/Study_Time-2_Hours-orange?style=for-the-badge)

> **"First come, first served"**
> 
> You've mastered the Stack's discipline of LIFO. Now we embrace fairness with **FIFO** - First In, First Out. If the Stack is a narrow tube, the Queue is a **horizontal pipe** where elements enter from one end and exit from the other.

Welcome to the world of **ordered processing** and **fair scheduling**.

---

## 🧠 1. The Blueprint (Concept & Memory)

### 🎫 The Analogy
Imagine a **line at a coffee shop** or **cars at a toll booth**:
- People join the line at the **back** (rear/tail)
- People are served from the **front** (head)
- First person in line gets served first
- This is **FIFO**: First-In, First-Out

### 🧮 The RAM View
A Queue maintains **two access points** unlike Stack's single point:

#### 🔗 Linked List-Based Queue
```
Queue (Linked List Implementation):
FRONT → [5] → [12] → [8] → [23] ← REAR
        ↑                    ↑
    Dequeue here         Enqueue here
```

#### 📦 Array-Based Queue (Circular)
```
Circular Queue (Array Implementation):
┌─────┬─────┬─────┬─────┬─────┐
│ 23  │     │     │  5  │ 12  │
├─────┼─────┼─────┼─────┼─────┤
│ [0] │ [1] │ [2] │ [3] │ [4] │
└─────┴─────┴─────┴─────┴─────┘
  ↑                 ↑     ↑
REAR              FRONT   8
```

### 🖥️ System Usage
Queues are everywhere in computing:
- **CPU scheduling** - processes wait their turn
- **Print queues** - documents printed in order
- **Network packets** - data transmission fairness

### ⚡ Why Queues?
Perfect for **fair resource allocation**:
- Ensures no process "cuts in line"
- Maintains order of arrival
- Prevents starvation of waiting processes

---

## ⚙️ 2. The Operations (Enqueue & Dequeue Logic)

Queues use **Enqueue** (add) and **Dequeue** (remove):

| 🔧 Operation | 🧠 Logic | ⏱️ Time Complexity |
|:-------------|:---------|:-------------------|
| **➕ Enqueue** | Add element to the rear/back | **O(1)** ⚡ |
| **➖ Dequeue** | Remove element from the front | **O(1)** ⚡ |
| **👁️ Front** | Look at front element without removing | **O(1)** ⚡ |
| **👁️ Rear** | Look at rear element without removing | **O(1)** ⚡ |
| **🔍 Search** | Must check all elements linearly | **O(n)** 🐌 |

### 📊 Visual: Queue Operations
```
Initial: Empty Queue

Enqueue 5:   Enqueue 12:  Enqueue 8:   Dequeue:     Dequeue:
┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐
│  5  │      │ 12  │      │  8  │      │  8  │      │     │
└─────┘      ├─────┤      ├─────┤      ├─────┤      └─────┘
FRONT        │  5  │      │ 12  │      │ 12  │      
REAR         └─────┘      ├─────┤      └─────┘      
             FRONT        │  5  │      FRONT        
             REAR         └─────┘      REAR         
                          FRONT                     
                          REAR                      
```

---

## 🐍 3. The Python Construction

Using **Linked List** approach for optimal performance:

### 🧱 Node Class
```python
from typing import Any, Optional

class Node:
    """🔗 Queue node"""
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional['Node'] = None
```

### 🚶♂️ Queue Implementation
```python
class Queue:
    """🚶♂️ The Line of Fairness"""
    
    def __init__(self) -> None:
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None
        self.size = 0

    def enqueue(self, data: Any) -> None:
        """➕ Add to the rear - O(1)"""
        new_node = Node(data)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1

    def dequeue(self) -> Any:
        """➖ Remove from the front - O(1)"""
        if self.is_empty():
            raise IndexError("🚨 Queue Underflow: The line is empty")
        
        dequeued_data = self.front.data
        self.front = self.front.next
        
        if self.front is None:  # Queue became empty
            self.rear = None
        
        self.size -= 1
        return dequeued_data

    def peek_front(self) -> Any:
        """👁️ View the front - O(1)"""
        if self.is_empty():
            return None
        return self.front.data

    def peek_rear(self) -> Any:
        """👁️ View the rear - O(1)"""
        if self.is_empty():
            return None
        return self.rear.data

    def is_empty(self) -> bool:
        return self.front is None

    def __len__(self) -> int:
        return self.size

    def display(self) -> None:
        """👁️ Visualize the queue"""
        if self.is_empty():
            print("🚶♂️ Empty Queue")
            return
        
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("🚶♂️ Queue (front → rear):")
        print("FRONT → " + " → ".join(elements) + " ← REAR")
```

### 🔄 Circular Queue (Array-Based)
```python
class CircularQueue:
    """🔄 Space-efficient array-based queue"""
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, data: Any) -> None:
        """➕ Add to rear - O(1)"""
        if self.is_full():
            raise OverflowError("🚨 Queue Overflow: Line is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1

    def dequeue(self) -> Any:
        """➖ Remove from front - O(1)"""
        if self.is_empty():
            raise IndexError("🚨 Queue Underflow: Line is empty")
        
        data = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity
```

### 🧪 Quick Test
```python
# Test our Queue
print_queue = Queue()
print_queue.enqueue("Document1.pdf")
print_queue.enqueue("Photo.jpg")
print_queue.enqueue("Report.docx")

print_queue.display()
# 🚶♂️ Queue (front → rear):
# FRONT → Document1.pdf → Photo.jpg → Report.docx ← REAR

print(f"Now printing: {print_queue.dequeue()}")  # Document1.pdf
print(f"Next in line: {print_queue.peek_front()}")  # Photo.jpg
```

---

## 🎯 4. The Engineer's Choice

### ✅ **USE Queues when:**
- 🖨️ **Task scheduling** - Print queues, CPU process scheduling
- 🌐 **Breadth-First Search (BFS)** - Level-by-level tree/graph traversal
- 🔄 **Buffer management** - Streaming data, network packets
- 🎮 **Game mechanics** - Turn-based systems, event processing
- 📞 **Call centers** - First caller gets first service

### ❌ **AVOID Queues when:**
- ↩️ Need **LIFO behavior** - Use Stack instead
- 🎯 Need **random access** to middle elements - Use Array
- 🔍 Frequent **searching** through elements - Wrong tool choice
- ⚡ Need **priority-based** processing - Use Priority Queue

---

## 📈 5. Complexity Summary

| Operation | Time Complexity | Space Complexity |
|:----------|:---------------:|:----------------:|
| Enqueue   | O(1) ⚡         | O(1)             |
| Dequeue   | O(1) ⚡         | O(1)             |
| Front     | O(1) ⚡         | O(1)             |
| Rear      | O(1) ⚡         | O(1)             |
| Search    | O(n) 🐌         | O(1)             |

---

## 🌟 6. Real-World Applications

### 🖨️ Print Queue System
```python
def print_manager():
    """Simple print queue simulation"""
    printer = Queue()
    
    # Add print jobs
    printer.enqueue("Resume.pdf")
    printer.enqueue("Invoice.docx")
    printer.enqueue("Photo.jpg")
    
    # Process jobs in order
    while not printer.is_empty():
        current_job = printer.dequeue()
        print(f"🖨️ Printing: {current_job}")
```

### 🌳 Breadth-First Search
```python
def bfs_traversal(graph, start):
    """BFS using queue for level-order traversal"""
    visited = set()
    queue = Queue()
    
    queue.enqueue(start)
    visited.add(start)
    
    while not queue.is_empty():
        node = queue.dequeue()
        print(f"Visiting: {node}")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.add(neighbor)
```

---

## 🆚 7. Stack vs Queue Comparison

| Feature | Stack (LIFO) | Queue (FIFO) |
|:--------|:------------:|:------------:|
| **Access Pattern** | Last In, First Out | First In, First Out |
| **Access Points** | One (top) | Two (front & rear) |
| **Use Cases** | Undo, DFS, Recursion | Scheduling, BFS, Buffering |
| **Real World** | Stack of plates | Line at store |

---

## 🚀 Next Adventure

> **"From linear restrictions to hierarchical freedom"**

You've mastered linear data structures with different access patterns:
- **Arrays**: Random access, contiguous memory
- **Linked Lists**: Dynamic size, scattered memory  
- **Stacks**: LIFO discipline
- **Queues**: FIFO fairness

Ready to break free from linear thinking and explore **Trees** - where data branches out in hierarchical relationships?

**Coming Next:** 🌳 **Trees** - Hierarchical Data Structures

---

*Happy Coding! 🎉*