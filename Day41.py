Day 41 – Tree Comparison Problems (Python)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1️⃣ Same Tree (Easy)
    def isSameTree(self, p, q):
        """
        Checks if two binary trees are structurally identical and have the same node values
        """
        # Both nodes are None
        if not p and not q:
            return True
        # One node is None or values differ
        if not p or not q or p.val != q.val:
            return False
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 2️⃣ Symmetric Tree (Easy)
    def isSymmetric(self, root):
        """
        Checks if a binary tree is symmetric around its center
        """
        if not root:
            return True
        
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)
