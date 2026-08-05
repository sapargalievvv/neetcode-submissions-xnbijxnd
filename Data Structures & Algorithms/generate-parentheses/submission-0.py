class Solution:
    def generateParenthesis(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(current, left, right):
            if len(current) == n * 2:
                res.append(current)
                return

            if left < n:
                backtrack(current + "(", left + 1, right)
            
            if left > right:
                backtrack(current + ")", left, right + 1)

        backtrack("", 0, 0)

        return res
