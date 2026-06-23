from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        land = 2147483647
        rows, cols = len(grid), len(grid[0])

        qu = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    qu.append((row, col))

        while qu:
            r, c = qu.popleft()
            print(r, c)

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                row = r + dr
                col = c + dc

                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != land:
                    continue

                grid[row][col] = grid[r][c] + 1
                qu.append((row,col))
