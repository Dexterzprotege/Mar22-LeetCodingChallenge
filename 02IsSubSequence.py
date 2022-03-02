# Question: https://leetcode.com/problems/is-subsequence/submissions/

# ------------------------------------------------------------------------------------------- #

# Solution: Two Pointer Technique
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
      
# Verdict:
# Runtime: 36 ms, faster than 78.02% of Python3 online submissions for Is Subsequence.
# Memory Usage: 13.9 MB, less than 92.79% of Python3 online submissions for Is Subsequence.

# ------------------------------------------------------------------------------------------- #

# Solution: Dynamic Programming
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[0 for x in range(n+1)] for y in range(m+1)] 
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return m == dp[m][n]
      
# Verdict:
# Runtime: 179 ms, faster than 5.02% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14.8 MB, less than 9.28% of Python3 online submissions for Is Subsequence.

# ------------------------------------------------------------------------------------------- #
