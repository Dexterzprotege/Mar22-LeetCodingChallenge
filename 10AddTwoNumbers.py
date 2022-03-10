# Question: https://leetcode.com/problems/add-two-numbers/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0
        while l1 or l2:
            v1, v2 = 0, 0
            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next
            
            val = carry + v1 + v2
            res.next = ListNode(val%10)
            res, carry = res.next, val//10
            
        if carry:
            res.next = ListNode(carry)
            
        return dummy.next
      
# Verdict:
# Runtime: 138 ms, faster than 12.11% of Python3 online submissions for Add Two Numbers.
#c Memory Usage: 13.9 MB, less than 65.79% of Python3 online submissions for Add Two Numbers.
