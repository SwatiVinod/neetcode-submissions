"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_to_clone_mapping = {}

        def dfs(node):
            curr = node

            if curr in node_to_clone_mapping:
                return node_to_clone_mapping[curr]
            
            new_node = Node(curr.val)
            node_to_clone_mapping[curr] = new_node

            for neighbour in curr.neighbors:
                new_node.neighbors.append(dfs(neighbour))
            return new_node

        new_node = dfs(node)
        return new_node
        