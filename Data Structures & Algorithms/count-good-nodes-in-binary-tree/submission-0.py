# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, float('-inf')))
        result = 0

        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                result +=1

            if node.left:
                queue.append((node.left, max(max_val, node.val)))
            
            if node.right:
                queue.append((node.right, max(max_val, node.val)))
        return result


