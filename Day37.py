📌 1. LeetCode 199 — Binary Tree Right Side View

Problem:
Return the values of the nodes visible from the right side of the binary tree.

✅ Python Code
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # Last node at each level (right view)
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

📌 2. Left View of Binary Tree (GFG)

Problem:
Return the nodes visible from the left side of the binary tree.

✅ Python Code
# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def leftView(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # First node at each level (left view)
                if i == 0:
                    result.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


✅ Used concept: Level Order Traversal (BFS)
✅ Time Complexity: O(n)
✅ Space Complexity: O(n)
✅ Logic:

Left View → First node of each level

Right View → Last node of each level
