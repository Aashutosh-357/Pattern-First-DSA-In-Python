# 📦 Arrays & Dynamic Arrays - The Foundation

> *"An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together."*

🎯 **Mission:** Master the most fundamental data structure in programming. Arrays are the building blocks of almost every algorithm you'll encounter. Understanding them deeply is non-negotiable!

---

## 📚 Table of Contents

| Section | Topics Covered |
|---------|----------------|
| **Part A: Array Fundamentals** | Memory layout, Time complexity, Static vs Dynamic |
| **Part B: Core Operations** | Insert, Delete, Search, Traverse |
| **Part C: Two Pointers** | Same direction, Opposite direction, Fast & Slow |
| **Part D: Sliding Window** | Fixed size, Variable size, Optimization patterns |
| **Part E: Prefix Sum** | Range queries, Subarray sums |
| **Part F: Kadane's Algorithm** | Maximum subarray sum |

---

## 🧱 Part A: Array Fundamentals

### 💡 What is an Array?

An array is a **contiguous block of memory** that stores elements of the **same type**.

**Visual Representation:**
```
Memory Address:  1000   1004   1008   1012   1016
                  ↓      ↓      ↓      ↓      ↓
Array:          [ 10  |  20  |  30  |  40  |  50 ]
Index:            0      1      2      3      4
```

**Key Properties:**
- ✅ **Random Access:** O(1) - Direct access using index
- ✅ **Cache Friendly:** Contiguous memory = better CPU cache utilization
- ❌ **Fixed Size:** (Static arrays) Cannot grow/shrink
- ❌ **Expensive Insert/Delete:** O(n) - May need to shift elements

### 🎯 The Bookshelf Analogy

Think of an array as a **bookshelf** with numbered slots:

```
Slot:    0      1      2      3      4
       [📕]   [📗]   [📘]   [📙]   [📔]
```

- **Access:** "Get book at slot 2" → O(1) - Direct!
- **Insert:** "Add book at slot 1" → O(n) - Must shift all books right!
- **Delete:** "Remove book at slot 2" → O(n) - Must shift all books left!

### 🔢 Static vs Dynamic Arrays

| Feature | Static Array | Dynamic Array (Python `list`) |
|---------|--------------|-------------------------------|
| **Size** | Fixed at creation | Grows/shrinks automatically |
| **Memory** | Allocated once | Reallocates when full |
| **Append** | Not possible | O(1) amortized |
| **Example** | C/C++ arrays | Python `list`, Java `ArrayList` |

### 💻 Python Arrays (Lists)

```python
from typing import List

# Creating arrays
arr1: List[int] = [1, 2, 3, 4, 5]
arr2: List[int] = [0] * 5  # [0, 0, 0, 0, 0]
arr3: List[int] = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Access
print(arr1[0])    # 1 (first element)
print(arr1[-1])   # 5 (last element)
print(arr1[1:4])  # [2, 3, 4] (slicing)

# Length
print(len(arr1))  # 5
```

---

## 🛠️ Part B: Core Operations

### 1️⃣ **Traversal - O(n)**

```python
def traverse_array(arr: List[int]) -> None:
    """Visit each element once."""
    # Method 1: Index-based
    for i in range(len(arr)):
        print(f"Index {i}: {arr[i]}")
    
    # Method 2: Direct iteration (Pythonic)
    for num in arr:
        print(num)
    
    # Method 3: With index and value
    for i, num in enumerate(arr):
        print(f"Index {i}: {num}")

# Test
traverse_array([10, 20, 30])
```

**Complexity:** Time O(n), Space O(1)

---

### 2️⃣ **Search - O(n) Linear, O(log n) Binary**

```python
def linear_search(arr: List[int], target: int) -> int:
    """
    Find target in unsorted array.
    Returns index if found, -1 otherwise.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    """
    Find target in SORTED array.
    Returns index if found, -1 otherwise.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test
print(linear_search([4, 2, 7, 1, 9], 7))  # 2
print(binary_search([1, 2, 4, 7, 9], 7))  # 3
```

---

### 3️⃣ **Insert - O(n)**

```python
def insert_at_index(arr: List[int], index: int, value: int) -> List[int]:
    """
    Insert value at specific index.
    
    Visual: Insert 99 at index 2
    Before: [10, 20, 30, 40]
                    ↑
    After:  [10, 20, 99, 30, 40]
    """
    # Method 1: Using list method
    arr.insert(index, value)
    return arr

    # Method 2: Manual (for understanding)
    # arr.append(0)  # Make space
    # for i in range(len(arr) - 1, index, -1):
    #     arr[i] = arr[i - 1]
    # arr[index] = value

# Test
arr = [10, 20, 30, 40]
insert_at_index(arr, 2, 99)
print(arr)  # [10, 20, 99, 30, 40]
```

**Complexity:** Time O(n), Space O(1)

---

### 4️⃣ **Delete - O(n)**

```python
def delete_at_index(arr: List[int], index: int) -> List[int]:
    """
    Delete element at specific index.
    
    Visual: Delete at index 2
    Before: [10, 20, 30, 40, 50]
                    ↑
    After:  [10, 20, 40, 50]
    """
    # Method 1: Using list method
    arr.pop(index)
    return arr

    # Method 2: Manual (for understanding)
    # for i in range(index, len(arr) - 1):
    #     arr[i] = arr[i + 1]
    # arr.pop()

# Test
arr = [10, 20, 30, 40, 50]
delete_at_index(arr, 2)
print(arr)  # [10, 20, 40, 50]
```

**Complexity:** Time O(n), Space O(1)

---

## 👉👈 Part C: Two Pointers Pattern

### 🎯 What is Two Pointers?

A technique using **two indices** to traverse an array efficiently, often reducing O(n²) to O(n).

**Three Main Types:**

1. **Opposite Direction** (left ← → right)
2. **Same Direction** (slow → fast →)
3. **Fast & Slow** (tortoise 🐢 & hare 🐇)

---

### 🔥 **Pattern 1: Opposite Direction** ⭐

**Use Case:** Palindrome check, Two Sum (sorted array), Reverse array

```python
def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome using two pointers.
    
    Visual: "racecar"
    left →  r a c e c a r  ← right
            ↓           ↓
            Compare and move inward
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 2: Two Sum (Sorted Array)** ⭐⭐

```python
def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Find two numbers that sum to target in SORTED array.
    
    Example: arr = [1, 2, 3, 4, 6], target = 6
    
    Visual:
    [1, 2, 3, 4, 6]
     ↑           ↑
     L           R
     
    1 + 6 = 7 > 6 → Move R left
    1 + 4 = 5 < 6 → Move L right
    2 + 4 = 6 ✓
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return [-1, -1]

# Test
print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # [1, 3] → arr[1]=2, arr[3]=4
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 3: Same Direction (Remove Duplicates)** ⭐⭐

```python
def remove_duplicates(arr: List[int]) -> int:
    """
    Remove duplicates from SORTED array in-place.
    Returns new length.
    
    Example: [1, 1, 2, 2, 3, 4, 4]
    
    Visual:
    [1, 1, 2, 2, 3, 4, 4]
     ↑  ↑
     S  F
     
    Slow: Unique elements position
    Fast: Exploring new elements
    """
    if not arr:
        return 0
    
    slow = 0  # Position for next unique element
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1  # Length of unique elements

# Test
arr = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(arr)
print(arr[:length])  # [1, 2, 3, 4]
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 4: Move Zeros to End** ⭐

```python
def move_zeros(arr: List[int]) -> None:
    """
    Move all zeros to end while maintaining order of non-zeros.
    
    Example: [0, 1, 0, 3, 12]
    Result:  [1, 3, 12, 0, 0]
    
    Logic: Slow pointer tracks position for next non-zero.
    """
    slow = 0  # Position for next non-zero
    
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1

# Test
arr = [0, 1, 0, 3, 12]
move_zeros(arr)
print(arr)  # [1, 3, 12, 0, 0]
```

**Complexity:** Time O(n), Space O(1)

---

## 🪟 Part D: Sliding Window Pattern

### 🎯 What is Sliding Window?

A technique to process **subarrays/substrings** by maintaining a "window" that slides through the array.

**Two Main Types:**

1. **Fixed Size Window** - Window size is constant
2. **Variable Size Window** - Window expands/shrinks based on condition

---

### 🔥 **Pattern 1: Fixed Size Window (Max Sum)** ⭐

```python
def max_sum_subarray(arr: List[int], k: int) -> int:
    """
    Find maximum sum of any subarray of size k.
    
    Example: arr = [2, 1, 5, 1, 3, 2], k = 3
    
    Visual:
    [2, 1, 5, 1, 3, 2]
     -------            Sum = 8
        -------         Sum = 7
           -------      Sum = 9 ← Max
              -------   Sum = 6
    """
    if len(arr) < k:
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Test
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 2: Variable Size Window (Smallest Subarray)** ⭐⭐

```python
def min_subarray_sum(arr: List[int], target: int) -> int:
    """
    Find length of smallest subarray with sum >= target.
    
    Example: arr = [2, 3, 1, 2, 4, 3], target = 7
    Result: 2 (subarray [4, 3])
    
    Logic:
    - Expand window (right++) until sum >= target
    - Shrink window (left++) while sum >= target
    """
    min_length = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]  # Expand window
        
        # Shrink window while condition met
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

# Test
print(min_subarray_sum([2, 3, 1, 2, 4, 3], 7))  # 2
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 3: Longest Substring Without Repeating** ⭐⭐⭐

```python
def longest_unique_substring(s: str) -> int:
    """
    Find length of longest substring without repeating characters.
    
    Example: "abcabcbb"
    Result: 3 ("abc")
    
    Logic: Use set to track characters in current window.
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test
print(longest_unique_substring("abcabcbb"))  # 3
print(longest_unique_substring("bbbbb"))     # 1
print(longest_unique_substring("pwwkew"))    # 3
```

**Complexity:** Time O(n), Space O(min(n, m)) where m = charset size

---

## 📊 Part E: Prefix Sum Pattern

### 🎯 What is Prefix Sum?

A technique to **precompute cumulative sums** for fast range queries.

**Formula:**
```
prefix[i] = arr[0] + arr[1] + ... + arr[i]
sum(i, j) = prefix[j] - prefix[i-1]
```

**Visual:**
```
Array:     [3, 1, 4, 2, 5]
Prefix:    [3, 4, 8, 10, 15]
           
Sum(1, 3) = prefix[3] - prefix[0]
          = 10 - 3 = 7
          = arr[1] + arr[2] + arr[3]
          = 1 + 4 + 2 = 7 ✓
```

---

### 🔥 **Pattern 1: Range Sum Query** ⭐

```python
class RangeSumQuery:
    """
    Precompute prefix sums for O(1) range queries.
    """
    def __init__(self, arr: List[int]):
        self.prefix = [0]
        for num in arr:
            self.prefix.append(self.prefix[-1] + num)
    
    def sum_range(self, left: int, right: int) -> int:
        """
        Return sum of elements from index left to right (inclusive).
        
        Example: arr = [1, 2, 3, 4, 5]
        sum_range(1, 3) = 2 + 3 + 4 = 9
        """
        return self.prefix[right + 1] - self.prefix[left]

# Test
rsq = RangeSumQuery([1, 2, 3, 4, 5])
print(rsq.sum_range(1, 3))  # 9
print(rsq.sum_range(0, 4))  # 15
```

**Complexity:** 
- Preprocessing: O(n)
- Query: O(1)
- Space: O(n)

---

### 🔥 **Pattern 2: Subarray Sum Equals K** ⭐⭐

```python
def subarray_sum_k(arr: List[int], k: int) -> int:
    """
    Count subarrays with sum equal to k.
    
    Example: arr = [1, 1, 1], k = 2
    Result: 2 (subarrays [1,1] at positions 0-1 and 1-2)
    
    Logic: Use hashmap to store prefix sums.
    If (current_sum - k) exists, we found a subarray!
    """
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}  # sum: frequency
    
    for num in arr:
        current_sum += num
        
        # Check if (current_sum - k) exists
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        
        # Update prefix sum frequency
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
    
    return count

# Test
print(subarray_sum_k([1, 1, 1], 2))        # 2
print(subarray_sum_k([1, 2, 3], 3))        # 2
print(subarray_sum_k([1, -1, 1, -1], 0))   # 4
```

**Complexity:** Time O(n), Space O(n)

---

## 🏆 Part F: Kadane's Algorithm - Maximum Subarray Sum

### 🎯 The Problem

Find the **contiguous subarray** with the **largest sum**.

**Example:**
```
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Max subarray: [4, -1, 2, 1] → sum = 6
```

---

### 🔥 **Kadane's Algorithm** ⭐⭐⭐

```python
def max_subarray_sum(arr: List[int]) -> int:
    """
    Find maximum sum of any contiguous subarray.
    
    Logic (Greedy):
    - Keep adding elements to current sum
    - If current sum becomes negative, reset to 0
    - Track maximum sum seen so far
    
    Visual: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    current: -2  1  -2  4   3  5  6   1  5
    max:     -2  1   1  4   4  5  6   6  6
    """
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend current subarray or start new one
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Alternative: More intuitive version
def max_subarray_sum_v2(arr: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        # Reset if current sum becomes negative
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

# Test
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray_sum([1]))                               # 1
print(max_subarray_sum([5, 4, -1, 7, 8]))                  # 23
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Kadane's with Subarray Indices** ⭐⭐

```python
def max_subarray_with_indices(arr: List[int]) -> tuple:
    """
    Return (max_sum, start_index, end_index).
    """
    max_sum = arr[0]
    current_sum = arr[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end

# Test
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start, end = max_subarray_with_indices(arr)
print(f"Max sum: {max_sum}")
print(f"Subarray: {arr[start:end+1]}")
# Output: Max sum: 6, Subarray: [4, -1, 2, 1]
```

---

## 🧪 Challenge Zone

> 🎯 **Test your array mastery with these problems!**

### 🟢 **Problem 1: Reverse Array In-Place**
Reverse an array without using extra space.

**💡 Hint:** Two pointers from opposite ends.

<details>
<summary>Click for solution</summary>

```python
def reverse_array(arr: List[int]) -> None:
    """Reverse array in-place using two pointers."""
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Test
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # [5, 4, 3, 2, 1]
```
</details>

---

### 🟡 **Problem 2: Container With Most Water**
Given heights array, find two lines that form container with max water.

**💡 Hint:** Two pointers, move the shorter line inward.

<details>
<summary>Click for solution</summary>

```python
def max_area(height: List[int]) -> int:
    """
    Find maximum water container area.
    
    Area = min(height[left], height[right]) × (right - left)
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width
        max_water = max(max_water, area)
        
        # Move the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Test
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
```
</details>

---

### 🟠 **Problem 3: Product of Array Except Self**
Return array where `output[i]` = product of all elements except `arr[i]`.
**Constraint:** No division allowed!

**💡 Hint:** Use prefix and suffix products.

<details>
<summary>Click for solution</summary>

```python
def product_except_self(arr: List[int]) -> List[int]:
    """
    Calculate product of all elements except current.
    
    Example: [1, 2, 3, 4]
    Output:  [24, 12, 8, 6]
    
    Logic:
    - Left product: product of all elements to the left
    - Right product: product of all elements to the right
    - Result[i] = left[i] × right[i]
    """
    n = len(arr)
    result = [1] * n
    
    # Calculate left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= arr[i]
    
    # Calculate right products and multiply
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]
    
    return result

# Test
print(product_except_self([1, 2, 3, 4]))  # [24, 12, 8, 6]
```
</details>

---

### 🔴 **Problem 4: Trapping Rain Water**
Calculate how much water can be trapped after raining.

**💡 Hint:** For each position, water = min(max_left, max_right) - height[i]

<details>
<summary>Click for solution</summary>

```python
def trap_rain_water(height: List[int]) -> int:
    """
    Calculate trapped water using two pointers.
    
    Example: [0,1,0,2,1,0,1,3,2,1,2,1]
    Water trapped: 6
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    
    return water

# Test
print(trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
```
</details>

---

### 🏆 **Problem 5: Maximum Product Subarray**
Find contiguous subarray with largest product.

**💡 Hint:** Track both max and min (negative × negative = positive!)

<details>
<summary>Click for solution</summary>

```python
def max_product_subarray(arr: List[int]) -> int:
    """
    Find maximum product of contiguous subarray.
    
    Example: [2, 3, -2, 4]
    Max product: 6 (subarray [2, 3])
    
    Trick: Track both max and min (negatives can flip!)
    """
    if not arr:
        return 0
    
    max_prod = min_prod = result = arr[0]
    
    for i in range(1, len(arr)):
        num = arr[i]
        
        # If negative, swap max and min
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        
        result = max(result, max_prod)
    
    return result

# Test
print(max_product_subarray([2, 3, -2, 4]))     # 6
print(max_product_subarray([-2, 0, -1]))       # 0
print(max_product_subarray([-2, 3, -4]))       # 24
```
</details>

---

## 📈 Time Complexity Summary

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| **Access** | O(1) | Direct indexing |
| **Search** | O(n) linear, O(log n) binary | Binary requires sorted |
| **Insert/Delete** | O(n) | May need to shift elements |
| **Append** | O(1) amortized | Dynamic arrays |
| **Two Pointers** | O(n) | Single pass |
| **Sliding Window** | O(n) | Each element visited twice max |
| **Prefix Sum** | O(n) preprocessing, O(1) query | Trade space for time |
| **Kadane's** | O(n) | Single pass |

---

## 🎓 Key Takeaways

✅ **Arrays** provide O(1) random access but O(n) insert/delete  
✅ **Two Pointers** reduces O(n²) to O(n) for many problems  
✅ **Sliding Window** efficiently processes subarrays  
✅ **Prefix Sum** enables O(1) range queries  
✅ **Kadane's Algorithm** solves maximum subarray in O(n)  

---

## 🚀 Pattern Recognition Guide

| Problem Type | Pattern to Use |
|--------------|----------------|
| Sorted array, find pair | Two Pointers (opposite) |
| Remove duplicates in-place | Two Pointers (same direction) |
| Subarray of size k | Sliding Window (fixed) |
| Smallest/longest subarray with condition | Sliding Window (variable) |
| Range sum queries | Prefix Sum |
| Maximum subarray sum | Kadane's Algorithm |
| All subarrays sum to k | Prefix Sum + HashMap |

---

## 🔗 Next Steps

Now that you've mastered arrays, you're ready for:
- **Strings** (similar patterns apply!)
- **Linked Lists** (dynamic insertion/deletion)
- **Stacks & Queues** (built on arrays)

**Remember:** Arrays are the foundation. Master these patterns, and 50% of interview problems become trivial! 💪

---

*Happy Coding! 🎉*