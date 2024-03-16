# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = {}

        self.zigzag_traverse(root, 0)

        final_ans = []
        count = 0

        for _ in sorted(list(self.ans.keys())) :
            final_ans.append(self.ans[_])
            if count % 2 == 1 :
                final_ans[-1].reverse()
            count += 1

        return final_ans

    def zigzag_traverse(self, root, level) :
        if root is None : return

        self.zigzag_traverse(root.left, level+1)
        if level not in self.ans :
            self.ans[level] = []
        self.ans[level].append(root.val)
        self.zigzag_traverse(root.right, level+1)
