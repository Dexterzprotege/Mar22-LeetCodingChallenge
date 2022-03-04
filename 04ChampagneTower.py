# Question: https://leetcode.com/problems/champagne-tower/

# Solution
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [0]*(query_row+2)
        res[0] = poured
        for row in range(1, query_row+1):
            for i in range(row, -1, -1):
                res[i] = max(res[i] - 1, 0) / 2.0 + max(res[i - 1] - 1, 0) / 2.0
        return min(res[query_glass], 1)
                
# Verdict:
# Runtime: 225 ms, faster than 32.04% of Python3 online submissions for Champagne Tower.
# Memory Usage: 14 MB, less than 81.55% of Python3 online submissions for Champagne Tower.
