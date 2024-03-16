# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self.max_path_sum(root)
        return self.max_sum
    
    def max_path_sum(self, root) :
        if root is None : return 0

        left_gain = max(self.max_path_sum(root.left), 0)
        right_gain = max(self.max_path_sum(root.right), 0)
        print(left_gain, right_gain)
        self.max_sum = max(self.max_sum, root.val+left_gain+right_gain)
        return root.val + max(left_gain, right_gain)
