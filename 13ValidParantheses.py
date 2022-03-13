# Question: https://leetcode.com/problems/valid-parentheses/

# Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            elif stack[-1] == "[" and i == "]" or stack[-1] == "(" and i == ")" or stack[-1] == "{" and i == "}":
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
          
# Verdict:
# Runtime: 36 ms, faster than 75.07% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 82.06% of Python3 online submissions for Valid Parentheses.
