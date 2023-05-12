# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Slower solution
# O(n) time, O(n) space - both worst case, where all elements are unique
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            # taking out else speeds up slightly, but why?
            else:
                seen.add(n)
        return False