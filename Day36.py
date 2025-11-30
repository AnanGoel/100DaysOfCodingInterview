Day 36 — Binary Tree Level Order Variations
1) LeetCode 107: Binary Tree Level Order Traversal II

Problem:
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.

Code (Python):

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Insert at the beginning for bottom-up order
            result.insert(0, level_nodes)
        
        return result

2) LeetCode 103: Binary Tree Zigzag Level Order Traversal

Problem:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.

Code (Python):

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level_nodes = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level_nodes))
            left_to_right = not left_to_right
        
        return result
