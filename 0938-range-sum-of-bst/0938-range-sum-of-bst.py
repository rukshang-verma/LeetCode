# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
       
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(root):
            if not root:
                return
            if low <= root.val <= high:
                self.res += root.val
            if low <= root.val:
                dfs(root.left)
            if high >= root.val:
                dfs(root.right)
        self.res = 0
        dfs(root)
        return self.res
        