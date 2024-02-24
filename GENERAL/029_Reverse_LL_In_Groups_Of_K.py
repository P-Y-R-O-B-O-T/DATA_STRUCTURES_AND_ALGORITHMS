"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head

        while node is not None :
            temp_node = node
            data = []
            found = 0

            for _ in range(k) :
                if temp_node is not None :
                    found += 1
                    data.append(temp_node.val)
                    temp_node = temp_node.next
                else : break
            
            if found == k :
                for _ in data[::-1] :
                    node.val = _
                    node = node.next
            else : break
        
        return head
