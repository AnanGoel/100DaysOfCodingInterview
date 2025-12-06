Day 42 – Construct Binary Tree from Traversals (Python)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1️⃣ Construct Binary Tree from Preorder and Inorder Traversal (Medium)
    def buildTreePreIn(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            in_root_index = inorder_index[root_val]
            left_size = in_root_index - in_start
            
            root.left = helper(pre_start + 1, pre_start + left_size, in_start, in_root_index - 1)
            root.right = helper(pre_start + left_size + 1, pre_end, in_root_index + 1, in_end)
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
    
    # 2️⃣ Construct Binary Tree from Inorder and Postorder Traversal (Medium)
    def buildTreeInPost(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None
            
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            in_root_index = inorder_index[root_val]
            left_size = in_root_index - in_start
            
            root.left = helper(in_start, in_root_index - 1, post_start, post_start + left_size - 1)
            root.right = helper(in_root_index + 1, in_end, post_start + left_size, post_end - 1)
            
            return root
        
        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
