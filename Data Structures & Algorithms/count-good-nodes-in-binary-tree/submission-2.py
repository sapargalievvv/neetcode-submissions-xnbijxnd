# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def getGoodNodesCount(node, maxVal):
            if not node: 
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)
            
            left = getGoodNodesCount(node.left, maxVal)
            right = getGoodNodesCount(node.right, maxVal)
            
            return res + right + left

        return getGoodNodesCount(root, root.val)
        