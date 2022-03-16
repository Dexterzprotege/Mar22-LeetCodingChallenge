# Question: https://leetcode.com/problems/validate-stack-sequences/

# Solution:
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped = popped[::-1]
        
        for i in pushed:
            if i != popped[-1]:
                stack.append(i)
            else:
                popped.pop()
                while stack and stack[-1] == popped[-1]:
                    stack.pop()
                    popped.pop()
        
        return len(stack) == 0
      
# Verdict:
# Runtime: 87 ms, faster than 69.83% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.2 MB, less than 34.77% of Python3 online submissions for Validate Stack Sequences.
