class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        tested = {"": True}
        def dfs(rest):
            if rest in tested:
                return tested[rest]
            for i in range(1, len(rest) + 1):
                tmp = rest[0:i]
                if tmp in wordDict:
                    print(tmp, rest[i:])
                    if dfs(rest[i:]):
                        tested[rest] = True
                        return True
            tested[rest] = False
            return False
        return dfs(s)