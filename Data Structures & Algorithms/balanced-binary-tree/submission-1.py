# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isOk = True

        def getLevels(root: TreeNode):
            if not root:
                return 0

            left = getLevels(root.left)
            right = getLevels(root.right)

            if left - right > 1 or right - left > 1:
                self.isOk = False

            return 1 + max(left, right)

        getLevels(root)

        return self.isOk
