# 🧵 Strings - The Arrays of Characters

> *"A string is a sequence of characters. But in Python, it's an immutable fortress."*

🎯 **Mission:** Strings appear in 50% of interview problems. They look simple, but hidden costs (immutability) and complex algorithms (KMP) make them tricky. Let's decode them!

---

## 📚 Table of Contents

| Section | Topics Covered |
|---------|----------------|
| **Part A: The Immutable Fortress** | Memory internals, `id()`, Interning, O(N²) trap |
| **Part B: Essential Operations** | Slicing, ASCII/Unicode, The "StringBuilder" Pattern |
| **Part C: Hashing & Anagrams** | Frequency Arrays, Rolling Hash Intuition |
| **Part D: Pattern Matching** | Naive Search vs. KMP Algorithm (LPS Array) |

---

## 🏰 Part A: The Immutable Fortress

### 💡 What is Immutability?

In Python, a **String cannot be changed** after it's created.

```python
s = "Hello"
s[0] = "Y"  # ❌ TypeError: 'str' object does not support item assignment
```

**Memory Visualization:**
When you do `s = s + " World"`, you aren't modifying `s`. You are:
1. Creating a **NEW** string "Hello World" in memory.
2. Pointing `s` to the new string.
3. Garbage collecting the old "Hello".

### ⚠️ The O(N²) Trap

```python
# ❌ BAD: Concatenation in a loop
s = ""
for i in range(1000):
    s += "a"  # Creates a NEW string every single time!
    # Cost: 1 + 2 + 3 + ... + N = O(N²)

# ✅ GOOD: List Join (StringBuilder Pattern)
parts = []
for i in range(1000):
    parts.append("a")
s = "".join(parts)  # Creates string ONCE at the end
# Cost: O(N)
```

---

## 🛠️ Part B: Essential Operations

### 1️⃣ **ASCII & Unicode (`ord` & `chr`)**

Computers only understand numbers. Characters are mapped to integers.

- `'a'` = 97, `'b'` = 98 ...
- `'A'` = 65 ... (Notice: Uppercase < Lowercase)

```python
print(ord('a'))      # 97
print(ord('z'))      # 122
print(chr(97))       # 'a'

# Distance between chars
print(ord('c') - ord('a'))  # 2 (c is 2 steps from a)
```

### 2️⃣ **Slicing & Reversing**

Python strings are sequence types, just like lists.

```python
s = "Algorithm"

print(s[0:4])   # "Algo" (Start inclusive, End exclusive)
print(s[5:])    # "ithm" (To the end)
print(s[::-1])  # "mhtiroglA" (Reverse string!) 🚀
```

---

## 🔍 Part C: Hashing & Anagrams

### 🎯 The Anagram Problem
Two strings are **anagrams** if they contain the same characters with same frequencies.
*Ex: "listen" ↔️ "silent"*

#### **Technique 1: Sorting (O(N log N))**
```python
def is_anagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

#### **Technique 2: Frequency Array (O(N))** ⭐
Since there are only 26 lowercase English letters, we can use a fixed-size array instead of a heavy Hash Map.

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    # Frequency array for 26 chars
    count = [0] * 26
    
    for char in s:
        # Map 'a'→0, 'b'→1, ...
        index = ord(char) - ord('a')
        count[index] += 1
        
    for char in t:
        index = ord(char) - ord('a')
        count[index] -= 1
        if count[index] < 0:
            return False
            
    return True
```

**Why is this "Hashing"?**
We are hashing the key (character) to an integer index (0-25).
`hash(char) = ord(char) - ord('a')`

---

## 🕵️ Part D: Pattern Matching (KMP Algorithm)

### ❓ The Needle in a Haystack
Given text `T` and pattern `P`. Does `P` exist in `T`?

**Naive Approach:** Check every position.
*Complexity: O(N × M)* (Slow!)

### 🚀 Knuth-Morris-Pratt (KMP) Algorithm
*Complexity: O(N + M)* (Fast!)

**The Secret:** DO NOT go back to start. Use previous knowledge.

#### 🧠 The LPS Array (Longest Prefix Suffix)
For pattern `P`, `LPS[i]` stores the length of the longest proper prefix of `P[0...i]` that is also a suffix of `P[0...i]`.

**Example:** `P = "AAABAAA"`

| Index | Substr | Prefix / Suffix Match | LPS |
|-------|--------|-----------------------|-----|
| 0 | A | - | 0 |
| 1 | AA | A | 1 |
| 2 | AAA | AA | 2 |
| 3 | AAAB | - | 0 |
| 4 | AAABA | A | 1 |
| 5 | AAABAA | AA | 2 |
| 6 | AAABAAA | AAA | 3 |

#### 💻 KMP Implementation

```python
from typing import List

def compute_LPS(pattern: str) -> List[int]:
    """
    Computes Longest Prefix Suffix array.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Tricky part: don't increment i here
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMPSearch(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text using KMP.
    Returns list of starting indices.
    """
    n, m = len(text), len(pattern)
    if m == 0: return []
    
    lps = compute_LPS(pattern)
    result = []
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            result.append(i - j)  # Found a match
            j = lps[j - 1]        # Prepare for next match
        
        elif i < n and pattern[j] != text[i]:
            # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]    # Jump back using LPS
            else:
                i += 1
    
    return result

# Test
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(f"Found at: {KMPSearch(txt, pat)}")
```

---

## 🧪 Challenge Zone

> 🎯 **Test your String mastery!**

### 🟢 **Problem 1: Valid Palindrome**
Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.
*Input: "A man, a plan, a canal: Panama" → True*

**💡 Hint:** Use `isalnum()` and Two Pointers.

<details>
<summary>Click for solution</summary>

```python
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
            
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
        
    return True
```
</details>

---

### 🟡 **Problem 2: Longest Palindromic Substring**
*Input: "babad" → "bab" (or "aba")*

**💡 Hint:** Expand from center. For each character, treat it as the center of a palindrome.

<details>
<summary>Click for solution</summary>

```python
def longest_palindrome(s: str) -> str:
    res = ""
    
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        
    for i in range(len(s)):
        # Odd length (center is i)
        s1 = expand(i, i)
        # Even length (center is i, i+1)
        s2 = expand(i, i+1)
        
        res = max(res, s1, s2, key=len)
        
    return res
```
</details>

---

### 🔴 **Problem 3: String to Integer (atoi)**
Implement `atoi` which converts a string to an integer. Handle whitespace, signs, and overflow.

**💡 Hint:** ASCII logic `current_digit = ord(char) - ord('0')`.

<details>
<summary>Click for solution</summary>

```python
def my_atoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
        
    sign = 1
    index = 0
    
    if s[0] == '-':
        sign = -1
        index += 1
    elif s[0] == '+':
        index += 1
        
    num = 0
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])
        
        # Check overflow (conceptually)
        if num > (2**31 - 1 - digit) // 10:
            return 2**31 - 1 if sign == 1 else -2**31
            
        num = num * 10 + digit
        index += 1
        
    return num * sign
```
</details>

---

## 🎓 Key Takeaways

✅ **Immutability:** String concatenation in loops is O(N²). Use `"".join()` list.  
✅ **ASCII:** `ord('b') - ord('a') = 1` is useful for mapping chars to array indices.  
✅ **Anagrams:** Solve using Frequency Arrays (Size 26) for O(N).  
✅ **KMP:** Solves pattern matching in O(N+M) using the LPS array to skip redundant comparisons.  

---

## 🚀 Next Steps
- **Linked Lists** (Where immutability isn't a problem!)
- **Recursion** (Often used with string permutations)

*Happy Coding! 🎉*