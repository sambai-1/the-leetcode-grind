class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        grid = [[-1] * len(text2) for _ in range(len(text1))]
        text1 = text1 + "0"
        text2 = text2 + "0"
        def dfs(x, y):
            if text1[x] == "0" or text2[y] == "0":
                return 0
            if grid[x][y] != -1:
                return grid[x][y]
            if text1[x] == text2[y]:
                grid[x][y] = 1 + dfs(x + 1, y + 1)
            else:
                grid[x][y] = max(dfs(x + 1, y), dfs(x, y + 1))
            return grid[x][y]
        
        return dfs(0, 0)