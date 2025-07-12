'''class Solution(object):
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
        '''
        
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    checked = [0] * len(s)

    def dfs(index):
        if index == len(s):
            return True
        if checked[index]:
            return checked[index]
        
        checked[index] = False
        for i in range(index, len(s)):
            word = s[index: i + 1]
            if word in wordDict:
                checked[index] = checked[index] or dfs(i + 1)
        return checked[index]

    return dfs(0)

print(wordBreak(s = "catsincars", wordDict = ["cats","cat","sin","in","car"]))