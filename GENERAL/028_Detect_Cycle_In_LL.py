"""
https://leetcode.com/problems/linked-list-cycle/
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head_p = head
        m = {}
        while head_p is not None :
            if id(head_p) in m :
                return True
            m[id(head_p)] = 1
            head_p = head_p.next
        return False
