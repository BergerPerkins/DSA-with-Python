
######        https://leetcode.com/problems/validate-binary-search-tree/    ##########



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            self.result.append(node.val)
            self.inOrderTraversal(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 
        
        self.result = []
        ## function calling
        self.inOrderTraversal(root)

        n = len(self.result)

        # weather the list is sorted or not
        for i in range(n-1):
            if self.result[i] >= self.result[i+1]:
                return False
        return True