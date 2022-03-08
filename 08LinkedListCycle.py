# Question: https://leetcode.com/problems/linked-list-cycle/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
# Verdict:
# Runtime: 56 ms, faster than 88.97% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.7 MB, less than 42.75% of Python3 online submissions for Linked List Cycle.
