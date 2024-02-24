"""
https://leetcode.com/problems/middle-of-the-linked-list/
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None : return None
        if head.next is None : return head

        slow = head
        fast = head

        while fast is not None and fast.next is not None : # the only imp condition
            slow = slow.next
            fast = fast.next.next     
        return slow
