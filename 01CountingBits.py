# Question: https://leetcode.com/problems/counting-bits/

# Solution:
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1+dp[i-offset]
        return dp

# Verdict:
# Runtime: 80 ms, faster than 93.31% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.9 MB, less than 20.15% of Python3 online submissions for Counting Bits.
