# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.check_height_balanced(root)
        return self.ans
    
    def check_height_balanced(self, root) :
        if root is None or self.ans == False : return

        lh = self.get_height(root.left)
        rh = self.get_height(root.right)

        if abs(lh - rh) >= 2 :
            self.ans = False
            return
        
        self.check_height_balanced(root.left)
        self.check_height_balanced(root.right)
    
    def get_height(self, root) :
        if root is None :
            return 1
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
