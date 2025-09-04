# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            if l == -1:
                return -1
            r = dfs(root.right)
            if r == -1:
                return -1
            if abs(l-r) > 1:
                return -1
            return 1+max(l,r)
        sol = dfs(root)
        if sol>=0:
            return True
        return False
        