"""

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def topSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = {}
        self.visited_levels = 0
        self.top_view(root, 1)

        return [self.ans[_] for _ in list(self.ans.keys()).sorted()]
    
    def top_view(self, root, x_axis) :
        if root is None :
            return

        if x_axis not in self.ans :
            self.ans[x_axis] = root.val
        self.top_view(root.left, x_axis-1)
        self.top_view(root.right, x_axis+1)
