# Question: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Solution:
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)
      
# Verdict:
# Runtime: 125 ms, faster than 73.45% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 15.7 MB, less than 66.40% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
