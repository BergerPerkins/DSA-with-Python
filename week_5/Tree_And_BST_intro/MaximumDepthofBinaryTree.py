
########     https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## base case condition
        if root is None:
            return 0
        ## recursive function calls
        else:
            lheight = self.maxDepth(root.left)
            rheight = self.maxDepth(root.right)
        return max(lheight, rheight) + 1 