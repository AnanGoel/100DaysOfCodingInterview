# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    # 1️⃣ Maximum Difference Between Node and Ancestor (Medium)
    def maxAncestorDiff(self, root):
        self.max_diff = 0
        
        def dfs(node, cur_min, cur_max):
            if not node:
                return
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            self.max_diff = max(self.max_diff, cur_max - cur_min)
            dfs(node.left, cur_min, cur_max)
            dfs(node.right, cur_min, cur_max)
        
        dfs(root, root.val, root.val)
        return self.max_diff

    # 2️⃣ All Nodes Distance K in Binary Tree (Medium)
    def distanceK(self, root, target, k):
        graph = defaultdict(list)
        
        # Build undirected graph from tree
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        build_graph(root, None)
        
        # BFS from target
        visited = set()
        queue = deque([(target.val, 0)])
        visited.add(target.val)
        result = []
        
        while queue:
            node_val, dist = queue.popleft()
            if dist == k:
                result.append(node_val)
            elif dist < k:
                for neighbor in graph[node_val]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
        
        return result
