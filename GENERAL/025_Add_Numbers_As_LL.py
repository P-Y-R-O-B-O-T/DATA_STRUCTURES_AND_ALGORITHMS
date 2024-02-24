"""
https://leetcode.com/problems/add-two-numbers/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None : return None
        pl1 = l1
        pl2 = l2
        carry = 0

        result_node = ListNode()
        result_node_pointer = result_node

        while pl1 is not None or pl2 is not None or carry != 0:
            s = 0
            if pl1 is not None : s += pl1.val; pl1 = pl1.next
            if pl2 is not None : s += pl2.val; pl2 = pl2.next

            result_node_pointer.next = ListNode((s+carry)%10)
            result_node_pointer = result_node_pointer.next

            carry = (s+carry) // 10
        
        return result_node.next
