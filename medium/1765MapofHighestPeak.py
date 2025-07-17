from collections import deque

#To add seed all into deque at same time rather than one by one

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = [[-1] * len(isWater[0]) for _ in range(len(isWater))]
        todo = deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]:
                    todo.append((i, j, 0))
                    ans[i][j] = 0

        while todo:
            r, c, curr = todo.popleft()
            direct =((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1))
            for i, j in direct:
                if i < 0 or j < 0 or i >= len(isWater) or j >= len(isWater[0]):
                    continue
                if ans[i][j] == -1:
                    ans[i][j] = curr + 1
                    todo.append((i, j, curr + 1))
                    
        return ans