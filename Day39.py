Day 39 – Binary Tree Depths (Python)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1️⃣ Maximum Depth of Binary Tree
    def maxDepth(self, root):
        """
        Returns the maximum depth (longest path from root to leaf)
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

    # 2️⃣ Minimum Depth of Binary Tree
    def minDepth(self, root):
        """
        Returns the minimum depth (shortest path from root to leaf)
        """
        if not root:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        # If one child is missing, take the depth of the existing child
        if not root.left or not root.right:
            return 1 + max(left_depth, right_depth)
        
        return 1 + min(left_depth, right_depth)
