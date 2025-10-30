# File: two_sum.py
# Author: Kanishkar R
# Date: 2025-10-28
# Description: Python program to find two indices such that their values add up to the given target.

"""
Time Complexity: O(n²)
→ Two nested loops, each potentially iterating through the entire list.

Space Complexity: O(1)
→ No extra space used other than variables.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Loop through each element
        for i in range(len(nums)):
            # Check with all subsequent elements
            for j in range(i + 1, len(nums)):
                # If sum matches the target, return indices
                if nums[i] + nums[j] == target:
                    return [i, j]

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Indices:", result)  # Output: [0, 1]
