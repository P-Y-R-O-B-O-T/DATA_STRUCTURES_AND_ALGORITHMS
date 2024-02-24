"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = self.get_len(head)

        if len_list - n == 0:
            return head.next
        
        deletion_counter = head

        for _ in range(len_list-n-1) :
            deletion_counter = deletion_counter.next
        
        deletion_counter.next = deletion_counter.next.next

        return head

    def get_len(self, ll):
        count = 0
        pointer = ll

        while pointer is not None:
            pointer = pointer.next
            count += 1

        return count
