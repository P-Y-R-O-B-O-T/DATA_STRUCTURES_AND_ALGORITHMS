# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = {}

        self.level_order(root, 0)

        final_ans = []
        levels = list(self.ans.keys())
        levels.sort()
        for _ in levels :
            final_ans.append(self.ans[_])
        
        return final_ans
    
    def level_order(self, root, level) :
        if root is None :
            return
        
        self.level_order(root.left, level+1)
        if level not in self.ans :
            self.ans[level] = []
        self.ans[level].append(root.val)
        self.level_order(root.right, level+1)
