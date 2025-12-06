# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1️⃣ Path Sum (Easy)
    def hasPathSum(self, root, targetSum):
        """
        Returns True if there is a root-to-leaf path with sum equal to targetSum
        """
        if not root:
            return False
        
        # If leaf node, check if path sum equals targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check left and right subtree
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))

    # 2️⃣ Path Sum II (Medium)
    def pathSum(self, root, targetSum):
        """
        Returns all root-to-leaf paths where sum of values equals targetSum
        """
        result = []

        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            current_path.append(node.val)
            current_sum += node.val
            
            # If leaf node and path sum matches targetSum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))
            else:
                dfs(node.left, current_path, current_sum)
                dfs(node.right, current_path, current_sum)
            
            # Backtrack
            current_path.pop()
        
        dfs(root, [], 0)
        return result
