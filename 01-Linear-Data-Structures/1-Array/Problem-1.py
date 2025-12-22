"""
🔄 Problem 1 (Easy): Reverse Array In-Place

📝 Task: Write a function that reverses a list in-place (without creating a new list)
📥 Input:  [1, 2, 3, 4, 5]
📤 Output: [5, 4, 3, 2, 1]

💡 Approach: Two Pointer Technique
   - Place one pointer at start (left), one at end (right)
   - Swap elements and move pointers toward center
   - Continue until pointers meet

⏰ Time Complexity:  O(N) - visit each element once
💾 Space Complexity: O(1) - only use two pointers
"""

from typing import List


def reverse_array_inplace(arr: List[int]) -> List[int]:
    """
    Reverse an array in-place using two pointers.
    
    Args:
        arr: List of integers to reverse
        
    Returns:
        The same list, reversed in-place
        
    Example:
        >>> reverse_array_inplace([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
    """
    left = 0
    right = len(arr) - 1
    
    # 🔄 Two pointers moving toward center
    while left < right:
        # 🔀 Swap elements at left and right positions
        arr[left], arr[right] = arr[right], arr[left]
        
        # 👈👉 Move pointers closer
        left += 1
        right -= 1
    
    return arr


# 🧪 Test Cases
if __name__ == "__main__":
    # Test case 1: Normal array
    test1 = [1, 2, 3, 4, 5]
    print(f"Original: {test1}")
    result1 = reverse_array_inplace(test1.copy())
    print(f"Reversed: {result1}")
    print()
    
    # Test case 2: Even length array
    test2 = [1, 2, 3, 4]
    print(f"Original: {test2}")
    result2 = reverse_array_inplace(test2.copy())
    print(f"Reversed: {result2}")
    print()
    
    # Test case 3: Single element
    test3 = [42]
    print(f"Original: {test3}")
    result3 = reverse_array_inplace(test3.copy())
    print(f"Reversed: {result3}")
    print()
    
    # Test case 4: Empty array
    test4 = []
    print(f"Original: {test4}")
    result4 = reverse_array_inplace(test4.copy())
    print(f"Reversed: {result4}")