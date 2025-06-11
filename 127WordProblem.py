class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = defaultdict(list)
        for i in wordList:
            for j in range(len(beginWord)):
                words[i[0:j] + "1" + i[j + 1: len(beginWord)]].append(i)
        

        visited = set()
        def dfs(curr, dist):
            if curr in visited:
                return 102
            dist += 1
            if curr == endWord:
                return dist
            
            todo = set()
            for i in range(len(beginWord)):
                for j in words[curr[0:i] + "1" + curr[i + 1: len(beginWord)]]:
                    todo.add(j)
            
            visited.add(curr)
            ans = 102
            for i in todo:
                print(i)
                ans = min(ans, dfs(i, dist))
            visited.remove(curr)
            return ans

        
        ans = dfs(beginWord, 0)
        if ans == 102:
            return 0
        return ans