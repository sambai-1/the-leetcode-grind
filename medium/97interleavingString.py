class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s1) + 1) for i in range(len(s2) + 1)]
        dp[-1][-1] = True
        visited = [[False] * (len(s1) + 1) for i in range(len(s2) + 1)]
        def dfs(x, y, i):
            if visited[x][y]:
                return dp[x][y]

            if x < len(s2) and y < len(s1) and s2[x] == s1[y] == s3[i]:
                dp[x][y] = dfs(x + 1, y, i + 1) or dfs(x, y + 1, i + 1)
            elif x < len(s2) and s2[x] == s3[i]:
                dp[x][y] = dfs(x + 1, y, i + 1)
            elif y < len(s1) and s1[y] == s3[i]:
                dp[x][y] = dfs(x, y + 1, i + 1)
            
            visited[x][y] = True
            return dp[x][y]
        
        return dfs(0, 0, 0)