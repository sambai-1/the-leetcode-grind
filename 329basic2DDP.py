class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        ans = 0
        def dfs(x, y):
            if dp[x][y] != -1:
                return dp[x][y]
            dp[x][y] = 1
            if x < len(matrix) - 1 and matrix[x + 1][y] > matrix[x][y]:
                dp[x][y] = max(dp[x][y], dfs(x + 1, y) + 1) 
            if y < len(matrix[0]) - 1 and matrix[x][y + 1] > matrix[x][y]:
                dp[x][y] = max(dp[x][y], dfs(x, y + 1) + 1) 
            if x > 0 and matrix[x - 1][y] > matrix[x][y]:
                dp[x][y] = max(dp[x][y], dfs(x - 1, y) + 1) 
            if y > 0 and matrix[x][y - 1] > matrix[x][y]:
                dp[x][y] = max(dp[x][y], dfs(x, y - 1) + 1) 
            return dp[x][y]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))
        print(dp)
        return ans