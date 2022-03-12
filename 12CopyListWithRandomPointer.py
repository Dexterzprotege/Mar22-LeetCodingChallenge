# Question: https://leetcode.com/problems/copy-list-with-random-pointer/

# Solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = dict()
        m = n = head
        while m:
            dic[m] = ListNode(m.val)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)
      
# Verdict:
# Runtime: 56 ms, faster than 42.66% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 14.9 MB, less than 55.97% of Python3 online submissions for Copy List with Random Pointer.
