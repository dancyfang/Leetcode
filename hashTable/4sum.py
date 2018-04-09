from collections import Counter
class Solution(object):
    # NSum works for N >= 2
    def NSum(self, nums, target, N, result, results):
        if len(nums) < N or nums[0]*N > target or nums[-1]*N < target or N < 2:
            return results
        # use 2Sum
        if N == 2:
            # special case
            if target/2.0 in nums and Counter(nums)[target/2.0] >= 2:
                results.append(result + [int(target/2.0), int(target/2.0)])
            d = {}
            for i,x in enumerate(set(nums)):
                if target - x in d.keys():
                    results.append(result + [target-x,x])
                else:
                    d[x] = i
            return results
        for i in range(len(nums)-N+1):
            # skip repeating cases
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                results = self.NSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return results
        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.NSum(sorted(nums), target, 4, [], [])
