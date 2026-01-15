# 🔄 Pattern 5: Cyclic Sort

## 🎯 **The Magic of O(N) Sorting**

> 💡 **The Secret:** When an array contains numbers in a fixed range (1 to N or 0 to N), we can sort it in **O(N)** time instead of O(N log N)!

### 📊 **Complexity Comparison**
| Algorithm | Time Complexity | Space | Use Case |
|-----------|----------------|-------|----------|
| **Merge Sort** | O(N log N) | O(N) | General sorting |
| **Quick Sort** | O(N log N) avg | O(log N) | General sorting |
| **Cyclic Sort** | O(N) | O(1) | Numbers in range 1 to N |

---

## 🚗 **The Parking Lot Analogy**

### 🅿️ **Concept**
Imagine a parking lot with numbered spots: **0, 1, 2, 3, 4**

Cars are also numbered: **0, 1, 2, 3, 4**

**Goal:** Park each car in its matching spot number!

```
Initial State:
[Car 3] [Car 0] [Car 2] [Car 1] [Car 4]
 Spot 0  Spot 1  Spot 2  Spot 3  Spot 4

Target State:
[Car 0] [Car 1] [Car 2] [Car 3] [Car 4]
 Spot 0  Spot 1  Spot 2  Spot 3  Spot 4
```

### 🔑 **The Rule**
- **1-based range (1 to N):** If `nums[i] != i + 1`, swap to correct position
- **0-based range (0 to N):** If `nums[i] != i`, swap to correct position

---

## 🎬 **Visual Walkthrough**

### 📝 **Problem:** Sort `[3, 1, 5, 4, 2]` (Range: 1 to 5)
**Target:** `[1, 2, 3, 4, 5]`

**Note:** Number `x` belongs at index `x - 1`

```python
# Initial: [3, 1, 5, 4, 2]
#          i=0

# Step 1: Index 0, Value = 3
# Does 3 belong at index 0? No → belongs at index 2
# Swap index 0 ↔ index 2
# Result: [5, 1, 3, 4, 2]
#          ↑ stay here

# Step 2: Index 0, Value = 5
# Does 5 belong at index 0? No → belongs at index 4
# Swap index 0 ↔ index 4
# Result: [2, 1, 3, 4, 5]
#          ↑ stay here

# Step 3: Index 0, Value = 2
# Does 2 belong at index 0? No → belongs at index 1
# Swap index 0 ↔ index 1
# Result: [1, 2, 3, 4, 5]
#          ↑ stay here

# Step 4: Index 0, Value = 1
# Does 1 belong at index 0? YES! ✓
# Move to index 1 →

# Step 5-7: All remaining elements are in correct positions
# Final: [1, 2, 3, 4, 5] ✓
```

---

## 💻 **Core Implementation**

### 🔧 **Basic Cyclic Sort (1 to N)**
```python
def cyclic_sort(nums):
    """
    Sort array containing numbers from 1 to N
    Time: O(N) | Space: O(1)
    """
    i = 0
    while i < len(nums):
        # Calculate correct index for current number
        correct_index = nums[i] - 1
        
        # If number is not at correct position, swap
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            # Number is in correct position, move forward
            i += 1
    
    return nums

# Test
print(cyclic_sort([3, 1, 5, 4, 2]))  # [1, 2, 3, 4, 5]
```

### 🔧 **Cyclic Sort (0 to N)**
```python
def cyclic_sort_zero_based(nums):
    """
    Sort array containing numbers from 0 to N
    Time: O(N) | Space: O(1)
    """
    i = 0
    while i < len(nums):
        correct_index = nums[i]
        
        # Check bounds and correct position
        if nums[i] < len(nums) and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    return nums

# Test
print(cyclic_sort_zero_based([3, 0, 2, 1]))  # [0, 1, 2, 3]
```

---

## 🎯 **Problem Variations**

### 📌 **Problem 1: Find Missing Number**
```python
def find_missing_number(nums):
    """
    Find the missing number in range 0 to N
    Input: [4, 0, 3, 1] → Output: 2
    """
    i = 0
    n = len(nums)
    
    # Cyclic sort
    while i < n:
        correct_index = nums[i]
        if nums[i] < n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    # Find missing number
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n  # If all present, missing number is N

# Test
print(find_missing_number([4, 0, 3, 1]))  # 2
print(find_missing_number([0, 1, 2, 3]))  # 4
```

### 📌 **Problem 2: Find All Missing Numbers**
```python
def find_all_missing(nums):
    """
    Find all missing numbers in range 1 to N
    Input: [2, 3, 1, 8, 2, 3, 5, 1] → Output: [4, 6, 7]
    """
    i = 0
    
    # Cyclic sort
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    # Find all missing numbers
    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing.append(i + 1)
    
    return missing

# Test
print(find_all_missing([2, 3, 1, 8, 2, 3, 5, 1]))  # [4, 6, 7]
```

### 📌 **Problem 3: Find Duplicate Number**
```python
def find_duplicate(nums):
    """
    Find the duplicate number in range 1 to N
    Input: [1, 3, 4, 2, 2] → Output: 2
    """
    i = 0
    
    while i < len(nums):
        correct_index = nums[i] - 1
        
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    # Find duplicate
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]
    
    return -1

# Test
print(find_duplicate([1, 3, 4, 2, 2]))  # 2
```

### 📌 **Problem 4: Find All Duplicates**
```python
def find_all_duplicates(nums):
    """
    Find all duplicates in range 1 to N
    Input: [4, 3, 2, 7, 8, 2, 3, 1] → Output: [2, 3]
    """
    i = 0
    
    # Cyclic sort
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    # Find duplicates
    duplicates = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicates.append(nums[i])
    
    return duplicates

# Test
print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # [2, 3]
```

---

## 🧠 **Why is This O(N)?**

### 🤔 **The Question**
"We're swapping inside a loop! Shouldn't this be O(N²)?"

### ✅ **The Answer**
**Key Insight:** Each number is swapped **at most once** to its correct position.

```python
# Analysis:
# - Outer loop: Visits each index once → O(N)
# - Inner swaps: Each element moves to correct position once → O(N) total
# - Total: O(N) + O(N) = O(N)

# Example: [3, 1, 5, 4, 2]
# Number 3: Swapped once from index 0 → index 2 (DONE)
# Number 5: Swapped once from index 0 → index 4 (DONE)
# Number 2: Swapped once from index 0 → index 1 (DONE)
# Each number: Maximum 1 swap to reach home!
```

---

## 🎯 **Pattern Recognition**

### 🔍 **When to Use Cyclic Sort**
Look for these **keywords** in problem descriptions:

✅ **Use Cyclic Sort if:**
- "Array contains numbers from **1 to N**"
- "Array contains numbers from **0 to N**"
- "Find **missing** number(s)"
- "Find **duplicate** number(s)"
- "Numbers in a **fixed range**"
- "In-place with **O(1) space**"

❌ **Don't use if:**
- Numbers are not in a continuous range
- Array contains negative numbers
- Need to preserve original order
- Numbers are outside 0 to N range

---

## 📝 **Drill Questions**

### ❓ **Question 1: First Swap**
**Problem:** Array `[3, 0, 1]`, Range: 0 to 3, One number missing

**Walk through the first swap:**
```python
# Initial: [3, 0, 1]
#          i=0

# Index 0 has value 3
# Where does 3 belong? Index 3
# Swap index 0 ↔ index 3

# But wait! Index 3 doesn't exist (array length is 3)
# This means 3 is OUT OF RANGE
# Skip it and move forward

# Result after handling: [3, 0, 1] → Move to index 1
```

**Answer:**
```python
def solve_question_1():
    nums = [3, 0, 1]
    i = 0
    
    # First iteration
    correct_index = nums[0]  # 3
    
    # Check if 3 is within bounds
    if correct_index < len(nums):  # 3 < 3? False
        # Skip, move forward
        i += 1
    
    # Now at index 1, value = 0
    # 0 belongs at index 0
    # Swap: [0, 3, 1]
    
    return "After first meaningful swap: [0, 3, 1]"
```

### ❓ **Question 2: Why O(N) Not O(N²)?**

**Answer:**
```
🔑 Key Insight: Each element is swapped AT MOST ONCE to its final position.

Proof:
1. When we swap nums[i] to its correct position, it stays there
2. We never revisit that position to swap it again
3. Total swaps ≤ N (one per element)
4. Loop iterations ≤ 2N (worst case: visit each index twice)
5. Overall: O(N) time complexity

Example:
[3, 1, 5, 4, 2]
- Element 3: Swapped once (index 0 → index 2) ✓
- Element 5: Swapped once (index 0 → index 4) ✓
- Element 2: Swapped once (index 0 → index 1) ✓
- Element 1: Already correct ✓
- Element 4: Already correct ✓

Total swaps: 3 (not N²)
```

### ❓ **Question 3: Pattern Recognition**

**What keyword screams "Use Cyclic Sort"?**

**Answer: B) "Array contains numbers 1 to N"**

```python
# Explanation:
pattern_indicators = {
    "A) Find the max sum": "❌ Use Kadane's Algorithm or DP",
    "B) Array contains numbers 1 to N": "✅ CYCLIC SORT!",
    "C) Linked List cycle": "❌ Use Floyd's Cycle Detection"
}

# The magic phrase: "numbers from 1 to N" or "0 to N"
# This tells us each number has a HOME (its index)
```

---

## 🏆 **LeetCode Problems**

### 🟢 **Easy**
1. **Missing Number (LC-268)** - Find missing number in 0 to N
2. **Find All Numbers Disappeared (LC-448)** - Find all missing

### 🟡 **Medium**
3. **Find Duplicate Number (LC-287)** - Find the duplicate
4. **Find All Duplicates (LC-442)** - Find all duplicates
5. **Set Mismatch (LC-645)** - Find duplicate and missing

---

## 🎯 **Key Takeaways**

### ✅ **Core Concepts**
- **Time Complexity:** O(N) - Linear time sorting!
- **Space Complexity:** O(1) - In-place algorithm
- **Key Condition:** Numbers must be in range 0 to N or 1 to N
- **Swap Strategy:** Each element swapped at most once

### 💡 **Problem-Solving Template**
```python
def cyclic_sort_template(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1  # or nums[i] for 0-based
        
        # Bounds check and position check
        if 0 <= correct_index < len(nums) and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    # Post-processing: Find missing/duplicate
    for i in range(len(nums)):
        if nums[i] != i + 1:  # or i for 0-based
            return i + 1  # or process as needed
```

---

*Sort in O(N), master the pattern! 🔄*