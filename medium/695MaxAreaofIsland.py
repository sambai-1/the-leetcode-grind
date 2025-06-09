class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        ans = 0
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or (x, y) in visited:
                return 0
            visited.add((x, y))
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x, y + 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and ((i, j) not in visited):
                    ans = max(ans, dfs(i, j))
        return ans