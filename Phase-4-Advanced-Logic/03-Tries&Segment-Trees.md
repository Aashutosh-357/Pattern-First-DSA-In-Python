# Tries (Prefix Trees) & Segment Trees: Advanced Data Structures

## Part 1: Tries (Prefix Trees)

### 🌿 The Concept (Why?)
Imagine you are building the search bar for an online massive bookstore. When a user types "bat", you want to instantly suggest "batman", "battle", and "batter".

If you store all 1 million dictionary words in a standard List, finding words that *start with* "bat" means checking every single word. That's painfully slow.

A **Trie** (pronounced "try", from re**trie**val) is specialized for this exact problem. It's like a magical filing cabinet where words are stored letter by letter. To find "bat", you open the drawer 'b', then folder 'a', then file 't', and you immediately see everything inside.

**Real-world Analogy:** The ultimate auto-complete engine.

### 👁️ Visual Logic First
Let's see what a Trie looks like when we insert the words: `"cat"`, `"car"`, `"bat"`.

```text
       (Root)
      /      \
    'c'      'b'
     |        |
    'a'      'a'
   /   \      |
 't'*  'r'*  't'*  (* marks end of a word)
```

Each node represents a single character. Words that share the same prefix (like "cat" and "car") share the same path down the tree (`c -> a`), saving massive amounts of space and making searches incredibly fast.

### 🏗️ Pythonic Implementation

```python
class TrieNode:
    def __init__(self):
        # A dictionary mapping characters to child TrieNodes
        self.children: dict[str, 'TrieNode'] = {}
        # Boolean to check if a word ends at this node
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
```

### 📈 Complexity Analysis (Big O)
*   **Time Complexity:** $O(L)$ for Insert, Search, and StartsWith, where `L` is the length of the word. It's incredibly fast because we only do as many operations as there are letters in the target word, regardless of how many millions of words are in the Trie!
*   **Space Complexity:** $O(N \cdot L)$, where `N` is the number of words and `L` is their average length. In the worst case, every word has unique characters. However, with many shared prefixes, the actual space used is much less.

---

## Part 2: Segment Trees

### 📊 The Concept (Why?)
Imagine you are managing an online game's leaderboard with millions of players. You constantly need to know two things:
1.  "What is the total score of players ranked between 10,000 and 20,000?" (Range Query)
2.  "Player 15,432 just scored 50 points, update their score." (Point Update)

*   **Naive Approach 1 (List):** `sum(array[10000:20000])`. Range sum takes $O(N)$ time. Too slow for frequent queries! Update is $O(1)$.
*   **Naive Approach 2 (Prefix Sum Array):** Range sum takes $O(1)$ time. But if you update a single player's score, you must recalculate all prefix sums after them. Update is $O(N)$ time. Too slow for frequent updates!

A **Segment Tree** strikes the perfect balance. It gives you both Range Queries and Updates in blazingly fast $O(\log N)$ time.

**Real-world Analogy:** A corporate hierarchy. The bottom-level employees are individual array elements. The managers above them store the sum, min, or max of their direct reports. The CEO at the very top summarizes the entire company. If one employee's performance changes, only their direct chain of command needs to update.

### 👁️ Visual Logic First
Let's build a Segment Tree for the array `nums = [1, 3, 5, 7]`, specifically to answer **Range Sum Queries**.

```text
Level 1 (The Array):
Indices:      [0]   [1]   [2]   [3]
Elements:      1     3     5     7

Level 2 (Managers - Pair sums):
            (1+3=4)      (5+7=12)
            /     \      /      \
           1       3    5        7

Level 3 (CEO - Total sum):
                  (4+12=16)
                 /         \
               (4)        (12)
              /   \      /    \
             1     3    5      7
```
If we want the sum of indices `0` to `1`, we just ask the manager on the left whose value is `4`. No need to add `1 + 3` again!

### 🏗️ Pythonic Implementation
We usually build segment trees using arrays (similar to heaps). For an array of size $N$, the segment tree takes up to $4N$ space.

```python
from typing import List

class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        # Tree array size 4 * N is safe to hold the full segment tree
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(data, node=0, start=0, end=self.n - 1)

    def _build(self, data: List[int], node: int, start: int, end: int) -> None:
        if start == end:
            # Leaf node: holds the array element
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            # Recursively build left and right subtrees
            self._build(data, left_child, start, mid)
            self._build(data, right_child, mid + 1, end)
            
            # Internal node: holds the sum of both children
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index: int, value: int) -> None:
        """Updates the value at array[index] to `val`."""
        self._update_recursive(0, 0, self.n - 1, index, value)

    def _update_recursive(self, node: int, start: int, end: int, index: int, value: int) -> None:
        if start == end:
            # Found the exact leaf node to update
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            if start <= index <= mid:
                # Target index is in the left subtree
                self._update_recursive(left_child, start, mid, index, value)
            else:
                # Target index is in the right subtree
                self._update_recursive(right_child, mid + 1, end, index, value)
                
            # Recalculate the sum for the current node after update
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, left: int, right: int) -> int:
        """Returns the sum of elements in the range [left, right] inclusive."""
        return self._query_recursive(0, 0, self.n - 1, left, right)

    def _query_recursive(self, node: int, start: int, end: int, l: int, r: int) -> int:
        # 1. Total Overlap: This segment is completely inside our query range
        if l <= start and end <= r:
            return self.tree[node]
            
        # 2. No Overlap: This segment is completely outside our query range
        if end < l or start > r:
            return 0
            
        # 3. Partial Overlap: Break it down and ask the children
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_sum = self._query_recursive(left_child, start, mid, l, r)
        right_sum = self._query_recursive(right_child, mid + 1, end, l, r)
        
        return left_sum + right_sum
```

### 📈 Complexity Analysis (Big O)
*   **Time Complexity:** 
    *   **Build:** $O(N)$
    *   **Update:** $O(\log N)$
    *   **Query:** $O(\log N)$
*   **Space Complexity:** $O(N)$, specifically bounded by $4N$ to represent the full binary tree structure.

---

## 🎯 Challenge Zone
Ready to test your knowledge? Try these classic problems:

1.  **[LeetCode 208] Implement Trie (Prefix Tree)** (Medium) - The exact code above!
2.  **[LeetCode 211] Design Add and Search Words Data Structure** (Medium) - Modify search to handle `.` as a wildcard.
3.  **[LeetCode 307] Range Sum Query - Mutable** (Medium) - The exact Segment Tree implementation above!
4.  **[LeetCode 212] Word Search II** (Hard) - Combining a Trie with Backtracking on a grid. A very common interview question.

---

## 💡 Key Takeaways
*   Use a **Trie** whenever you hear "prefix", "autocomplete", or "dictionary matching". It's the ultimate string look-up accelerator.
*   Use a **Segment Tree** whenever you need to perform *both* frequent updates and frequent range queries (sums, min, max) over an array.
