# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.width = 0
        self.get_diameter(root)

        return self.width
    
    def get_diameter(self, root) :
        if root is None : return

        lh = self.get_max_height(root.left)
        rh = self.get_max_height(root.right)
        self.width = max(self.width, lh+rh)

        self.get_diameter(root.left)
        self.get_diameter(root.right)
    
    def get_max_height(self, root) :
        if root is None :
            return 0
        return 1 + max(self.get_max_height(root.left), self.get_max_height(root.right))
