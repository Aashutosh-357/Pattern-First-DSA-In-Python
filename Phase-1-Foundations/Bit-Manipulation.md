# ⚡ Bit Manipulation - The Speed Demon

> *"There are 10 types of people in the world: those who understand binary, and those who don't."* - Classic Programmer Joke

🎯 **Mission:** Master the art of manipulating individual bits to write blazingly fast, memory-efficient code. This is the secret weapon of competitive programmers and system engineers!

---

## 📚 Table of Contents

| Topic | Symbol | Superpower |
|-------|--------|------------|
| **Binary Basics** | `0b1010` | Understanding the language of computers |
| **AND** | `&` | Masking & Checking specific bits |
| **OR** | `\|` | Setting bits |
| **XOR** | `^` | Toggling & Finding unique elements |
| **NOT** | `~` | Inverting bits |
| **Left Shift** | `<<` | Multiplying by powers of 2 |
| **Right Shift** | `>>` | Dividing by powers of 2 |

---

## 🔢 Part A: Binary Basics - The Foundation

### 💡 What is Binary?

Computers think in **binary** (base-2): only `0` and `1`.

**Decimal to Binary Conversion:**
```
Decimal: 13
Binary:  1101

Breakdown:
1×2³ + 1×2² + 0×2¹ + 1×2⁰
= 8  +  4  +  0  +  1
= 13
```

### 🎯 The Light Switch Analogy

```
Bit:    1    0    1    0    1
Switch: 💡   ⚫   💡   ⚫   💡
State:  ON  OFF  ON  OFF  ON
Value:  16   8    4    2    1
```

**Reading right to left:** `10101₂ = 16 + 4 + 1 = 21₁₀`

### 💻 Python Binary Representation

```python
# Different ways to represent binary in Python
num = 13

print(bin(num))           # '0b1101' (binary string)
print(f"{num:04b}")       # '1101' (formatted, 4 bits)
print(f"{num:08b}")       # '00001101' (8 bits)

# Convert binary string to integer
binary_str = "1101"
decimal = int(binary_str, 2)
print(decimal)            # 13
```

---

## 🛠️ Part B: The Essential Operators

### 1️⃣ **AND (`&`) - The Gatekeeper**

**Rule:** Both bits must be `1` to get `1`.

```
Truth Table:
  1 & 1 = 1
  1 & 0 = 0
  0 & 1 = 0
  0 & 0 = 0
```

**Visual Example:**
```
    1101  (13)
  & 1011  (11)
  ------
    1001  (9)
```

#### 🎯 **Use Case 1: Check if Number is Even/Odd**
```python
def is_even(n: int) -> bool:
    """
    Check last bit: if 0 → even, if 1 → odd
    
    Examples:
    4 = 100₂ → last bit is 0 → even
    5 = 101₂ → last bit is 1 → odd
    """
    return (n & 1) == 0

# Test
print(is_even(4))   # True
print(is_even(5))   # False
```

**Complexity:** O(1) - Single operation! ⚡

#### 🎯 **Use Case 2: Extract Specific Bits (Masking)**
```python
def get_bit(n: int, pos: int) -> int:
    """
    Get the bit at position 'pos' (0-indexed from right).
    
    Example: n = 13 (1101₂), pos = 2
    Mask: 1 << 2 = 100₂
    Result: 1101 & 0100 = 0100 → bit is 1
    """
    return (n >> pos) & 1

# Test
num = 13  # 1101₂
print(get_bit(num, 0))  # 1 (rightmost bit)
print(get_bit(num, 1))  # 0
print(get_bit(num, 2))  # 1
print(get_bit(num, 3))  # 1 (leftmost bit)
```

---

### 2️⃣ **OR (`|`) - The Includer**

**Rule:** At least one bit must be `1` to get `1`.

```
Truth Table:
  1 | 1 = 1
  1 | 0 = 1
  0 | 1 = 1
  0 | 0 = 0
```

**Visual Example:**
```
    1100  (12)
  | 1010  (10)
  ------
    1110  (14)
```

#### 🎯 **Use Case: Set a Specific Bit**
```python
def set_bit(n: int, pos: int) -> int:
    """
    Set the bit at position 'pos' to 1.
    
    Example: n = 12 (1100₂), pos = 1
    Mask: 1 << 1 = 0010₂
    Result: 1100 | 0010 = 1110₂ = 14
    """
    return n | (1 << pos)

# Test
num = 12  # 1100₂
result = set_bit(num, 1)
print(f"{num:04b} → {result:04b}")  # 1100 → 1110
print(result)  # 14
```

---

### 3️⃣ **XOR (`^`) - The Interview Superstar** ⭐⭐⭐

**Rule:** Bits must be **different** to get `1`.

```
Truth Table:
  1 ^ 1 = 0  (same → 0)
  1 ^ 0 = 1  (different → 1)
  0 ^ 1 = 1  (different → 1)
  0 ^ 0 = 0  (same → 0)
```

**Visual Example:**
```
    1100  (12)
  ^ 1010  (10)
  ------
    0110  (6)
```

#### 🌟 **XOR Magic Properties**
```python
# Property 1: Self-cancellation
a ^ a = 0

# Property 2: Identity
a ^ 0 = a

# Property 3: Commutative
a ^ b = b ^ a

# Property 4: Associative
(a ^ b) ^ c = a ^ (b ^ c)

# Property 5: Pairs cancel out
a ^ b ^ a = b  # 'a' cancels itself
```

#### 🎯 **Use Case 1: Find the Unique Number** ⭐
```python
from typing import List

def find_unique(nums: List[int]) -> int:
    """
    Find the unique number in an array where every other 
    number appears exactly twice.
    
    Example: [4, 1, 2, 1, 2] → 4
    
    Logic: XOR all numbers - pairs cancel out!
    4 ^ 1 ^ 2 ^ 1 ^ 2
    = 4 ^ (1 ^ 1) ^ (2 ^ 2)
    = 4 ^ 0 ^ 0
    = 4
    """
    result = 0
    for num in nums:
        result ^= num
    return result

# Test
print(find_unique([4, 1, 2, 1, 2]))  # 4
print(find_unique([7, 3, 5, 3, 5]))  # 7
```

**Complexity:** Time O(n), Space O(1) 🚀

#### 🎯 **Use Case 2: Swap Two Numbers Without Temp Variable**
```python
def swap_xor(a: int, b: int) -> tuple:
    """
    Swap two numbers using XOR (no extra space!).
    
    Magic:
    a = a ^ b  → a becomes (original_a ^ original_b)
    b = a ^ b  → b becomes (original_a ^ original_b) ^ original_b = original_a
    a = a ^ b  → a becomes (original_a ^ original_b) ^ original_a = original_b
    """
    print(f"Before: a={a}, b={b}")
    
    a = a ^ b
    b = a ^ b  # b = (a^b) ^ b = a
    a = a ^ b  # a = (a^b) ^ a = b
    
    print(f"After: a={a}, b={b}")
    return a, b

# Test
swap_xor(5, 10)
```

#### 🎯 **Use Case 3: Toggle a Specific Bit**
```python
def toggle_bit(n: int, pos: int) -> int:
    """
    Toggle (flip) the bit at position 'pos'.
    
    Example: n = 12 (1100₂), pos = 1
    Mask: 1 << 1 = 0010₂
    Result: 1100 ^ 0010 = 1110₂ = 14
    """
    return n ^ (1 << pos)

# Test
num = 12  # 1100₂
result = toggle_bit(num, 0)
print(f"{num:04b} → {result:04b}")  # 1100 → 1101
```

---

### 4️⃣ **NOT (`~`) - The Inverter**

**Rule:** Flip all bits (`0` → `1`, `1` → `0`).

```python
# Note: Python uses two's complement for negative numbers
num = 5   # 0000 0101
result = ~num
print(result)  # -6

# Why -6? In two's complement:
# ~5 = flip all bits = 1111 1010 = -6
```

#### 🎯 **Use Case: Clear a Specific Bit**
```python
def clear_bit(n: int, pos: int) -> int:
    """
    Clear (set to 0) the bit at position 'pos'.
    
    Example: n = 15 (1111₂), pos = 2
    Mask: ~(1 << 2) = ~0100 = 1011₂
    Result: 1111 & 1011 = 1011₂ = 11
    """
    mask = ~(1 << pos)
    return n & mask

# Test
num = 15  # 1111₂
result = clear_bit(num, 2)
print(f"{num:04b} → {result:04b}")  # 1111 → 1011
print(result)  # 11
```

---

### 5️⃣ **Left Shift (`<<`) - The Multiplier**

**Rule:** Shift bits to the left, fill with `0` on the right.

```
Visual:
5 << 1:
  0101  (5)
→ 1010  (10)  [Multiplied by 2]

5 << 2:
  0101  (5)
→ 10100 (20)  [Multiplied by 4]
```

**Formula:** `n << k = n × 2^k`

```python
def multiply_by_power_of_2(n: int, k: int) -> int:
    """Multiply n by 2^k using left shift."""
    return n << k

# Test
print(5 << 1)   # 10  (5 × 2¹)
print(5 << 2)   # 20  (5 × 2²)
print(5 << 3)   # 40  (5 × 2³)
```

**Complexity:** O(1) - Much faster than `n * (2**k)` ⚡

---

### 6️⃣ **Right Shift (`>>`) - The Divider**

**Rule:** Shift bits to the right, discard rightmost bits.

```
Visual:
20 >> 1:
  10100  (20)
→  1010  (10)  [Divided by 2]

20 >> 2:
  10100  (20)
→   101  (5)   [Divided by 4]
```

**Formula:** `n >> k = n // 2^k` (integer division)

```python
def divide_by_power_of_2(n: int, k: int) -> int:
    """Divide n by 2^k using right shift."""
    return n >> k

# Test
print(20 >> 1)   # 10  (20 ÷ 2¹)
print(20 >> 2)   # 5   (20 ÷ 2²)
print(21 >> 1)   # 10  (21 ÷ 2 = 10.5 → 10)
```

---

## 🎪 Part C: Advanced Patterns & Tricks

### 🔥 **Pattern 1: Check if Power of Two**

```python
def is_power_of_two(n: int) -> bool:
    """
    Power of 2 has only one bit set:
    2 = 0010
    4 = 0100
    8 = 1000
    
    Trick: n & (n-1) removes the rightmost set bit.
    If n is power of 2, result is 0.
    
    Example:
    8 & 7 = 1000 & 0111 = 0000 ✓
    6 & 5 = 0110 & 0101 = 0100 ✗
    """
    return n > 0 and (n & (n - 1)) == 0

# Test
print(is_power_of_two(8))    # True
print(is_power_of_two(16))   # True
print(is_power_of_two(18))   # False
```

**Complexity:** O(1)

---

### 🔥 **Pattern 2: Count Set Bits (Hamming Weight)**

```python
def count_set_bits(n: int) -> int:
    """
    Count the number of 1s in binary representation.
    
    Example: 13 = 1101₂ → 3 set bits
    
    Method 1: Brian Kernighan's Algorithm
    n & (n-1) removes the rightmost set bit each time.
    """
    count = 0
    while n:
        n &= (n - 1)  # Remove rightmost set bit
        count += 1
    return count

# Alternative: Pythonic way
def count_set_bits_pythonic(n: int) -> int:
    return bin(n).count('1')

# Test
print(count_set_bits(13))    # 3 (1101)
print(count_set_bits(7))     # 3 (0111)
print(count_set_bits(8))     # 1 (1000)
```

**Complexity:** O(number of set bits)

---

### 🔥 **Pattern 3: Find Missing Number**

```python
def find_missing(nums: List[int]) -> int:
    """
    Find the missing number in array [0, 1, 2, ..., n].
    
    Example: [0, 1, 3] → missing 2
    
    Logic: XOR all numbers from 0 to n, then XOR with array.
    Pairs cancel out, leaving the missing number!
    
    0 ^ 1 ^ 2 ^ 3 ^ 0 ^ 1 ^ 3
    = (0^0) ^ (1^1) ^ 2 ^ (3^3)
    = 0 ^ 0 ^ 2 ^ 0
    = 2
    """
    n = len(nums)
    xor_all = 0
    
    # XOR all numbers from 0 to n
    for i in range(n + 1):
        xor_all ^= i
    
    # XOR with array elements
    for num in nums:
        xor_all ^= num
    
    return xor_all

# Test
print(find_missing([0, 1, 3]))        # 2
print(find_missing([3, 0, 1]))        # 2
print(find_missing([0, 1, 2, 4, 5]))  # 3
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 4: Find Two Unique Numbers**

```python
def find_two_unique(nums: List[int]) -> List[int]:
    """
    Find two unique numbers in array where every other 
    number appears exactly twice.
    
    Example: [1, 2, 1, 3, 2, 5] → [3, 5]
    
    Logic:
    1. XOR all → gets (a ^ b) where a, b are unique
    2. Find rightmost set bit in (a ^ b)
    3. Divide numbers into two groups based on that bit
    4. XOR each group separately
    """
    # Step 1: XOR all numbers
    xor_all = 0
    for num in nums:
        xor_all ^= num
    
    # Step 2: Find rightmost set bit
    rightmost_bit = xor_all & (-xor_all)
    
    # Step 3 & 4: Divide and conquer
    num1, num2 = 0, 0
    for num in nums:
        if num & rightmost_bit:
            num1 ^= num
        else:
            num2 ^= num
    
    return [num1, num2]

# Test
print(find_two_unique([1, 2, 1, 3, 2, 5]))  # [3, 5]
```

**Complexity:** Time O(n), Space O(1)

---

### 🔥 **Pattern 5: Reverse Bits**

```python
def reverse_bits(n: int, bit_length: int = 32) -> int:
    """
    Reverse the bits of a number.
    
    Example: 13 (1101) with 4 bits → 11 (1011)
    
    Logic: Extract each bit from right, add to result from left.
    """
    result = 0
    for i in range(bit_length):
        # Extract rightmost bit and add to result
        result = (result << 1) | (n & 1)
        # Move to next bit
        n >>= 1
    return result

# Test (using 8 bits for clarity)
num = 13  # 00001101
result = reverse_bits(num, 8)
print(f"{num:08b} → {result:08b}")  # 00001101 → 10110000
print(result)  # 176
```

---

### 🔥 **Pattern 6: Generate All Subsets (Power Set)**

```python
def generate_subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets using bit manipulation.
    
    Example: [1, 2, 3]
    
    Logic: For n elements, there are 2^n subsets.
    Each number from 0 to 2^n-1 represents a subset:
    
    000 → []
    001 → [3]
    010 → [2]
    011 → [2, 3]
    100 → [1]
    101 → [1, 3]
    110 → [1, 2]
    111 → [1, 2, 3]
    """
    n = len(nums)
    total_subsets = 1 << n  # 2^n
    result = []
    
    for i in range(total_subsets):
        subset = []
        for j in range(n):
            # Check if jth bit is set
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)
    
    return result

# Test
print(generate_subsets([1, 2, 3]))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

**Complexity:** Time O(n × 2^n), Space O(2^n)

---

## 🧪 Challenge Zone

> 🎯 **Test your mastery with these problems!**

### 🟢 **Problem 1: Single Bit Operations**
Given `n = 10` (binary: `1010`), perform:
1. Set bit at position 0
2. Clear bit at position 3
3. Toggle bit at position 1

**💡 Hint:** Use OR, AND with NOT, and XOR respectively.

<details>
<summary>Click for solution</summary>

```python
n = 10  # 1010

# 1. Set bit 0: 1010 | 0001 = 1011 (11)
result1 = n | (1 << 0)
print(f"Set bit 0: {result1}")  # 11

# 2. Clear bit 3: 1010 & ~1000 = 0010 (2)
result2 = n & ~(1 << 3)
print(f"Clear bit 3: {result2}")  # 2

# 3. Toggle bit 1: 1010 ^ 0010 = 1000 (8)
result3 = n ^ (1 << 1)
print(f"Toggle bit 1: {result3}")  # 8
```
</details>

---

### 🟡 **Problem 2: Fast Multiplication**
Multiply `17 × 8` using only bit operations (no `*` operator).

**💡 Hint:** 8 = 2³, so use left shift!

<details>
<summary>Click for solution</summary>

```python
def multiply_by_8(n: int) -> int:
    # 8 = 2^3, so left shift by 3
    return n << 3

print(multiply_by_8(17))  # 136
```
</details>

---

### 🟠 **Problem 3: Check if Bits are Alternating**
Check if a number has alternating bits (e.g., `10101` or `01010`).

**💡 Hint:** XOR with right-shifted version should give all 1s.

<details>
<summary>Click for solution</summary>

```python
def has_alternating_bits(n: int) -> bool:
    """
    Example: 5 = 101₂ (alternating) ✓
             10 = 1010₂ (alternating) ✓
             7 = 111₂ (not alternating) ✗
    
    Logic: n ^ (n >> 1) should have all bits set
    Then check if result is power of 2 minus 1
    """
    xor_result = n ^ (n >> 1)
    # Check if all bits are set: (x & (x+1)) == 0
    return (xor_result & (xor_result + 1)) == 0

# Test
print(has_alternating_bits(5))   # True (101)
print(has_alternating_bits(10))  # True (1010)
print(has_alternating_bits(7))   # False (111)
```
</details>

---

### 🔴 **Problem 4: Find XOR of Range**
Calculate XOR of all numbers from `1` to `n` efficiently.

**💡 Hint:** Pattern repeats every 4 numbers!

<details>
<summary>Click for solution</summary>

```python
def xor_from_1_to_n(n: int) -> int:
    """
    Pattern:
    n % 4 == 0 → result = n
    n % 4 == 1 → result = 1
    n % 4 == 2 → result = n + 1
    n % 4 == 3 → result = 0
    
    Example: 1^2^3^4^5^6
    = (1^2^3^4) ^ 5 ^ 6
    = 4 ^ 5 ^ 6
    """
    remainder = n % 4
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n + 1
    else:  # remainder == 3
        return 0

# Test
print(xor_from_1_to_n(6))   # 7
print(xor_from_1_to_n(10))  # 11
```
</details>

---

### 🏆 **Problem 5: Minimum Bit Flips to Convert**
Find minimum bit flips needed to convert number `a` to `b`.

**💡 Hint:** XOR gives different bits, then count them!

<details>
<summary>Click for solution</summary>

```python
def min_bit_flips(a: int, b: int) -> int:
    """
    Example: a = 10 (1010), b = 7 (0111)
    XOR: 1010 ^ 0111 = 1101 (3 different bits)
    """
    # XOR to find different bits
    xor_result = a ^ b
    
    # Count set bits
    count = 0
    while xor_result:
        xor_result &= (xor_result - 1)
        count += 1
    
    return count

# Test
print(min_bit_flips(10, 7))   # 3
print(min_bit_flips(3, 4))    # 3
```
</details>

---

## 📈 Why Bit Manipulation Matters

| Use Case | Benefit | Example |
|----------|---------|---------|
| **Speed** | Fastest CPU operations | Even/odd check, power of 2 |
| **Space** | Compact data storage | Flags, permissions (Unix) |
| **Algorithms** | Elegant solutions | Find unique, missing numbers |
| **Optimization** | Replace expensive operations | Multiply/divide by 2^k |
| **Cryptography** | Core of encryption | XOR ciphers |

---

## 🎓 Key Takeaways

✅ **AND (`&`)** - Check/extract specific bits (masking)  
✅ **OR (`\|`)** - Set specific bits  
✅ **XOR (`^`)** - Toggle bits, find unique elements (cancellation property)  
✅ **NOT (`~`)** - Invert all bits  
✅ **Left Shift (`<<`)** - Fast multiplication by 2^k  
✅ **Right Shift (`>>`)** - Fast division by 2^k  

---

## 🚀 Common Interview Patterns

1. **Single Number** → XOR all elements
2. **Power of Two** → `n & (n-1) == 0`
3. **Count Set Bits** → Brian Kernighan's algorithm
4. **Bit at Position** → `(n >> pos) & 1`
5. **Set/Clear/Toggle Bit** → OR/AND/XOR with mask
6. **Generate Subsets** → Iterate through `2^n` combinations

---

## 🔗 Next Steps

Master these bit manipulation patterns, and you'll be ready for:
- **Advanced DP** (bitmask DP)
- **Graph Algorithms** (visited states)
- **System Design** (efficient flags)

**Remember:** Every bit counts! ⚡

---

*Happy Bit Hacking! 🎉*