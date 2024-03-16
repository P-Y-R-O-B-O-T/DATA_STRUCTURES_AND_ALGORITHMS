# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.height = 0

        self. get_height(root, 1)

        return self.height
    
    def get_height(self, root, level) :
        if root is None : return

        self.height  = max(self.height, level)

        self.get_height(root.left, level+1)
        self.get_height(root.right, level+1)
