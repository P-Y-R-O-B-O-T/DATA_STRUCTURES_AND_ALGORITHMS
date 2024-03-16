"""

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.visited_levels = 0
        self.left_view(root, 1)

        return self.ans
    
    def left_view(self, root, level) :
        if root is None :
            return

        if level > self.visited_levels :
            self.ans.append(root.val)
            self.visited_levels += 1
        self.left_view(root.left, level+1)
        self.left_view(root.right, level+1)
