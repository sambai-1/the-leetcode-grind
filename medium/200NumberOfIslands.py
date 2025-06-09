class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        ans = 0
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0" or (x, y) in visited:
                return
            visited.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (not (i, j) in visited):
                    dfs(i, j)
                    ans += 1
        return ans