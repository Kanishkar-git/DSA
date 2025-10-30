# File: valid_anagram.py
# Author: Kanishkar R
# Date: 2025-10-28
# Description: Python program to check if two strings are anagrams of each other.

"""
Time Complexity: O(n log n)
→ Sorting both strings takes O(n log n) time.

Space Complexity: O(1)
→ Sorting is done in place; only a few variables are used.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Sort both strings and compare
        return ''.join(sorted(s)) == ''.join(sorted(t))


# Example usage
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    result = solution.isAnagram(s, t)
    print("Is Anagram:", result)  # Output: True
