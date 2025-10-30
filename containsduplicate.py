# File: contains_duplicate.py
# Author: Kanishkar R
# Date: 2025-10-28
# Description: Python program to check if a list contains any duplicate elements.

"""
Time Complexity: O(n log n)
→ Because of sorting the array before checking duplicates.

Space Complexity: O(1)
→ Sorting is done in place, and only a few variables are used.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Sort the list first
        nums.sort()

        # Compare each element with its previous one
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True  # Duplicate found

        return False  # No duplicates found


# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print("Contains duplicate:", result)  # Output: True
