# Question: https://leetcode.com/problems/score-of-parentheses/

# Solution:
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for i in s:
            if i == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2*val, 1)
        return stack.pop()
      
# Verdict:
# Runtime: 32 ms, faster than 86.28% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 13.9 MB, less than 70.86% of Python3 online submissions for Score of Parentheses.
