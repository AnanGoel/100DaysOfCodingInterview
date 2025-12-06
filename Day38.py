1️⃣ Vertical Order Traversal (Hard)
from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []

        nodes = defaultdict(list)
        queue = deque([(root, 0, 0)])  # (node, row, col)

        while queue:
            node, row, col = queue.popleft()
            nodes[col].append((row, node.val))

            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        result = []
        for col in sorted(nodes.keys()):
            column = sorted(nodes[col])   # sort by row, then value
            result.append([val for row, val in column])

        return result

2️⃣ Diagonal Tree Traversal (Medium)
from collections import deque

class Solution:
    def diagonal(self, root):
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            node = q.popleft()

            while node:
                result.append(node.data)

                # Push left child for the next diagonal
                if node.left:
                    q.append(node.left)

                # Move right on the same diagonal
                node = node.right

        return result
