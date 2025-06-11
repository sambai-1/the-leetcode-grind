from collections import defaultdict
import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        nodes = defaultdict(list)
        for x, y, t in times:
            nodes[x - 1].append((y - 1, t))
        
        visited = set()
        minTime = {}
        for i in range(n):
            minTime[i] = float("inf")
        minTime[k-1] = 0
        
        currAns = -1
        todo = [(0, k - 1)]
        while todo:
            t, x = heapq.heappop(todo)
            if x in visited:
                continue
            visited.add(x)
            if len(visited) == n:
                currAns = t
                break
            for y, dist in nodes[x]:
                if t + dist < minTime[y]:
                    minTime[y] = t + dist
                    heapq.heappush(todo, (t + dist, y))
        
        return currAns