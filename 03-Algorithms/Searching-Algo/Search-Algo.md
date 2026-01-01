# 🔍 Searching Algorithms: The Art of Finding

![Searching](https://img.shields.io/badge/Topic-Searching_Algorithms-indigo?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)
![Time](https://img.shields.io/badge/Study_Time-3_Hours-orange?style=for-the-badge)

> **"The Detective's Toolkit"**
> 
> In the vast landscape of data, finding a specific element is like being a detective in a library. Do you check every book one by one, or do you use the catalog system? The choice of search strategy can mean the difference between seconds and hours.

Welcome to the world of **intelligent searching** - where strategy beats brute force.

---

## 🧠 1. The Blueprint (Concept & Strategy)

### 🕵️ The Analogy
Searching is like finding a specific book in a library:
- **Linear Search**: Check every shelf, every book, one by one
- **Binary Search**: Use the catalog system and section numbers to jump directly

### 🎯 The Core Question
**"How do we minimize the number of comparisons needed to find our target?"**

The answer depends on:
- Is our data **sorted** or **unsorted**?
- Do we have **random access** (arrays) or **sequential access** (linked lists)?
- Are we searching **once** or **multiple times**?

---

## 🔍 2. Linear Search: The Brute Force Detective

### 📖 The Concept
Check **every element sequentially** until you find the target or reach the end.

### 🎯 When to Use
- **Unsorted data** (no other choice)
- **Small datasets** (overhead not worth it)
- **Linked lists** (no random access available)
- **One-time searches** (sorting cost > search benefit)

### 📊 Visual Representation
```
Array: [64, 34, 25, 12, 22, 11, 90]
Target: 22

Step 1: Check 64 ≠ 22 ❌
Step 2: Check 34 ≠ 22 ❌  
Step 3: Check 25 ≠ 22 ❌
Step 4: Check 12 ≠ 22 ❌
Step 5: Check 22 = 22 ✅ Found at index 4!
```

### 🐍 Implementation
```python
from typing import List, Optional

def linear_search(arr: List[int], target: int) -> Optional[int]:
    """🔍 Linear Search - O(n) time, O(1) space"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found at index i
    return None  # Not found

# Test
numbers = [64, 34, 25, 12, 22, 11, 90]
result = linear_search(numbers, 22)
print(f"Found at index: {result}")  # Found at index: 4
```

---

## ⚡ 3. Binary Search: The Divide & Conquer Master

### 📖 The Concept
**"Divide and Conquer"** on **sorted arrays**:
1. Check the **middle** element
2. If target is smaller → search **left half**
3. If target is larger → search **right half**
4. Repeat until found or search space is empty

### 🎯 When to Use
- **Sorted data** (prerequisite!)
- **Large datasets** (logarithmic advantage shines)
- **Frequent searches** (sorting cost amortized)
- **Arrays/lists** with random access

### 📊 Visual Representation
```
Sorted Array: [11, 12, 22, 25, 34, 64, 90]
Target: 25

Step 1: [11, 12, 22, |25|, 34, 64, 90]  mid=25, target=25 ✅ Found!

If target was 22:
Step 1: [11, 12, 22, |25|, 34, 64, 90]  mid=25 > 22, go left
Step 2: [11, |12|, 22]                  mid=12 < 22, go right  
Step 3: [22]                            mid=22 = 22 ✅ Found!
```

### 🐍 Implementation
```python
def binary_search(arr: List[int], target: int) -> Optional[int]:
    """⚡ Binary Search - O(log n) time, O(1) space"""
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid  # Found!
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half
    
    return None  # Not found

# Test
sorted_numbers = [11, 12, 22, 25, 34, 64, 90]
result = binary_search(sorted_numbers, 25)
print(f"Found at index: {result}")  # Found at index: 3
```

### 🔄 Recursive Binary Search
```python
def binary_search_recursive(arr: List[int], target: int, low: int = 0, high: int = None) -> Optional[int]:
    """🔄 Recursive Binary Search - O(log n) time, O(log n) space"""
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return None  # Base case: not found
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
```

---

## 📈 4. Complexity Analysis

| Algorithm | Best Case | Average Case | Worst Case | Space |
|:----------|:---------:|:------------:|:----------:|:-----:|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) |
| **Binary (Recursive)** | O(1) | O(log n) | O(log n) | O(log n) |

### 📊 Performance Comparison
```
For n = 1,000,000 elements:
Linear Search:   Up to 1,000,000 comparisons
Binary Search:   Up to 20 comparisons (log₂ 1,000,000 ≈ 20)

That's a 50,000x improvement! 🚀
```

---

## 🎯 5. The Engineer's Choice

### ✅ **Use Linear Search when:**
- 📊 **Unsorted data** (no preprocessing possible)
- 🔗 **Linked lists** (no random access)
- 📏 **Small datasets** (n < 100, overhead not worth it)
- 🔄 **One-time search** (sorting cost > search benefit)

### ✅ **Use Binary Search when:**
- ✅ **Sorted data** available
- 📈 **Large datasets** (logarithmic advantage)
- 🔄 **Multiple searches** (amortize sorting cost)
- 🎯 **Arrays/vectors** with random access

---

## 🌟 6. Advanced Search Variants

### 🎯 Find First/Last Occurrence
```python
def find_first_occurrence(arr: List[int], target: int) -> Optional[int]:
    """Find leftmost occurrence in sorted array with duplicates"""
    low, high = 0, len(arr) - 1
    result = None
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            high = mid - 1  # Continue searching left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result
```

### 🔍 Search in Rotated Array
```python
def search_rotated_array(arr: List[int], target: int) -> Optional[int]:
    """Binary search in rotated sorted array"""
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return None
```

---

## 🧪 7. Practical Applications

### 🌐 **Real-World Usage:**
- 📚 **Database indexing** - B-trees use binary search principles
- 🔍 **Search engines** - Inverted indexes for fast lookups
- 🎮 **Game development** - Collision detection, pathfinding
- 💰 **Financial systems** - Price lookups, trading algorithms
- 🧬 **Bioinformatics** - DNA sequence matching

---

## 🚀 Next Adventure

> **"From finding elements to arranging them"**

You've mastered the art of **finding** data efficiently. But what if the data isn't organized in the first place? How do we transform chaos into order?

**Coming Next:** 🔄 **Sorting Algorithms** - The Art of Organization

---

*Happy Coding! 🎉*