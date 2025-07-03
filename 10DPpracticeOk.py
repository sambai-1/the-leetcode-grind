class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1] * (len(s) + 1) for _ in range(len(p))]


        def dfs(x, y):
            if x == len(p) and y == len(s):
                return True
            elif x == len(p) or y > len(s):
                return False
            if dp[x][y] != -1:
                return dp[x][y]
            
            current = dp[x][y]
            if (x < (len(p) - 1) and p[x + 1] == "*"):
                if y == len(s):
                    current = dfs(x + 2, y)
                elif p[x] == s[y] or p[x] == ".":
                    current = dfs(x, y + 1) or dfs(x + 2, y) or dfs(x + 2, y + 1)
                else:
                    current = dfs(x + 2, y)
            else:
                if y == len(s):
                    return False
                elif p[x] == s[y] or p[x] == ".":
                    current = dfs(x + 1, y + 1)
                else:
                    current = False or dfs(x + 1, y)

            
            dp[x][y] = current
            return current
        
        return dfs(0, 0)