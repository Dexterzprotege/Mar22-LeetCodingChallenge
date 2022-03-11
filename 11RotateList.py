# Question: https://leetcode.com/problems/rotate-list/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        tail.next = head
         
        k = k % n
         
        for i in range(0, n-k):
            tail = tail.next
        
        head = tail.next
        tail.next = None
    
        return head
        
# Verdict:
# Runtime: 49 ms, faster than 63.02% of Python3 online submissions for Rotate List.
# Memory Usage: 14 MB, less than 32.21% of Python3 online submissions for Rotate List.
