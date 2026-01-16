# 🔄 Level 2: Recursion - The Logic Builder

## 🎯 **Welcome to Level 2: The Logic Builders**

> 💡 **Mental Shift:** We stop thinking linearly (loops) and start thinking **recursively**. This is the foundation for Trees, Graphs, and Dynamic Programming.

---

## 🪆 **The Russian Nesting Dolls Analogy**

### 🎭 **The Concept**
Imagine you have a sealed Russian doll. You want to find if there's a diamond inside the smallest doll.

```
🪆 Big Doll
  └─ 🪆 Medium Doll
      └─ 🪆 Small Doll
          └─ 🪆 Tiny Doll
              └─ 💎 Diamond!
```

**Process:**
1. Open the big doll → No diamond, but there's a smaller doll
2. Open the smaller doll → No diamond, but there's an even smaller doll
3. Continue...
4. **Base Case:** Reach the tiny solid doll → Check it!

### 🔑 **Definition**
**Recursion** is a function that **calls itself** to solve a problem by breaking it into smaller versions of the same problem.

---

## 🧬 **The Anatomy of Recursion**

### ⚠️ **Two Critical Components**
Every recursive function MUST have these, or you'll get a Stack Overflow:

| Component | Purpose | Example |
|-----------|---------|----------|
| **Base Case** | The emergency brake - when to stop | `if n == 0: return 1` |
| **Recursive Relation** | The shrink ray - make problem smaller | `return n * factorial(n-1)` |

---

## 📚 **Visualizing the Call Stack**

### 🍽️ **The Plates Analogy**
When you call a function, Python places a "plate" (Stack Frame) in memory.

```
┌─────────────┐
│  fact(3)    │ ← Top plate (current)
├─────────────┤
│  fact(2)    │ ← Waiting...
├─────────────┤
│  fact(1)    │ ← Waiting...
├─────────────┤
│  fact(0)    │ ← Base case reached!
└─────────────┘
```

**Rule:** You cannot finish the bottom plate until the top plate is removed.

---

## 🎬 **Example: Factorial**

### 📐 **Mathematical Definition**
```
factorial(n) = n × factorial(n-1)
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### 🔍 **Execution Trace for fact(3)**

```python
# Call Stack Visualization

Step 1: fact(3) → "What is 3 × fact(2)?" [PAUSE]
  ↓
Step 2: fact(2) → "What is 2 × fact(1)?" [PAUSE]
  ↓
Step 3: fact(1) → "What is 1 × fact(0)?" [PAUSE]
  ↓
Step 4: fact(0) → "Base case! Return 1" [RETURN 1]
  ↑
Step 5: fact(1) ← receives 1 → computes 1 × 1 = 1 [RETURN 1]
  ↑
Step 6: fact(2) ← receives 1 → computes 2 × 1 = 2 [RETURN 2]
  ↑
Step 7: fact(3) ← receives 2 → computes 3 × 2 = 6 [RETURN 6]

Final Answer: 6
```

### 💻 **Python Implementation**
```python
def factorial(n: int) -> int:
    """
    Calculate factorial using recursion
    Time: O(n) | Space: O(n) - call stack
    """
    # Base Case: Stop at 0 or 1
    if n <= 1:
        return 1
    
    # Recursive Step: n × factorial(n-1)
    return n * factorial(n - 1)

# Test
print(factorial(5))  # 120
print(factorial(0))  # 1
print(factorial(1))  # 1
```

---

## 🔄 **Head vs Tail Recursion**

### 📊 **Comparison**
| Type | Calculation Timing | Stack Growth | Example |
|------|-------------------|--------------|----------|
| **Head Recursion** | After recursive call | Deep stack | `n * factorial(n-1)` |
| **Tail Recursion** | Before recursive call | Optimizable | `factorial(n-1, acc*n)` |

### 💻 **Head Recursion Example**
```python
def factorial_head(n: int) -> int:
    """Calculation happens AFTER recursive call"""
    if n <= 1:
        return 1
    return n * factorial_head(n - 1)  # Multiply AFTER return
```

### 💻 **Tail Recursion Example**
```python
def factorial_tail(n: int, accumulator: int = 1) -> int:
    """Calculation happens BEFORE recursive call"""
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, accumulator * n)  # Pass result down

# Note: Python doesn't optimize tail recursion automatically
```

---

## 🎯 **Problem 1: Sum of Digits**

### 📝 **Problem Statement**
Write a recursive function that takes a number (e.g., `1234`) and returns the sum of its digits (`1+2+3+4 = 10`).

### 💡 **Key Insights**
- `n % 10` gives the last digit (e.g., `1234 % 10 = 4`)
- `n // 10` removes the last digit (e.g., `1234 // 10 = 123`)
- **Base Case:** When `n` becomes 0

### 🔍 **Execution Trace**
```python
sum_digits(1234)
= 4 + sum_digits(123)
= 4 + (3 + sum_digits(12))
= 4 + (3 + (2 + sum_digits(1)))
= 4 + (3 + (2 + (1 + sum_digits(0))))
= 4 + (3 + (2 + (1 + 0)))
= 4 + (3 + (2 + 1))
= 4 + (3 + 3)
= 4 + 6
= 10
```

### 💻 **Solution**
```python
def sum_of_digits(n: int) -> int:
    """
    Calculate sum of digits recursively
    Time: O(log n) | Space: O(log n)
    """
    # Base Case: No more digits
    if n == 0:
        return 0
    
    # Recursive Step: last digit + sum of remaining
    return (n % 10) + sum_of_digits(n // 10)

# Test
print(sum_of_digits(1234))  # 10
print(sum_of_digits(999))   # 27
print(sum_of_digits(0))     # 0
print(sum_of_digits(5))     # 5
```

---

## 🎯 **Problem 2: Fibonacci Number**

### 📝 **Problem Statement**
The Fibonacci sequence: `0, 1, 1, 2, 3, 5, 8, 13, 21...`

**Formula:** `F(n) = F(n-1) + F(n-2)`

### 💻 **Naive Solution**
```python
def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number (naive approach)
    Time: O(2^n) | Space: O(n)
    ⚠️ Warning: Very slow for n > 35
    """
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive Step
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(5))   # 5
print(fibonacci(10))  # 55
# print(fibonacci(50))  # ⚠️ Will hang!
```

### 🔍 **Execution Tree for fib(5)**
```
                    fib(5)
                   /      \
              fib(4)      fib(3)
             /     \      /    \
        fib(3)   fib(2) fib(2) fib(1)
        /   \    /   \  /   \
    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
    /   \
 fib(1) fib(0)

Notice: fib(3) is calculated TWICE!
This is why it's O(2^n) - exponential!
```

### 🚀 **Optimized Solution with Memoization**
```python
def fibonacci_memo(n: int, memo: dict = None) -> int:
    """
    Calculate nth Fibonacci number with memoization
    Time: O(n) | Space: O(n)
    """
    if memo is None:
        memo = {}
    
    # Check if already calculated
    if n in memo:
        return memo[n]
    
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Calculate and store result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Test
print(fibonacci_memo(50))   # 12586269025 (instant!)
print(fibonacci_memo(100))  # Works fine!
```

---

## 🎯 **Additional Practice Problems**

### 💻 **Problem 3: Power Function**
```python
def power(base: int, exp: int) -> int:
    """
    Calculate base^exp recursively
    Time: O(exp) | Space: O(exp)
    """
    # Base Case
    if exp == 0:
        return 1
    
    # Recursive Step
    return base * power(base, exp - 1)

# Test
print(power(2, 5))   # 32
print(power(3, 3))   # 27
```

### 💻 **Problem 4: Reverse String**
```python
def reverse_string(s: str) -> str:
    """
    Reverse string recursively
    Time: O(n) | Space: O(n)
    """
    # Base Case
    if len(s) <= 1:
        return s
    
    # Recursive Step: last char + reverse of rest
    return s[-1] + reverse_string(s[:-1])

# Test
print(reverse_string("hello"))  # "olleh"
print(reverse_string("a"))      # "a"
```

### 💻 **Problem 5: Count Occurrences**
```python
def count_occurrences(arr: list, target: int) -> int:
    """
    Count occurrences of target in array recursively
    Time: O(n) | Space: O(n)
    """
    # Base Case
    if not arr:
        return 0
    
    # Recursive Step
    count = 1 if arr[0] == target else 0
    return count + count_occurrences(arr[1:], target)

# Test
print(count_occurrences([1, 2, 3, 2, 2], 2))  # 3
print(count_occurrences([1, 1, 1], 1))        # 3
```

---

## 🏆 **LeetCode Problems**

### 🟢 **Easy**
1. **Fibonacci Number (LC-509)** - Classic recursion
2. **Power of Two (LC-231)** - Base case identification
3. **Climbing Stairs (LC-70)** - Fibonacci variant

### 🟡 **Medium**
4. **Generate Parentheses (LC-22)** - Backtracking
5. **Letter Combinations (LC-17)** - Multiple recursion
6. **Subsets (LC-78)** - Decision tree recursion

---

## 🎯 **Key Takeaways**

### ✅ **Core Concepts**
- **Base Case:** The stopping condition (emergency brake)
- **Recursive Relation:** How to break problem into smaller parts
- **Call Stack:** Each call waits for the next to complete
- **Trust the Process:** Leap of faith that recursion works

### 📊 **Complexity Analysis**
```python
complexity_guide = {
    "Linear Recursion": "O(n) time, O(n) space",
    "Binary Recursion": "O(2^n) time, O(n) space",
    "With Memoization": "O(n) time, O(n) space",
    "Tail Recursion": "O(n) time, O(1) space (if optimized)"
}
```

### 💡 **Problem-Solving Template**
```python
def recursive_function(n):
    # Step 1: Define base case(s)
    if base_condition:
        return base_value
    
    # Step 2: Make problem smaller
    smaller_problem = modify(n)
    
    # Step 3: Trust recursion and combine results
    return combine(n, recursive_function(smaller_problem))
```

### ⚠️ **Common Pitfalls**
1. **Missing base case** → Stack overflow
2. **Wrong base case** → Incorrect results
3. **Not making problem smaller** → Infinite recursion
4. **Exponential complexity** → Use memoization

---

*Master recursion, unlock advanced algorithms! 🔄*