# 🧵 Strings - The Arrays of Characters

> *"A string is a sequence of characters. But in Python, it's an immutable fortress."*

🎯 **Mission:** Strings appear in **50%+ of interview problems**. They look simple on the surface, but hidden costs (immutability), clever patterns (Sliding Window, Two Pointers), and complex algorithms (KMP) make them deceptively tricky. Let's decode them systematically!

---

## 📚 Table of Contents

| Section | Topics Covered |
|---------|----------------|
| **Part A: The Immutable Fortress** | Memory internals, `id()`, Interning, O(N²) trap |
| **Part B: Essential Operations** | Slicing, ASCII/Unicode, String Methods Toolkit |
| **Part C: Two Pointers on Strings** | Palindromes, Reverse, Valid Palindrome II |
| **Part D: Sliding Window on Strings** | Longest Unique Substring, Minimum Window Substring |
| **Part E: Hashing & Anagrams** | Frequency Arrays, Counter, Group Anagrams |
| **Part F: Rolling Hash** | Rabin-Karp Intuition, Polynomial Hashing |
| **Part G: Pattern Matching (KMP)** | LPS Array, KMP Search Algorithm |

---

## 🏰 Part A: The Immutable Fortress

### 💡 What is Immutability?

In Python, a **String cannot be changed** after it's created. It's baked into memory as a read-only object.

```python
s = "Hello"
s[0] = "Y"  # ❌ TypeError: 'str' object does not support item assignment
```

**Why does Python do this?**
- **Safety:** Multiple variables can safely point to the same string without one accidentally modifying it.
- **Hashability:** Because strings never change, they can be used as dictionary keys (`dict[str]`) and added to sets.

---

### 🔍 Memory Visualization — What Happens Under the Hood?

When you do `s = s + " World"`, you are **NOT** patching the existing string. You are:

```
Step 1: "Hello" lives at memory address 0x100
        s  ──────────────────────►  [ H | e | l | l | o ]
                                          addr: 0x100

Step 2: Python creates a brand NEW string "Hello World"
        at memory address 0x200

        [ H | e | l | l | o |   | W | o | r | l | d ]
              addr: 0x200

Step 3: s now points to 0x200. Old "Hello" at 0x100
        is marked for garbage collection.
```

```python
s = "Hello"
print(id(s))   # e.g., 140200000000 (address)
s = s + " World"
print(id(s))   # Different address! A new object was created.
```

---

### 🔬 String Interning (Bonus Knowledge)

Python **caches short, simple strings** to save memory. This is called **string interning**.

```python
a = "hello"
b = "hello"
print(a is b)   # True  → Both point to SAME object in memory!
print(id(a) == id(b))  # True

c = "hello world"
d = "hello world"
print(c is d)   # False → Longer strings may NOT be interned!
```

> 🧠 **Takeaway:** Use `==` to compare **values**, never `is`. The `is` operator checks **identity** (memory address), not equality.

---

### ⚠️ The O(N²) Trap — The Most Common Beginner Mistake

```python
# ❌ BAD: Concatenation in a loop
# Each += creates a BRAND NEW string in memory!
# Total work: 1 + 2 + 3 + ... + N = O(N²)
s = ""
for i in range(1000):
    s += "a"   # Creates a new string every single iteration!

# ✅ GOOD: Collect in a list, join once at the end
# Append is O(1), join is O(N). Total: O(N)
parts = []
for i in range(1000):
    parts.append("a")
s = "".join(parts)  # Creates the final string ONCE
```

**Cost Comparison:**

| Approach | Time Complexity | Why |
|----------|----------------|-----|
| `s += char` in loop | **O(N²)** | Creates N new strings |
| `"".join(list)` | **O(N)** | Single allocation at the end |

> 💡 **Analogy:** Imagine writing a book by rewriting the entire manuscript from scratch every time you add a word (BAD), vs. writing notes on scraps of paper and binding them at the end (GOOD).

---

## 🛠️ Part B: Essential Operations

### 1️⃣ **ASCII & Unicode (`ord` & `chr`)**

Computers only understand numbers. Characters are mapped to integers via a standard called **ASCII** (and its superset, **Unicode**).

```
'A' = 65    'Z' = 90
'a' = 97    'z' = 122
'0' = 48    '9' = 57
```

> ⚠️ **Notice:** Uppercase letters have **smaller** ASCII values than lowercase. `'A' < 'a'` is `True`!

```python
print(ord('a'))           # 97
print(ord('z'))           # 122
print(chr(97))            # 'a'

# Distance trick: Map 'a'→0, 'b'→1, ... 'z'→25
print(ord('c') - ord('a'))  # 2 → 'c' is 2 steps from 'a'
print(ord('z') - ord('a'))  # 25

# Digit trick: Map '0'→0, '1'→1, ... '9'→9
digit_char = '7'
print(ord(digit_char) - ord('0'))  # 7
```

---

### 2️⃣ **Slicing & Reversing**

Python strings are **sequence types**, just like lists. Slicing follows the format `s[start:stop:step]`.

```python
s = "Algorithm"
#    012345678   (positive indices)
#   -987654321   (negative indices)

print(s[0:4])    # "Algo"  → start inclusive, stop exclusive
print(s[5:])     # "ithm"  → from index 5 to end
print(s[:3])     # "Alg"   → from start to index 3
print(s[-3:])    # "hm"    → last 3 characters (wait: actually last 3 of "Algorithm" is "ithm"... let's verify)

# Reverse
print(s[::-1])   # "mhtiroglA"  → Step of -1 means go backwards!

# Every other character
print(s[::2])    # "Agrtm"  → Step of 2
```

**Quick Cheatsheet:**
| Slice | Meaning |
|-------|---------|
| `s[i:j]` | Characters from index `i` to `j-1` |
| `s[:j]` | From start to index `j-1` |
| `s[i:]` | From index `i` to the end |
| `s[::-1]` | Reverse the string |
| `s[i:j:k]` | Every `k`th character from `i` to `j-1` |

---

### 3️⃣ **The String Methods Toolkit**

Python's built-in string methods cover 90% of real interview needs.

```python
s = "  Hello, World!  "

# ── Cleaning ──────────────────────────────────────
print(s.strip())          # "Hello, World!"  → removes leading/trailing whitespace
print(s.lstrip())         # "Hello, World!  "
print(s.rstrip())         # "  Hello, World!"

# ── Case ──────────────────────────────────────────
print(s.strip().lower())  # "hello, world!"
print(s.strip().upper())  # "HELLO, WORLD!"

# ── Checking (Returns True/False) ─────────────────
print("hello".isalpha())    # True  → all letters?
print("123".isdigit())      # True  → all digits?
print("abc123".isalnum())   # True  → all letters or digits?
print("  ".isspace())       # True  → all whitespace?
print("Hello".startswith("He"))  # True
print("Hello".endswith("lo"))    # True

# ── Searching ─────────────────────────────────────
print("hello world".find("world"))     # 6  → index of first match
print("hello world".find("xyz"))       # -1 → not found
print("hello world".count("l"))        # 3

# ── Transforming ──────────────────────────────────
print("hello world".replace("world", "Python"))  # "hello Python"
words = "one,two,three".split(",")               # ["one", "two", "three"]
print(", ".join(["a", "b", "c"]))               # "a, b, c"
```

---

### 4️⃣ **String Formatting (f-strings)**

```python
name = "Alice"
score = 95.678

# f-string (Pythonic, modern)
print(f"Name: {name}, Score: {score:.2f}")  # "Name: Alice, Score: 95.68"

# Padding and alignment
print(f"{'left':<10}|")    # "left      |"  → left align in 10 chars
print(f"{'right':>10}|")   # "     right|"  → right align
print(f"{'center':^10}|")  # "  center  |"  → center align
```

---

## 👉👈 Part C: Two Pointers on Strings

### 🎯 Why Two Pointers for Strings?

Most string problems require comparing characters from different positions. Two Pointers lets us do this **in O(N) time with O(1) space** by keeping two indices that traverse the string.

**Two core patterns:**
1. **Opposite ends** — Start from both ends, move inward (`l →` and `← r`)
2. **Same direction** — One fast, one slow, both moving forward (`slow →` and `fast →`)

---

### 🔥 **Pattern 1: Valid Palindrome — Opposite Ends** ⭐

A palindrome reads the same forwards and backwards: `"racecar"`, `"madam"`.

```python
def is_palindrome_basic(s: str) -> bool:
    """
    Check if a string is a palindrome.

    Visual: "racecar"
    l → r a c e c a r ← r
        ↑               ↑
        Same? Move inward.
    """
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# Test
print(is_palindrome_basic("racecar"))  # True
print(is_palindrome_basic("hello"))    # False
```

**Complexity:** Time O(N), Space O(1)

---

### 🔥 **Pattern 2: Valid Palindrome (Skip Non-Alphanumeric)** ⭐⭐

*LeetCode #125 — Valid Palindrome*

Real-world palindrome check: ignore spaces, punctuation, and case.

```
Input:  "A man, a plan, a canal: Panama"
Output: True
```

```python
def is_valid_palindrome(s: str) -> bool:
    """
    Check palindrome ignoring non-alphanumeric characters.

    Strategy:
    1. Keep two pointers at opposite ends.
    2. Skip non-alphanumeric characters.
    3. Compare remaining characters (case-insensitive).
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# Test
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_valid_palindrome("race a car"))                      # False
print(is_valid_palindrome(" "))                               # True (empty → palindrome)
```

**Complexity:** Time O(N), Space O(1)

---

### 🔥 **Pattern 3: Reverse a String In-Place** ⭐

```python
from typing import List

def reverse_string(s: List[str]) -> None:
    """
    Reverse array of characters in-place.
    LeetCode #344

    Visual: ['h','e','l','l','o']
    Step 1:  h ↔ o → ['o','e','l','l','h']
    Step 2:  e ↔ l → ['o','l','l','e','h']
    Step 3:  center 'l' stays put
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test
chars = ['h', 'e', 'l', 'l', 'o']
reverse_string(chars)
print(chars)  # ['o', 'l', 'l', 'e', 'h']
```

**Complexity:** Time O(N), Space O(1)

---

### 🔥 **Pattern 4: Valid Palindrome II (Delete One Char)** ⭐⭐⭐

*LeetCode #680*

Can the string become a palindrome by removing **at most one** character?

```python
def valid_palindrome_ii(s: str) -> bool:
    """
    Valid Palindrome allowing at most 1 deletion.

    Strategy:
    - Run standard palindrome check.
    - On first mismatch, try SKIPPING either:
      a) the left character, OR
      b) the right character
    - If either remaining substring is a palindrome → True.

    Example: "abca"
    l=0, r=3: 'a' == 'a' ✓
    l=1, r=2: 'b' != 'c' ← Mismatch!
      Try skipping 'b': check "ca" → not palindrome
      Try skipping 'c': check "bc" → not palindrome... wait
      Actually: skip left gives s[2:3]="ca", skip right gives s[1:2]="bc"?

    Let's be precise: mismatch at l, r.
      - Skip left:  check s[l+1 : r+1] as palindrome
      - Skip right: check s[l : r] as palindrome
    """
    def is_palindrome(s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try both: skip left char OR skip right char
            return is_palindrome(s, left + 1, right) or \
                   is_palindrome(s, left, right - 1)
        left += 1
        right -= 1

    return True

# Test
print(valid_palindrome_ii("aba"))    # True
print(valid_palindrome_ii("abca"))   # True (remove 'c' → "aba")
print(valid_palindrome_ii("abc"))    # False
```

**Complexity:** Time O(N), Space O(1)

---

## 🪟 Part D: Sliding Window on Strings

### 🎯 What is Sliding Window on Strings?

Almost like arrays — but strings use **character frequency maps** (dicts or arrays of 26) as the "state" inside the window.

**Template:**
```
left = 0
for right in range(len(s)):
    # Expand: add s[right] to window
    while <window invalid>:
        # Shrink: remove s[left] from window
        left += 1
    # Record answer
```

---

### 🔥 **Pattern 1: Longest Substring Without Repeating Characters** ⭐⭐

*LeetCode #3*

```
Input:  "abcabcbb"
Output: 3  ("abc")
```

```python
def length_of_longest_substring(s: str) -> int:
    """
    Find length of longest substring with all unique characters.

    Visual: "abcabcbb"
    Window: [a]            → len 1
    Window: [a,b]          → len 2
    Window: [a,b,c]        → len 3 ← max so far
    'a' repeats → Shrink:
    Window: [b,c,a]        → len 3
    'b' repeats → Shrink:
    Window: [c,a,b]        → len 3
    'c' repeats → ...

    Strategy: A Set tracks characters in the current window.
    """
    char_set: set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Shrink: remove from left until no duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3
print(length_of_longest_substring(""))          # 0
```

**Complexity:** Time O(N), Space O(min(N, Charset))

---

### 🔥 **Pattern 2: Longest Substring with At Most K Distinct Characters** ⭐⭐

*LeetCode #340*

```
Input:  s = "eceba", k = 2
Output: 3  ("ece")
```

```python
from collections import defaultdict

def longest_k_distinct(s: str, k: int) -> int:
    """
    Longest substring with at most k distinct characters.

    Strategy:
    - Use a HashMap: char → count of occurrences in window.
    - Expand right, add to map.
    - While map has more than k keys, shrink from left.
    """
    char_count: dict = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] += 1  # Expand window

        # Shrink until at most k distinct chars
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Test
print(longest_k_distinct("eceba", 2))   # 3 ("ece")
print(longest_k_distinct("aa", 1))      # 2 ("aa")
```

**Complexity:** Time O(N), Space O(K)

---

### 🔥 **Pattern 3: Minimum Window Substring** ⭐⭐⭐

*LeetCode #76 — Hard Classic*

```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"  (minimum window containing all chars of t)
```

```python
from collections import Counter

def min_window_substring(s: str, t: str) -> str:
    """
    Find minimum window in s that contains all characters of t.

    Strategy:
    - need:     frequency map of t (what we require)
    - window:   frequency map of current window
    - have:     how many characters currently satisfy their required count
    - required: total unique characters we need to satisfy

    Shrink the window as soon as all characters are satisfied.
    Track the smallest valid window seen.

    Visual for s="ADOBECODEBANC", t="ABC":
    ┌─────────── Window ───────────┐
    A D O B E C O D E B A N C
    ↑                           ↑
    left                      right

    - Expand right until all of A, B, C are covered.
    - Once covered, shrink left to find minimum window.
    """
    if not t or not s:
        return ""

    need: dict = Counter(t)
    window: dict = defaultdict(int)

    required = len(need)   # # unique chars in t
    have = 0               # # chars in window satisfying need

    left = 0
    min_len = float("inf")
    result = ""

    for right in range(len(s)):
        char = s[right]
        window[char] += 1

        # Check if this char now satisfies its requirement
        if char in need and window[char] == need[char]:
            have += 1

        # Try shrinking window from left
        while have == required:
            # Update result if this window is smaller
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]

            # Shrink from left
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                have -= 1
            left += 1

    return result

# Test
print(min_window_substring("ADOBECODEBANC", "ABC"))  # "BANC"
print(min_window_substring("a", "a"))                # "a"
print(min_window_substring("a", "aa"))               # ""
```

**Complexity:** Time O(N + M), Space O(N + M) where M = len(t)

---

### 🔥 **Pattern 4: Find All Anagrams in a String** ⭐⭐

*LeetCode #438*

```
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]   (anagrams of "abc" start at index 0 and 6)
```

```python
from typing import List

def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of p's anagrams in s.
    Use a FIXED SIZE sliding window of size len(p).

    Strategy:
    - Maintain frequency count of characters in the current window.
    - Compare with the target frequency of p.
    - Use a 'matches' counter to avoid comparing full arrays each time.
    """
    if len(p) > len(s):
        return []

    p_count = [0] * 26
    window_count = [0] * 26
    result: List[int] = []

    # Initialize p_count and first window
    for i in range(len(p)):
        p_count[ord(p[i]) - ord('a')] += 1
        window_count[ord(s[i]) - ord('a')] += 1

    if window_count == p_count:
        result.append(0)

    # Slide the window
    for right in range(len(p), len(s)):
        # Add new character (right)
        window_count[ord(s[right]) - ord('a')] += 1
        # Remove old character (right - len(p))
        window_count[ord(s[right - len(p)]) - ord('a')] -= 1

        if window_count == p_count:
            result.append(right - len(p) + 1)

    return result

# Test
print(find_anagrams("cbaebabacd", "abc"))  # [0, 6]
print(find_anagrams("abab", "ab"))         # [0, 1, 2]
```

**Complexity:** Time O(N), Space O(1) — fixed array of 26

---

## 🔍 Part E: Hashing & Anagrams

### 🎯 The Core Insight

Strings are sequences of characters. Characters map to integers. Integers can be used as array **indices**. This is the bridge from strings to O(N) hashing!

---

### 🔥 **Technique 1: Sorting — O(N log N)**

```python
def is_anagram_sort(s: str, t: str) -> bool:
    """Check anagram by sorting both strings and comparing."""
    return sorted(s) == sorted(t)
```

Simple, but sorting costs O(N log N).

---

### 🔥 **Technique 2: Frequency Array — O(N)** ⭐

Since there are only **26 lowercase English letters**, we use a fixed-size array instead of a heavy Hash Map.

```python
def is_anagram(s: str, t: str) -> bool:
    """
    Valid Anagram — LeetCode #242

    Key Insight:
    Map each character to index: 'a'→0, 'b'→1, ..., 'z'→25
    hash(char) = ord(char) - ord('a')

    Increment count for chars in s.
    Decrement count for chars in t.
    If all counts are 0 at the end → anagram!
    """
    if len(s) != len(t):
        return False

    count = [0] * 26

    for char in s:
        count[ord(char) - ord('a')] += 1

    for char in t:
        index = ord(char) - ord('a')
        count[index] -= 1
        if count[index] < 0:
            return False  # Early exit: t has more of this char than s

    return True

# Test
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
```

**Complexity:** Time O(N), Space O(1) — array of fixed size 26

---

### 🔥 **Technique 3: Group Anagrams** ⭐⭐

*LeetCode #49*

```
Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]
```

```python
from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group all anagrams together.

    Key: Two strings that are anagrams of each other
         will produce the SAME sorted string (canonical form).

    'eat' → 'aet'
    'tea' → 'aet'  ← same key!
    'tan' → 'ant'
    """
    anagram_map: dict = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))     # Canonical form as key
        anagram_map[key].append(word)

    return list(anagram_map.values())

# Test
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Advanced Version — Use Frequency Tuple as Key (O(N) per word):**

```python
def group_anagrams_optimized(strs: List[str]) -> List[List[str]]:
    """Use char count tuple instead of sorted string for O(N) key generation."""
    anagram_map: dict = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)          # e.g., (1,0,0,1,...) for "ad"
        anagram_map[key].append(word)

    return list(anagram_map.values())
```

**Complexity:** Time O(N × M), Space O(N × M) — N words, M = average length

---

### 🔥 **Technique 4: Ransom Note** ⭐

*LeetCode #383*

Can you build `ransomNote` using letters from `magazine`?

```python
from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Check if ransom_note can be built using characters from magazine.

    Each character from magazine can only be used once.
    """
    mag_count = Counter(magazine)

    for char in ransom_note:
        if mag_count[char] == 0:
            return False
        mag_count[char] -= 1

    return True

# Test
print(can_construct("a", "b"))       # False
print(can_construct("aa", "aab"))    # True
```

**Complexity:** Time O(N + M), Space O(N)

---

## 🌊 Part F: Rolling Hash

### 🎯 The Big Idea

**Problem:** You need to check if a substring matches a pattern many times. Computing a hash from scratch at each position is O(M) per position → O(N × M) total.

**Solution:** A **Rolling Hash** lets you slide the hash from one position to the next in **O(1)** using addition and subtraction, like rolling a window.

---

### 🔍 The Rabin-Karp Intuition

Think of a string as a **polynomial** evaluated at a base `B`:

```
For pattern "abc" with base B = 26:
Hash = ord('a') × B² + ord('b') × B¹ + ord('c') × B⁰
     = 97 × 676  + 98 × 26   + 99 × 1
     = 65572 + 2548 + 99
     = 68219
```

When you **slide** the window from `s[i...i+m-1]` to `s[i+1...i+m]`:

```
New Hash = (Old Hash - ord(s[i]) × B^(m-1)) × B + ord(s[i+m])
```

This subtracts the leftmost character, shifts everything up (×B), and adds the new rightmost character. **All in O(1)!**

---

### 💻 Rabin-Karp Implementation

```python
def rabin_karp_search(text: str, pattern: str) -> list:
    """
    Find all pattern occurrences in text using Rolling Hash.

    Returns list of start indices.

    Time: O(N + M) average, O(N*M) worst case (many hash collisions)
    Space: O(1)
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []

    BASE = 26
    MOD = 10**9 + 7  # Large prime to reduce collisions

    # Compute B^(m-1) % MOD — the highest power
    high_power = pow(BASE, m - 1, MOD)

    # Compute initial hash for pattern and first window of text
    pattern_hash = 0
    window_hash = 0

    for i in range(m):
        pattern_hash = (pattern_hash * BASE + ord(pattern[i])) % MOD
        window_hash  = (window_hash  * BASE + ord(text[i]))    % MOD

    result = []

    for i in range(n - m + 1):
        # Hash match → verify character by character (avoid false positives)
        if window_hash == pattern_hash:
            if text[i:i + m] == pattern:  # O(M) verification
                result.append(i)

        # Roll the hash: remove left char, add new right char
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * high_power) % MOD
            window_hash = (window_hash * BASE + ord(text[i + m])) % MOD
            window_hash = (window_hash + MOD) % MOD  # Keep positive

    return result

# Test
print(rabin_karp_search("AABAACAADAABAABA", "AABA"))  # [0, 9, 12]
print(rabin_karp_search("ABABDABACDABABCABAB", "ABAB")) # [0, 10, 14]
```

**Why use MOD?** Hashes can become astronomically large. Modular arithmetic keeps them in bounds. The trade-off: rare **hash collisions** (two different strings with the same hash) → that's why we always verify character-by-character on a hash match.

---

## 🕵️ Part G: Pattern Matching (KMP Algorithm)

### ❓ The Needle in a Haystack Problem

Given text `T` and pattern `P`. Find all positions where `P` occurs in `T`.

**Naive Approach:** Check every position. Reset to start on mismatch.
```
Text:    A B C D A B C A B C D
Pattern: A B C D
         ✓ ✓ ✓ ✗ ← mismatch at D vs A. Start over from text[1]!
           A B C D
           ✓ ...
```
*Complexity: O(N × M)* — Too slow!

---

### 🚀 Knuth-Morris-Pratt (KMP) — O(N + M)

**The Secret Weapon:** When a mismatch happens, we already know some characters from the partial match. Instead of going back to the start of the pattern, we **jump to the best known restart position** using the **LPS array**.

---

### 🧠 The LPS Array (Longest Prefix Suffix)

For pattern `P`, `LPS[i]` stores the **length of the longest proper prefix of P[0...i] that is also a suffix** of P[0...i].

> 💡 **"Proper" prefix/suffix** means it's NOT the full string itself.

**Example by Example:**

```
Pattern: A A B A A B A A B A
Index:   0 1 2 3 4 5 6 7 8 9

LPS[0] = 0  → "A"       — no proper prefix/suffix
LPS[1] = 1  → "AA"      — prefix "A" = suffix "A"  → length 1
LPS[2] = 0  → "AAB"     — no match
LPS[3] = 1  → "AABA"    — prefix "A" = suffix "A"  → length 1
LPS[4] = 2  → "AABAA"   — prefix "AA" = suffix "AA" → length 2
LPS[5] = 3  → "AABAAB"  — prefix "AAB" = suffix "AAB" → length 3
LPS[6] = 4  → "AABAABA" — prefix "AABA" = suffix "AABA" → length 4
...
```

**Simpler Example:**

| Index | Substr | Best Prefix = Suffix | LPS |
|-------|--------|----------------------|-----|
| 0 | A | — | 0 |
| 1 | AA | A | 1 |
| 2 | AAA | AA | 2 |
| 3 | AAAB | — | 0 |
| 4 | AAABA | A | 1 |
| 5 | AAABAA | AA | 2 |
| 6 | AAABAAA | AAA | 3 |

---

### 💻 Step 1: Build the LPS Array

```python
from typing import List

def compute_lps(pattern: str) -> List[int]:
    """
    Build the LPS (Longest Prefix Suffix) array.

    Time: O(M), Space: O(M)

    Two pointers:
    - `length`: length of the current longest prefix-suffix
    - `i`: current position in pattern being processed

    Key insight: When mismatch, don't reset to 0.
    Instead, fall back to lps[length-1] — the previous best.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0   # Length of previous longest prefix-suffix
    i = 1        # We always know lps[0] = 0

    while i < m:
        if pattern[i] == pattern[length]:
            # Characters match → extend the prefix-suffix
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Mismatch after some match: fall back smartly
                # Don't increment i — try the shorter prefix
                length = lps[length - 1]
            else:
                # No prefix to fall back to
                lps[i] = 0
                i += 1

    return lps

# Test
print(compute_lps("AAABAAA"))   # [0, 1, 2, 0, 1, 2, 3]
print(compute_lps("AABAAB"))    # [0, 1, 0, 1, 2, 3]
print(compute_lps("ABCABD"))    # [0, 0, 0, 1, 2, 0]
```

---

### 💻 Step 2: KMP Search

```python
def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text using KMP.
    Returns list of starting indices.

    Time: O(N + M), Space: O(M)

    Two pointers:
    - `i`: index into text
    - `j`: index into pattern

    On match: move both forward.
    On full match: record result, use lps[j-1] to find next start.
    On mismatch:
        - if j > 0: fall back to lps[j-1] (don't backtrack i!)
        - if j == 0: just advance i
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    lps = compute_lps(pattern)
    result: List[int] = []

    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            # Found a complete match!
            result.append(i - j)
            j = lps[j - 1]  # Prepare for next potential match

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]  # Smart fallback — don't backtrack i
            else:
                i += 1          # Nothing to fall back to, advance text

    return result

# Test
text1 = "ABABDABACDABABCABAB"
pat1  = "ABABCABAB"
print(kmp_search(text1, pat1))     # [10]

text2 = "AAAAAA"
pat2  = "AA"
print(kmp_search(text2, pat2))     # [0, 1, 2, 3, 4]

text3 = "AABAACAADAABAABA"
pat3  = "AABA"
print(kmp_search(text3, pat3))     # [0, 9, 12]
```

---

### 📊 KMP Dry Run

```
text:    A B X A B C A B
pattern: A B C A B
lps:     0 0 0 1 2

i=0,j=0: A==A ✓ → i=1,j=1
i=1,j=1: B==B ✓ → i=2,j=2
i=2,j=2: X!=C ✗ → j=lps[1]=0, i stays at 2
i=2,j=0: X!=A ✗ → j=0, i=3
i=3,j=0: A==A ✓ → i=4,j=1
i=4,j=1: B==B ✓ → i=5,j=2
i=5,j=2: C==C ✓ → i=6,j=3
i=6,j=3: A==A ✓ → i=7,j=4
i=7,j=4: B==B ✓ → i=8,j=5 → j==m! MATCH at index 3
```

---

### ⚡ Algorithm Comparison

| Algorithm | Time | Space | Best For |
|-----------|------|-------|----------|
| **Naive** | O(N × M) | O(1) | Very short patterns |
| **Rabin-Karp** | O(N + M) avg | O(1) | Multiple pattern search |
| **KMP** | O(N + M) worst | O(M) | Single pattern, guaranteed linear |

---

## 🧪 Challenge Zone

> 🎯 **Test your String mastery!**

### 🟢 **Problem 1: Valid Palindrome**
Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.

*Input: `"A man, a plan, a canal: Panama"` → `True`*

**💡 Hint:** Use `isalnum()` and Two Pointers from opposite ends.

<details>
<summary>Click for solution</summary>

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
```
</details>

---

### 🟡 **Problem 2: Longest Palindromic Substring**

*Input: `"babad"` → `"bab"` (or `"aba"`)*

**💡 Hint:** Expand from center. For each character (and each gap), treat it as the center of a palindrome and expand outward.

<details>
<summary>Click for solution</summary>

```python
def longest_palindrome(s: str) -> str:
    """
    Expand Around Center approach.

    For each index i:
    - Odd  length: expand around (i, i)
    - Even length: expand around (i, i+1)

    Time: O(N²), Space: O(1)
    """
    res = ""

    def expand(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]  # l and r have gone one step too far

    for i in range(len(s)):
        s1 = expand(i, i)       # Odd-length palindrome
        s2 = expand(i, i + 1)   # Even-length palindrome
        res = max(res, s1, s2, key=len)

    return res

print(longest_palindrome("babad"))   # "bab"
print(longest_palindrome("cbbd"))    # "bb"
print(longest_palindrome("racecar")) # "racecar"
```
</details>

---

### 🟠 **Problem 3: Longest Repeating Character Replacement** ⭐⭐⭐

*LeetCode #424*

You can replace at most `k` characters in a string. Find the longest substring containing the same letter.

*Input: `s = "AABABBA"`, `k = 1` → `4` (replace one 'B' → "AABA" or "ABAA" etc.)*

**💡 Hint:** Use sliding window. The key insight: `window_size - max_count <= k`.

<details>
<summary>Click for solution</summary>

```python
def character_replacement(s: str, k: int) -> int:
    """
    Key Insight:
    In any valid window, the number of characters we need to REPLACE
    = (window size) - (count of the most frequent character)
    This must be <= k.

    We don't shrink when max_count decreases — we just don't expand
    our answer. This is an optimization: we only ever grow our answer.
    """
    count = [0] * 26
    max_count = 0  # Count of the most frequent character in window
    left = 0
    max_length = 0

    for right in range(len(s)):
        count[ord(s[right]) - ord('a')] += 1
        max_count = max(max_count, count[ord(s[right]) - ord('a')])

        # Check if current window is valid
        window_size = right - left + 1
        if window_size - max_count > k:
            # Shrink: remove left character
            count[ord(s[left]) - ord('a')] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

print(character_replacement("AABABBA", 1))  # 4
print(character_replacement("ABAB", 2))     # 4
```
</details>

---

### 🔴 **Problem 4: String to Integer (atoi)**
Implement `atoi` which converts a string to an integer. Handle whitespace, signs, and overflow.

**💡 Hint:** ASCII logic `digit = ord(char) - ord('0')`.

<details>
<summary>Click for solution</summary>

```python
def my_atoi(s: str) -> int:
    """
    Steps:
    1. Strip leading whitespace.
    2. Handle optional sign.
    3. Parse digits until non-digit or end.
    4. Clamp to 32-bit integer range.
    """
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
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    while index < len(s) and s[index].isdigit():
        digit = ord(s[index]) - ord('0')

        # Check for overflow BEFORE multiplying
        if num > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN

        num = num * 10 + digit
        index += 1

    return num * sign

print(my_atoi("42"))           # 42
print(my_atoi("   -42"))       # -42
print(my_atoi("4193 with words"))  # 4193
print(my_atoi("words and 987"))    # 0
```
</details>

---

### 🔴 **Problem 5: Repeated Substring Pattern** ⭐⭐

*LeetCode #459*

Given a string `s`, check if it can be constructed by taking a substring and repeating it.

*Input: `"abab"` → `True` (repeat "ab" twice)*
*Input: `"aba"` → `False`*

**💡 Hint:** KMP trick — if `s` has a repeated pattern, then `lps[-1] > 0` and `len(s) % (len(s) - lps[-1]) == 0`.

<details>
<summary>Click for solution</summary>

```python
def repeated_substring_pattern(s: str) -> bool:
    """
    KMP trick:
    Build the LPS array for s.
    The minimum period (smallest repeating unit) has length:
        period_len = len(s) - lps[-1]

    If len(s) is divisible by period_len, the string is
    made of repeated copies of that period.

    Example: "abab"
    lps = [0, 0, 1, 2]
    period_len = 4 - 2 = 2  → period is "ab"
    4 % 2 == 0 → True!

    Example: "aba"
    lps = [0, 0, 1]
    period_len = 3 - 1 = 2  → period would be "ab"
    3 % 2 != 0 → False!
    """
    lps = compute_lps(s)
    period_len = len(s) - lps[-1]
    return lps[-1] != 0 and len(s) % period_len == 0

print(repeated_substring_pattern("abab"))   # True
print(repeated_substring_pattern("aba"))    # False
print(repeated_substring_pattern("abcabc")) # True
print(repeated_substring_pattern("abcabcabcabc"))  # True
```
</details>

---

## 🎓 Key Takeaways

| Concept | Takeaway |
|---------|---------|
| **Immutability** | `+=` in loops is O(N²). Always use `"".join(list)` → O(N). |
| **ASCII** | `ord('b') - ord('a') = 1` maps characters to indices 0–25. |
| **Two Pointers** | Use opposite-ends for palindromes, same-direction for filters. |
| **Sliding Window** | Grow right, shrink left. Use a `dict` or `list[26]` to track frequency. |
| **Anagrams** | Frequency Array of size 26 → O(N). Sorted canonical form → O(N log N). |
| **Rolling Hash** | Slide hash in O(1). Always verify on hash collision. |
| **KMP** | Build LPS array first — it's the key to O(N+M) pattern matching. |

---

## 🗺️ Problem Map

| Problem | Pattern | Difficulty | LeetCode |
|---------|---------|------------|---------|
| Valid Palindrome | Two Pointers | 🟢 Easy | #125 |
| Valid Palindrome II | Two Pointers | 🟡 Medium | #680 |
| Reverse String | Two Pointers | 🟢 Easy | #344 |
| Longest Substring No Repeat | Sliding Window | 🟡 Medium | #3 |
| Find All Anagrams | Sliding Window | 🟡 Medium | #438 |
| Minimum Window Substring | Sliding Window | 🔴 Hard | #76 |
| Valid Anagram | Hashing | 🟢 Easy | #242 |
| Group Anagrams | Hashing | 🟡 Medium | #49 |
| Ransom Note | Hashing | 🟢 Easy | #383 |
| Longest Palindromic Substring | Expand Center | 🟡 Medium | #5 |
| Char Replacement | Sliding Window | 🟡 Medium | #424 |
| String to Integer | Simulation | 🟡 Medium | #8 |
| Repeated Substring | KMP | 🟡 Medium | #459 |

---

## 🚀 Next Steps

- **Linked Lists** → Explore another sequential structure where immutability isn't the concern.
- **Recursion** → Strings + Recursion = Permutations, Subsets, and Backtracking problems.
- **Dynamic Programming** → Longest Common Subsequence, Edit Distance — the advanced string chapter!

---

*Happy Coding! 🎉*