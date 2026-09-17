class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vistied = set()
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if (
                row >= ROWS
                or col >= COLS
                or row < 0
                or col < 0
                or (row, col) in vistied
                or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"
            vistied.add((row, col))

            for nr, nc in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
