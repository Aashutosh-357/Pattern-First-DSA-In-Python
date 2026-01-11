# 📅 Merge Intervals Pattern Mastery

## 🎯 Pattern Overview
**Core Concept:** The King of scheduling problems - merge overlapping time intervals into a clean, consolidated list.

> 💡 **Real-World Applications:** Calendar management, meeting room scheduling, video game collision detection, resource allocation systems.

---

# 👑 Pattern 4: Merge Intervals

## 🎯 **Problem Definition**
Given a list of time intervals (Start, End), merge all overlapping intervals into a simplified list.

**Input:** `[[1, 3], [2, 6], [8, 10], [15, 18]]`
**Output:** `[[1, 6], [8, 10], [15, 18]]`

---

# 📊 Visual Calendar Representation

## 🕐 **Timeline Visualization**
```
Time:    1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
         |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
[1,3]:   [=======]
[2,6]:       [===============]
Merged:  [===================]                    → [1, 6]

[8,10]:                          [=======]        → [8, 10]
[15,18]:                                              [===============] → [15, 18]
```

## 🔍 **Overlap Detection Logic**
```
Meeting A: [1, 3] (1:00 PM - 3:00 PM)
Meeting B: [2, 6] (2:00 PM - 6:00 PM)

Conflict: Meeting B starts at 2:00 PM
         Meeting A hasn't ended yet (ends at 3:00 PM)
         
Resolution: Merge into [1, 6] (1:00 PM - 6:00 PM)
```

---

# 🔧 Algorithm: Sort First, Ask Questions Later

## 📋 **Step-by-Step Process**

### 1️⃣ **Sort by Start Time**
**Why Mandatory:** Without sorting, we can't efficiently detect all overlaps in O(N) time.

### 2️⃣ **Merge Logic**
```python
For each interval:
    if current_start <= last_merged_end:
        # OVERLAP: Merge intervals
        new_end = max(last_merged_end, current_end)
    else:
        # NO OVERLAP: Add as separate interval
        add_to_merged_list(current_interval)
```

---

# 🔍 Detailed Walkthrough

## 📊 **Input Processing**
**Original:** `[[1, 3], [8, 10], [2, 6], [15, 18]]`

### Step 1: Sort by Start Time
**Sorted:** `[[1, 3], [2, 6], [8, 10], [15, 18]]`

### Step 2: Execute Merge Algorithm

| Step | Current | Last Merged | Overlap Check | Action | Merged List |
|------|---------|-------------|---------------|--------|-------------|
| **Init** | [1,3] | - | - | Add first | `[[1,3]]` |
| **1** | [2,6] | [1,3] | 2 ≤ 3? ✅ | Merge: max(3,6)=6 | `[[1,6]]` |
| **2** | [8,10] | [1,6] | 8 ≤ 6? ❌ | Add separate | `[[1,6], [8,10]]` |
| **3** | [15,18] | [8,10] | 15 ≤ 10? ❌ | Add separate | `[[1,6], [8,10], [15,18]]` |

**Final Result:** `[[1, 6], [8, 10], [15, 18]]`

---

# 💻 Implementation

## 🔧 **Core Algorithm**
```python
def merge_intervals(intervals):
    """
    Merge overlapping intervals in O(N log N) time
    
    Args:
        intervals: List of [start, end] pairs
    
    Returns:
        List of merged intervals
    """
    if not intervals:
        return []
    
    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]  # Initialize with first interval
    
    # Step 2: Process remaining intervals
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # Check for overlap
        if current[0] <= last_merged[1]:
            # Overlap detected: merge intervals
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap: add as separate interval
            merged.append(current)
    
    return merged
```

## 🎯 **Alternative Implementation (More Explicit)**
```python
def merge_intervals_explicit(intervals):
    """
    More explicit version showing each step clearly
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda interval: interval[0])
    
    merged = []
    
    for interval in intervals:
        # If merged is empty OR no overlap with last interval
        if not merged or interval[0] > merged[-1][1]:
            # Add current interval as new separate interval
            merged.append(interval)
        else:
            # Overlap detected: extend the end of last interval
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged
```

---

# 🧠 Pattern Drill Solutions

## ✅ **Question 1: Edge Case - Adjacent Intervals**
**Input:** `[[1, 4], [4, 5]]`

### 🔍 **Analysis**
- First interval: [1, 4] (ends at 4)
- Second interval: [4, 5] (starts at 4)
- **Overlap Check:** Does 4 ≤ 4? **YES** ✅

### 📊 **Step-by-Step Solution**
| Step | Current | Last Merged | Check | Action | Result |
|------|---------|-------------|-------|--------|--------|
| Init | [1,4] | - | - | Add first | `[[1,4]]` |
| 1 | [4,5] | [1,4] | 4 ≤ 4? ✅ | Merge: max(4,5)=5 | `[[1,5]]` |

**✅ Answer:** They DO overlap. **Result:** `[[1, 5]]`

---

## ✅ **Question 2: Nested Intervals**
**Input:** `[[1, 4], [2, 3]]`

### 🔍 **Analysis**
- Interval A: [1, 4] (large interval)
- Interval B: [2, 3] (completely inside A)
- **Overlap Check:** Does 2 ≤ 4? **YES** ✅

### 📊 **Step-by-Step Solution**
| Step | Current | Last Merged | Check | Action | Result |
|------|---------|-------------|-------|--------|--------|
| Init | [1,4] | - | - | Add first | `[[1,4]]` |
| 1 | [2,3] | [1,4] | 2 ≤ 4? ✅ | Merge: max(4,3)=4 | `[[1,4]]` |

**✅ Answer:** Final merged interval is `[1, 4]` (unchanged because [2,3] is completely contained)

---

## ✅ **Question 3: Why Sorting is Mandatory**
**Scenario:** Process `[8, 10]` before `[1, 6]` with connecting piece `[5, 9]` coming later.

### 🔍 **Without Sorting (Incorrect)**
```
Step 1: Process [8, 10] → merged = [[8, 10]]
Step 2: Process [1, 6]  → No overlap with [8, 10] → merged = [[8, 10], [1, 6]]
Step 3: Process [5, 9]  → Overlaps with [1, 6] → merged = [[8, 10], [1, 9]]
                        → Still doesn't connect [8, 10] with [1, 9]!
```

### ✅ **With Sorting (Correct)**
```
Sorted: [[1, 6], [5, 9], [8, 10]]
Step 1: [1, 6] → merged = [[1, 6]]
Step 2: [5, 9] → 5 ≤ 6? YES → merged = [[1, 9]]
Step 3: [8, 10] → 8 ≤ 9? YES → merged = [[1, 10]]
```

**✅ Answer:** Sorting ensures we process intervals in chronological order, allowing us to detect ALL overlaps in a single pass. Without sorting, we might miss connections between non-adjacent intervals.

---

# 🎯 Advanced Variations

## 🔧 **Variation 1: Insert Interval**
```python
def insert_interval(intervals, new_interval):
    """
    Insert a new interval and merge if necessary
    Time: O(N), Space: O(N)
    """
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals that end before new interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result
```

## 🔧 **Variation 2: Meeting Rooms**
```python
def can_attend_all_meetings(intervals):
    """
    Check if a person can attend all meetings (no overlaps)
    Time: O(N log N), Space: O(1)
    """
    if not intervals:
        return True
    
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        # If current meeting starts before previous ends
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True

def min_meeting_rooms(intervals):
    """
    Find minimum number of meeting rooms needed
    Time: O(N log N), Space: O(N)
    """
    if not intervals:
        return 0
    
    import heapq
    
    intervals.sort(key=lambda x: x[0])
    heap = []  # Min heap to track end times
    
    for interval in intervals:
        # If room is available (earliest end time <= current start)
        if heap and heap[0] <= interval[0]:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, interval[1])
    
    return len(heap)
```

---

# 📊 Complexity Analysis

## ⏱️ **Time Complexity**
| Operation | Complexity | Explanation |
|-----------|------------|-------------|
| **Sorting** | O(N log N) | Dominant factor |
| **Merging** | O(N) | Single pass through sorted list |
| **Overall** | O(N log N) | Sorting dominates |

## 💾 **Space Complexity**
| Approach | Space | Explanation |
|----------|-------|-------------|
| **In-place sorting** | O(1) | Modify input array |
| **New result array** | O(N) | Store merged intervals |
| **Worst case** | O(N) | All intervals separate |

---

# 🎯 Common Problem Patterns

## 📋 **Problem Categories**

### 🕐 **Scheduling Problems**
| Problem | Description | Key Insight |
|---------|-------------|-------------|
| **Merge Intervals** | Combine overlapping time slots | Sort + merge overlaps |
| **Meeting Rooms I** | Can attend all meetings? | Check for any overlap |
| **Meeting Rooms II** | Min rooms needed | Count max concurrent meetings |
| **Insert Interval** | Add new interval to sorted list | Find position + merge |

### 🎮 **Collision Detection**
| Problem | Description | Key Insight |
|---------|-------------|-------------|
| **Range Overlap** | Do two ranges intersect? | Check start ≤ other_end |
| **Point in Intervals** | Which intervals contain point? | Binary search on sorted starts |
| **Interval Intersection** | Find common parts of intervals | Merge logic with intersection |

---

# 🚀 Optimization Techniques

## 🔧 **Performance Tips**
```python
# Tip 1: Early termination for sorted intervals
def merge_intervals_optimized(intervals):
    if len(intervals) <= 1:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:
            # Merge: only update end if current extends further
            if current[1] > last[1]:
                last[1] = current[1]
        else:
            merged.append(current)
    
    return merged

# Tip 2: Use tuple unpacking for readability
def merge_intervals_readable(intervals):
    if not intervals:
        return []
    
    intervals.sort()
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end:
            merged[-1] = [last_start, max(last_end, end)]
        else:
            merged.append([start, end])
    
    return merged
```

---

# 🎯 Key Takeaways

## ✅ **Pattern Recognition**
- **Overlapping intervals** → Merge intervals pattern
- **Scheduling conflicts** → Check for overlaps
- **Resource allocation** → Count concurrent intervals
- **Time-based problems** → Sort by start time first

## 🚀 **Implementation Checklist**
- [ ] **Sort intervals** by start time
- [ ] **Handle edge cases** (empty input, single interval)
- [ ] **Check overlap condition** (start ≤ last_end)
- [ ] **Merge correctly** (max of end times)
- [ ] **Consider space complexity** (in-place vs new array)

## 💼 **Real-World Applications**
- **Calendar Systems:** Google Calendar, Outlook scheduling
- **Resource Management:** Meeting room booking, equipment allocation
- **Game Development:** Collision detection, event scheduling
- **System Design:** Load balancing, time-slot management

---

*Schedule efficiently, merge intelligently! 📅*