# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ok = True

        def getLevel(root):
            if not root: return 0

            left = getLevel(root.left)
            right = getLevel(root.right)

            if left - right > 1 or right - left > 1: 
                self.ok = False

            return 1 + max(left,right)

        getLevel(root)

        return self.ok
