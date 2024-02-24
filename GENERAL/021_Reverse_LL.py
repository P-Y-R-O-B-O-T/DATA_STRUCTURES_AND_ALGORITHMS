"""
https://leetcode.com/problems/reverse-linked-list/
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None : return None
        if head.next is None : return head

        self.new_node = None
        self.reverse_ll(head)
        head.next = None

        return self.new_node
    
    def reverse_ll(self, ll) :
        if ll.next is not None :
            if ll.next.next is None :
                self.new_node = ll.next
            self.reverse_ll(ll.next)
            ll.next.next = ll
