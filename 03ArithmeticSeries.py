# Question: https://leetcode.com/problems/arithmetic-slices/

# Solution:
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        
        return sum(dp)
      
# Verdict:
# Runtime: 44 ms, faster than 72.54% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.1 MB, less than 75.02% of Python3 online submissions for Arithmetic Slices.
