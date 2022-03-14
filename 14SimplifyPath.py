# Question: https://leetcode.com/problems/simplify-path/

# Solution:
class Solution:
    def simplifyPath(self, path: str) -> str:
        places = [p for p in path.split("/") if p!="." and p!=""]
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
            
# Verdict:
# Runtime: 86 ms, faster than 5.02% of Python3 online submissions for Simplify Path.
# Memory Usage: 14 MB, less than 57.22% of Python3 online submissions for Simplify Path.
