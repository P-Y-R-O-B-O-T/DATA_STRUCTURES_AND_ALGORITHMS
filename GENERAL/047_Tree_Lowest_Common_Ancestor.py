# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.has_p_map = []
        self.has_q_map = []

        self.has_p(root, p.val)
        self.has_q(root, q.val)

        n = min(len(self.has_p_map), len(self.has_q_map))
        ans_node = None
        
        for _ in range(-1, -n-1, -1) :
            if self.has_p_map[_] == self.has_q_map[_] :
                ans_node = self.has_p_map[_]
        
        return ans_node
    
    def has_p(self, root, p_val) :
        if root is None : return False
        if root.val == p_val :
            self.has_p_map.append(root)
            return True

        a = self.has_p(root.left, p_val)
        b = self.has_p(root.right, p_val)

        if a or b :
            self.has_p_map.append(root)
            return True
        return False
    
    def has_q(self, root, q_val) :
        if root is None : return False
        if root.val == q_val :
            self.has_q_map.append(root)
            return True

        a = self.has_q(root.left, q_val)
        b = self.has_q(root.right, q_val)

        if a or b :
            self.has_q_map.append(root)
            return True
        return False
