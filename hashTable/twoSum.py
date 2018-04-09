# Use hash table to store value, index pair -> dictionary d
# For each number, if complement exist, return indices. Otherwise, add number to dictionary.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)
        d = {}
        for i,x in enumerate(nums):
            if target-x in d.keys():
                return [d[target-x],i]
            else:
                d[x] = i
