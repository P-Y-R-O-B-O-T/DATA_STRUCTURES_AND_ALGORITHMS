# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodes = []
        self.ref = []
        self.get_nodes(root)
        self.gen_ll(root)

    def gen_ll(self, root) :
        for _ in range(len(self.nodes) -1) :
            self.ref[_].right = self.ref[_+1]
        for _ in range(len(self.nodes)) :
            self.ref[_].left = None

    def get_nodes(self, root) :
        if root is None : return

        self.nodes.append(root.val)
        self.ref.append(root)
        self.get_nodes(root.left)
        self.get_nodes(root.right)
