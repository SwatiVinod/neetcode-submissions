# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {ele: index for index, ele in enumerate(inorder)}
        pre_indx = 0

        def dfs(l, r):
            nonlocal pre_indx
            if l > r:
                return None
            
            root_val = preorder[pre_indx]
            root = TreeNode(root_val)
            mid = indices[root_val]
            pre_indx += 1
            
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid+1, r)
            return root

        return dfs(0, len(inorder) - 1)

        