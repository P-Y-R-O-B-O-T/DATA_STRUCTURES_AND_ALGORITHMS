"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node_p = node

        while node_p is not None :
            node_p.val = node_p.next.val
            if node_p.next.next is None :
                node_p.next = None
                break
            node_p = node_p.next
