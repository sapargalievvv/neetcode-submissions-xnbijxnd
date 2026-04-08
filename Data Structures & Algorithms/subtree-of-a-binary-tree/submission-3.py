# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        def sameThree(r, s):
            if not r and not s: 
                return True
            
            if not r or not s: 
                return False
            
            if r.val != s.val:
                return False

            left = sameThree(r.left, s.left)
            right = sameThree(r.right, s.right)
            
            return left and right

        if sameThree(root, subRoot):
            return True
        
        return self.isSubtree(root.left ,subRoot) or self.isSubtree(root.right, subRoot)

