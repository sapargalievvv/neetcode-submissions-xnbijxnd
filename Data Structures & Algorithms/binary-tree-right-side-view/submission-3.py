# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        result = []

        if not root:
            return result

        while q:
            levelSize = len(q)
            currentLevel = []
            
            for _ in range(levelSize):
                node = q.popleft()
                currentLevel.append(node.val)

                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            lastItem = currentLevel.pop()

            if lastItem:
                result.append(lastItem)
        
        return result



        