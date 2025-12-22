"""
🔢 Problem 2 (Medium): Move Zeros to End

📝 Task: Move all 0s to the end while maintaining relative order of non-zero elements
📥 Input:  [0, 1, 0, 3, 12]
📤 Output: [1, 3, 12, 0, 0]

💡 Approach: Two Pointer Technique (Focus on Non-Zeros)
   - Use a "write" pointer to track where next non-zero should go
   - Iterate through array with "read" pointer
   - When we find non-zero, swap it to the "write" position
   - This naturally pushes zeros to the end

⏰ Time Complexity:  O(N) - single pass through array
💾 Space Complexity: O(1) - only use two pointers
"""

from typing import List


def move_zeros_to_end(arr: List[int]) -> List[int]:
    """
    Move all zeros to the end while maintaining order of non-zeros.
    
    Args:
        arr: List of integers containing zeros and non-zeros
        
    Returns:
        The same list with zeros moved to end
        
    Example:
        >>> move_zeros_to_end([0, 1, 0, 3, 12])
        [1, 3, 12, 0, 0]
    """
    write_pos = 0  # 📝 Position where next non-zero should go
    
    # 🔍 Scan through entire array
    for read_pos in range(len(arr)):
        # 🔢 Found a non-zero element?
        if arr[read_pos] != 0:
            # 🔀 Swap it to the write position
            arr[write_pos], arr[read_pos] = arr[read_pos], arr[write_pos]
            # ➡️ Move write pointer forward
            write_pos += 1
    
    return arr


# 🧪 Test Cases
if __name__ == "__main__":
    # Test case 1: Mixed zeros and non-zeros
    test1 = [0, 1, 0, 3, 12]
    print(f"Original: {test1}")
    result1 = move_zeros_to_end(test1.copy())
    print(f"After moving zeros: {result1}")
    print()
    
    # Test case 2: All zeros
    test2 = [0, 0, 0, 0]
    print(f"Original: {test2}")
    result2 = move_zeros_to_end(test2.copy())
    print(f"After moving zeros: {result2}")
    print()
    
    # Test case 3: No zeros
    test3 = [1, 2, 3, 4, 5]
    print(f"Original: {test3}")
    result3 = move_zeros_to_end(test3.copy())
    print(f"After moving zeros: {result3}")
    print()
    
    # Test case 4: Zeros at beginning
    test4 = [0, 0, 1, 2, 3]
    print(f"Original: {test4}")
    result4 = move_zeros_to_end(test4.copy())
    print(f"After moving zeros: {result4}")
    print()
    
    # Test case 5: Single element
    test5 = [0]
    print(f"Original: {test5}")
    result5 = move_zeros_to_end(test5.copy())
    print(f"After moving zeros: {result5}")