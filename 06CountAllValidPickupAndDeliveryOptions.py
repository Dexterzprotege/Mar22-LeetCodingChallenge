# Question: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

# Solution:
class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 1
        for i in range(2, n+1):
            spaceNum = (i-1)*2 + 1
            ans *= spaceNum * (spaceNum + 1)/2
            ans %= mod
        return int(ans)
      
# Verdict:
# Runtime: 47 ms, faster than 62.22% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 13.9 MB, less than 88.07% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
