# 🧮 Basic Mathematics for DSA

> *"Mathematics is not about numbers, equations, or algorithms: it is about understanding."* - William Paul Thurston

🎯 **Mission:** Master the essential mathematical concepts that power efficient algorithms. These aren't abstract theories—they're the building blocks of every optimization you'll ever make!

---

## 📚 Table of Contents

| Topic | Symbol | Real-World Impact |
|-------|--------|-------------------|
| **Logarithms** | `log(n)` | Binary Search, Tree Heights, Divide & Conquer |
| **Arithmetic/Geometric Progressions** | `AP/GP` | Loop Analysis, Exponential Growth, Amortized Analysis |
| **Modular Arithmetic** | `%` | Hash Tables, Circular Arrays, Cryptography |

---

## 🌲 Part A: Logarithms - The Tree Climber's Secret

### 🤔 What is a Logarithm?

**Simple Definition:** A logarithm answers the question:  
> *"How many times do I need to **divide** a number by a base to reach 1?"*

**Mathematical Notation:**
```
log₂(8) = 3    because    2³ = 8
log₁₀(1000) = 3    because    10³ = 1000
```

### 🎯 The Phonebook Analogy

Imagine finding "Smith" in a 1,000-page phonebook:

| Method | Pages Checked | Complexity |
|--------|---------------|------------|
| **Linear Search** (page by page) | ~500 pages | O(n) |
| **Binary Search** (split in half) | ~10 pages | O(log n) |

**Why 10 pages?**
```
1000 → 500 → 250 → 125 → 63 → 32 → 16 → 8 → 4 → 2 → 1
  ↑      ↑     ↑     ↑     ↑    ↑    ↑   ↑   ↑   ↑   ↑
Step 1   2     3     4     5    6    7   8   9   10
```

**Result:** `log₂(1000) ≈ 10` steps!

### 🔢 Logarithm Properties (The Cheat Codes)

```python
# Property 1: Product Rule
log(a × b) = log(a) + log(b)

# Property 2: Quotient Rule
log(a / b) = log(a) - log(b)

# Property 3: Power Rule
log(aⁿ) = n × log(a)

# Property 4: Base Change
log_b(a) = log(a) / log(b)

# Property 5: Identity
log_b(b) = 1
log_b(1) = 0
```

### 💻 Python Implementation

#### 🎲 **Pattern 1: Counting Digits**
```python
import math

def count_digits(n: int) -> int:
    """
    Count digits in a number using logarithms.
    
    Logic: 
    - 100 has 3 digits → log₁₀(100) = 2 → digits = 2 + 1 = 3
    - 9999 has 4 digits → log₁₀(9999) ≈ 3.99 → digits = 3 + 1 = 4
    """
    if n == 0:
        return 1
    return math.floor(math.log10(abs(n))) + 1

# Test
print(count_digits(12345))  # Output: 5
print(count_digits(999))    # Output: 3
```

**Complexity:** O(1) - Instant calculation! 🚀

#### 🌳 **Pattern 2: Tree Height Calculation**
```python
def max_tree_height(nodes: int) -> int:
    """
    Calculate max height of a complete binary tree.
    
    Visual:
         1           Height 0 (1 node)
        / \
       2   3         Height 1 (2 nodes)
      / \ / \
     4 5 6 7        Height 2 (4 nodes)
    
    Pattern: Height = log₂(nodes + 1) - 1
    """
    return math.floor(math.log2(nodes + 1))

# Test
print(max_tree_height(7))   # Output: 3
print(max_tree_height(15))  # Output: 4
```

#### ⚡ **Pattern 3: Power of Two Checker**
```python
def is_power_of_two(n: int) -> bool:
    """
    Check if n is a power of 2 using logarithms.
    
    Logic: If log₂(n) is an integer, n is a power of 2.
    """
    if n <= 0:
        return False
    
    log_val = math.log2(n)
    return log_val == int(log_val)

# Test
print(is_power_of_two(16))   # True (2⁴)
print(is_power_of_two(18))   # False
```

---

## 📊 Part B: Arithmetic & Geometric Progressions

### 🎯 Arithmetic Progression (AP)

**Definition:** A sequence where each term increases by a **constant difference**.

**Formula:**
```
Sequence: a, a+d, a+2d, a+3d, ...
nth term: aₙ = a + (n-1)d
Sum of n terms: Sₙ = n/2 × (2a + (n-1)d)
                   = n/2 × (first + last)
```

#### 🎪 **Visual Example: Staircase**
```
Step 1: 🧍 (height 2)
Step 2: 🧍🧍 (height 4)
Step 3: 🧍🧍🧍 (height 6)
Step 4: 🧍🧍🧍🧍 (height 8)

Pattern: 2, 4, 6, 8, ... (d = 2)
```

#### 💻 **Python Implementation**
```python
def ap_sum(first: int, diff: int, n: int) -> int:
    """
    Calculate sum of first n terms of an AP.
    
    Example: Sum of 1+2+3+...+100
    """
    last = first + (n - 1) * diff
    return n * (first + last) // 2

# Famous Problem: Sum of 1 to 100
print(ap_sum(1, 1, 100))  # Output: 5050
```

**Real-World Use:** Analyzing loops with constant increments!
```python
# This loop runs in O(n²) time
total = 0
for i in range(1, n+1):
    for j in range(i):  # Runs i times
        total += 1

# Total iterations: 1+2+3+...+n = n(n+1)/2 = O(n²)
```

### 🚀 Geometric Progression (GP)

**Definition:** A sequence where each term is **multiplied** by a constant ratio.

**Formula:**
```
Sequence: a, ar, ar², ar³, ...
nth term: aₙ = a × rⁿ⁻¹
Sum of n terms: Sₙ = a(rⁿ - 1) / (r - 1)    [when r ≠ 1]
```

#### 🎪 **Visual Example: Cell Division**
```
Hour 0: 🦠 (1 cell)
Hour 1: 🦠🦠 (2 cells)
Hour 2: 🦠🦠🦠🦠 (4 cells)
Hour 3: 🦠🦠🦠🦠🦠🦠🦠🦠 (8 cells)

Pattern: 1, 2, 4, 8, ... (r = 2)
```

#### 💻 **Python Implementation**
```python
def gp_sum(first: int, ratio: int, n: int) -> int:
    """
    Calculate sum of first n terms of a GP.
    
    Example: 1 + 2 + 4 + 8 + ... (n terms)
    """
    if ratio == 1:
        return first * n
    
    return first * (ratio**n - 1) // (ratio - 1)

# Example: Sum of powers of 2
print(gp_sum(1, 2, 10))  # Output: 1023 (2¹⁰ - 1)
```

**Real-World Use:** Analyzing divide-and-conquer algorithms!
```python
# Merge Sort Time Complexity Analysis
# Level 0: n work
# Level 1: n/2 + n/2 = n work
# Level 2: n/4 + n/4 + n/4 + n/4 = n work
# ...
# Total levels: log(n)
# Total work: n × log(n) = O(n log n)
```

---

## 🔄 Part C: Modular Arithmetic - The Clock Math

### 🕐 The Clock Analogy

Imagine a **12-hour clock**:
```
    12
 9      3
    6
```

**Key Insight:**
- 13 o'clock = 1 o'clock (13 % 12 = 1)
- 25 o'clock = 1 o'clock (25 % 12 = 1)
- This "wrap-around" is **modular arithmetic**!

### 🎯 The Modulo Operator (`%`)

**Definition:** `a % b` gives the **remainder** when `a` is divided by `b`.

```python
10 % 3 = 1    # 10 = 3×3 + 1
17 % 5 = 2    # 17 = 5×3 + 2
8 % 4 = 0     # 8 = 4×2 + 0 (perfectly divisible)
```

### 🔢 Modular Arithmetic Properties

```python
# Property 1: Addition
(a + b) % m = ((a % m) + (b % m)) % m

# Property 2: Multiplication
(a × b) % m = ((a % m) × (b % m)) % m

# Property 3: Subtraction
(a - b) % m = ((a % m) - (b % m) + m) % m

# Property 4: Power
(aⁿ) % m = ((a % m)ⁿ) % m
```

### 💻 Python Implementation

#### 🎲 **Pattern 1: Even/Odd Detection**
```python
def is_even(n: int) -> bool:
    """Check if number is even using modulo."""
    return n % 2 == 0

# Test
print(is_even(42))  # True
print(is_even(13))  # False
```

#### 🎡 **Pattern 2: Circular Array Navigation** ⭐
```python
from typing import List

def rotate_array(arr: List[int], k: int) -> List[int]:
    """
    Rotate array to the right by k steps.
    
    Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]
    
    Logic: new_index = (old_index + k) % len(arr)
    """
    n = len(arr)
    result = [0] * n
    
    for i in range(n):
        new_index = (i + k) % n
        result[new_index] = arr[i]
    
    return result

# Test
print(rotate_array([1,2,3,4,5], 2))  # [4,5,1,2,3]
```

**Complexity:** O(n) time, O(n) space

#### 🔐 **Pattern 3: Large Number Modulo** ⭐⭐
```python
def power_mod(base: int, exp: int, mod: int) -> int:
    """
    Calculate (base^exp) % mod efficiently.
    
    Problem: 2^1000 % 13 → Direct calculation overflows!
    Solution: Use modular exponentiation
    
    Logic: (a × b) % m = ((a % m) × (b % m)) % m
    """
    result = 1
    base = base % mod
    
    while exp > 0:
        # If exp is odd, multiply base with result
        if exp % 2 == 1:
            result = (result * base) % mod
        
        # exp must be even now
        exp = exp // 2
        base = (base * base) % mod
    
    return result

# Test
print(power_mod(2, 10, 1000))  # 24 (2^10 = 1024, 1024 % 1000 = 24)
print(power_mod(3, 50, 7))     # 2
```

**Complexity:** O(log exp) - Blazing fast! 🚀

#### 🎯 **Pattern 4: Check Divisibility**
```python
def is_divisible_by(n: int, divisor: int) -> bool:
    """Check if n is divisible by divisor."""
    return n % divisor == 0

# Test
print(is_divisible_by(100, 5))   # True
print(is_divisible_by(101, 5))   # False
```

---

## 🧪 Challenge Zone

> 🎯 **Test your understanding with these brain teasers!**

### 🟢 **Problem 1: Logarithm Puzzle**
Without using a calculator, estimate: `log₂(1,000,000)`

**💡 Hint:** 2¹⁰ = 1024 ≈ 1000

<details>
<summary>Click for solution</summary>

```python
# 1,000,000 = 1000 × 1000 = 2^10 × 2^10 = 2^20
# Therefore: log₂(1,000,000) ≈ 20
```
</details>

---

### 🟡 **Problem 2: AP Sum**
Find the sum: `5 + 10 + 15 + 20 + ... + 500`

**💡 Hint:** Use the AP sum formula!

<details>
<summary>Click for solution</summary>

```python
def solve():
    # First term a = 5, difference d = 5
    # Last term = 500
    # Number of terms: n = (500 - 5)/5 + 1 = 100
    
    n = 100
    first = 5
    last = 500
    
    total = n * (first + last) // 2
    return total

print(solve())  # Output: 25250
```
</details>

---

### 🟠 **Problem 3: Circular Array**
You have a circular array of size `N = 7`. Currently at index `5`. Move backward `3` steps. What's the new index?

**💡 Hint:** `(current - steps + N) % N`

<details>
<summary>Click for solution</summary>

```python
def circular_move_backward(current: int, steps: int, size: int) -> int:
    # Add size to handle negative numbers correctly
    return (current - steps + size) % size

print(circular_move_backward(5, 3, 7))  # Output: 2
```
</details>

---

### 🔴 **Problem 4: GP Growth**
A bacteria colony doubles every hour. Starting with 1 bacterium, how many will there be after 24 hours?

**💡 Hint:** This is a GP with r = 2

<details>
<summary>Click for solution</summary>

```python
def bacteria_growth(hours: int) -> int:
    # GP: 1, 2, 4, 8, ...
    # nth term = a × r^(n-1) = 1 × 2^(hours)
    return 2 ** hours

print(bacteria_growth(24))  # Output: 16,777,216
print(f"{bacteria_growth(24):,}")  # Formatted: 16,777,216
```
</details>

---

### 🏆 **Problem 5: Modular Power**
Calculate `7^256 % 13` efficiently (without overflow).

**💡 Hint:** Use the `power_mod` function!

<details>
<summary>Click for solution</summary>

```python
def solve():
    return power_mod(7, 256, 13)

print(solve())  # Output: 9
```
</details>

---

## 📈 Why This Matters in DSA

| Concept | DSA Application | Example |
|---------|-----------------|---------|
| **Logarithms** | Binary Search, Tree Heights | Finding element in sorted array |
| **AP** | Loop Analysis | Nested loops complexity |
| **GP** | Divide & Conquer | Merge Sort, Binary Tree levels |
| **Modulo** | Hash Functions, Circular Buffers | Hash Table indexing |

---

## 🎓 Key Takeaways

✅ **Logarithms** reduce multiplication to addition (log properties)  
✅ **AP** helps analyze linear growth patterns  
✅ **GP** helps analyze exponential growth patterns  
✅ **Modular Arithmetic** enables efficient large number calculations  

---

## 🚀 Next Steps

Now that you've mastered the mathematical foundations, you're ready to tackle:
- **Arrays & Two Pointers** (Level 1)
- **Binary Search** (Level 3)
- **Dynamic Programming** (Level 5)

**Remember:** Every optimization you'll ever make relies on these mathematical principles!

---

*Happy Learning! 🎉*