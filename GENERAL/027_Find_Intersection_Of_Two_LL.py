"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA

        m = {}
        while pa is not None :
            m[id(pa)] = pa
            pa = pa.next
        
        pb = headB

        while pb is not None :
            if id(pb) in m :
                return pb
            pb = pb.next
