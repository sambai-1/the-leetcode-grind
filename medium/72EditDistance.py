class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0:
            return len(word2)
        dp = {}

        def dfs(x, y):
            if (x, y) in dp:
                return dp[(x, y)]
            if y == len(word2):
                return len(word1) - x
            if x == len(word1):
                return len(word2) - y
            
            if word1[x] == word2[y]:
                dp[(x, y)] = dfs(x + 1, y + 1)
                
            else:
                a = 1 + dfs(x + 1, y)
                b = 1 + dfs(x, y + 1)
                c = 1 + dfs(x + 1, y + 1)
                curr = min(a, b, c)
                dp[(x, y)] = curr

            return dp[(x, y)]
        
        return dfs(0, 0)