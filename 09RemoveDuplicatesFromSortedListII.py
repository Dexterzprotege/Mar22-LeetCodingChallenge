# Question: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Solution:# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, dummy.next
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                dupe_val = curr.val
                while curr and curr.val == dupe_val:
                    curr = curr.next
                
                prev.next = curr
            else:
                prev, curr = curr, curr.next
        return dummy.next
      
# Verdict:
# Runtime: 63 ms, faster than 41.57% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.9 MB, less than 85.61% of Python3 online submissions for Remove Duplicates from Sorted List II
