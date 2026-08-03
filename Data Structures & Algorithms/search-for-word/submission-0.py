class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtrack(r, c, start):
            if start == len(word):
                return True

            if (
                r >= rows
                or c >= cols
                or r < 0
                or c < 0
                or (r, c) in visited
                or word[start] != board[r][c]
            ):
                return False
            else:
                visited.add((r, c))
                for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    new_row = dr + r
                    new_col = dc + c
                    if backtrack(new_row, new_col, start + 1):
                        return True
                visited.remove((r, c))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False
