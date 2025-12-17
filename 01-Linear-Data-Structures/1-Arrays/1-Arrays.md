# 📊 Level 1: Linear Data Structures
## 🔢 Topic 1: Arrays & Dynamic Arrays

> Welcome to the most used data structure in the world! In Python, we call them **Lists** (`[1, 2, 3]`), but under the hood, they are **Dynamic Arrays**.

---

## 🧠 Step 1: The Concept (The RAM Parking Lot)

🏢 Imagine your computer's RAM is a massive street with parking spots numbered `0, 1, 2, 3...`

When you create an array `arr = [10, 20, 30]`:

1. 🅿️ The computer finds **3 empty spots right next to each other** (Contiguous Memory)
2. 📦 It puts `10` in the first, `20` in the second, `30` in the third
3. 📍 It remembers the address of the *start*

### ⚡ Why is Access O(1)?

Because of **Math**, not magic! 🧮

If I want `arr[2]`, the computer calculates:
```
Start_Address + (2 × Size_of_Item)
```
It jumps straight there. No searching! 🎯

---

## ⚙️ Step 2: The Operations (Insert is Expensive!)

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| 📖 **Reading (Get)** | `O(1)` | Fast access by index |
| ✏️ **Writing (Update)** | `O(1)` | Direct assignment `arr[0] = 99` |
| ➕ **Inserting/Deleting** | `O(N)` | Requires shifting elements |

### 🎬 Why Insert/Delete is Slow?

Imagine 5 friends sitting in cinema seats. You want to sit at index 0:

- Friend at index 4 → moves to 5
- Friend at index 3 → moves to 4  
- Friend at index 2 → moves to 3
- Everyone shifts! 😅

**Visual Example:**
```
[A, B, C, _, _]  →  Insert 'X' at index 0  →  [X, A, B, C, _]
```
*We had to touch A, B, and C to move them.* 🔄

---

## 🐍 Step 3: Python's Secret (Dynamic Arrays)

In C++ or Java, arrays have **fixed size**. But in Python, `list.append()` works forever! How? 🤔

### 🔄 The "Doubling Strategy":

1. 📦 Python creates an array of size 4
2. 📈 You fill it up
3. ➕ You try to add a 5th item
4. 🚀 Python creates a **new** array of size 8 (double!), copies old items, deletes old array

#### ⏱️ Amortized Time Complexity:
- ✅ Most `append()` calls are `O(1)`
- 🔄 Occasionally (when full), it takes `O(N)` to copy
- 📊 **On average: `O(1)`**

---

## 💻 Step 4: Coding the Operations

Let's explore Python's array manipulation syntax:

```python
# 1. 🏗️ Initialization
nums = [1, 2, 3, 4, 5]

# 2. 📖 Access - O(1)
print(nums[2])  # Output: 3

# 3. ✏️ Update - O(1)
nums[2] = 99
# nums is now [1, 2, 99, 4, 5]

# 4. ➕ Append (Add to end) - Average O(1)
nums.append(6) 
# [1, 2, 99, 4, 5, 6]

# 5. 🔄 Insert (Add to middle) - O(N) ⚠️ AVOID IN LOOPS
nums.insert(0, 100) 
# Everyone shifts right: [100, 1, 2, 99, 4, 5, 6]

# 6. 🗑️ Delete (Remove from middle) - O(N) ⚠️ AVOID IN LOOPS
nums.pop(0) 
# Everyone shifts left: [1, 2, 99, 4, 5, 6]
```

---

## 🎯 Step 5: Checkpoint Problems

To master arrays, you must master the **Index**! 📍

### 🔄 Problem 1 (Easy): Reverse Array

**Task:** Write a function that reverses a list **in-place** (without creating a new list)

```
📥 Input:  [1, 2, 3, 4, 5]
📤 Output: [5, 4, 3, 2, 1]
```

💡 **Hint:** Use the "Two Pointer" technique. One finger on start, one on end. Swap and move inward!

### 🔢 Problem 2 (Medium): Move Zeros

**Task:** Move all `0`s to the end while maintaining relative order of non-zero elements. Do this **in-place** (O(1) Space)

```
📥 Input:  [0, 1, 0, 3, 12]
📤 Output: [1, 3, 12, 0, 0]
```

💡 **Hint:** Don't focus on zeros. Focus on non-zeros. If you find a non-zero, where should it go?

---

## 🚀 Ready to Code?

**Show me your solutions for these two problems!** Focus on clean, readable syntax. 🎨