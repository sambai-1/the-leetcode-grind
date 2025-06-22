class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = {}
        def dfs(x, y):
            if y == len(t):
                return 1
            if x == len(s):
                return 0
            if (x, y) in dp:
                return dp[(x, y)]
            if s[x] == t[y]:
                dp[(x, y)] = dfs(x + 1, y + 1) + dfs(x + 1, y)
            else:
                dp[(x, y)] = dfs(x + 1, y)
            return dp[(x, y)]
                

        return dfs(0, 0)