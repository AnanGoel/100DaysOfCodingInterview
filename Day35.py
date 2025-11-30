Day 35 — Binary Tree Traversals
1) LeetCode 144: Binary Tree Preorder Traversal

Problem:
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Code (Python):

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            # Preorder: Root -> Left -> Right
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result

2) LeetCode 94: Binary Tree Inorder Traversal

Problem:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Code (Python):

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            # Inorder: Left -> Root -> Right
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result
