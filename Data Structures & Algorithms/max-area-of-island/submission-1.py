class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            top = dfs(r - 1, c)
            right = dfs(r, c + 1)
            bottom = dfs(r + 1, c)
            left = dfs(r, c - 1)

            return 1 + top + right + bottom + left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    print("area", area)
                    maxArea = max(maxArea, area)

        return maxArea
