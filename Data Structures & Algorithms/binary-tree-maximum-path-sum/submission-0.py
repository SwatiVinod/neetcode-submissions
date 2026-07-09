# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpathsum  = float('-inf')

        def dfs(node):
            nonlocal maxpathsum
            if not node:
                return 0
            
            left_path_sum = max(dfs(node.left), 0)
            right_pah_sum = max(dfs(node.right), 0)
            path_sum = left_path_sum + right_pah_sum + node.val

            maxpathsum = max(path_sum, maxpathsum)

            return node.val + max(left_path_sum, right_pah_sum)


        dfs(root)
        return maxpathsum
        