# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        def height(node):
            nonlocal max_height
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            max_height = max(max_height, left_height + right_height)

            return 1 + max(left_height, right_height)
        height(root)
        return max_height