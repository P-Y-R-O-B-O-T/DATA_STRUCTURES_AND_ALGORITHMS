# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.is_same(p, q)
    
    def is_same(self, r1, r2) :
        if r1 == None and r2 == None :
            return True
        if r1 ==  None and r2 != None or r1 !=  None and r2 == None :
            return False
        
        if r1.val == r2.val :
            a = self.is_same(r1.left, r2.left)
            b = self.is_same(r1.right, r2.right)
            if a and b :
                return True
        return False
