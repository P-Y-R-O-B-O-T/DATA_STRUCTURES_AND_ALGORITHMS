# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = {}
        self.traverse_vertical(root, 0,0)
        x_indexes = list(self.ans.keys())
        x_indexes.sort()

        final_ans = []

        print(self.ans)

        for _ in x_indexes :
            final_ans.append([])
            sorted_level = list(self.ans[_].keys())
            sorted_level.sort()
            for __ in sorted_level :
                self.ans[_][__].sort()
                final_ans[-1] = final_ans[-1] + self.ans[_][__]

        print(self.ans)

        return final_ans

    def traverse_vertical(self, root, x_axis, level) :
        if root is None :
            return

        if x_axis not in self.ans :
            self.ans[x_axis] = {}
        if level not in self.ans[x_axis] :
            self.ans[x_axis][level] = []
        self.ans[x_axis][level].append(root.val)

        self.traverse_vertical(root.left, x_axis-1, level+1)
        self.traverse_vertical(root.right, x_axis+1, level+1)
