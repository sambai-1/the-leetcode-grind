class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        tree = [[] for _ in range(n + 1)]
        for x, y, z in times:
            tree[x].append((y, z))

        front = [(0, k)]
        best = [float("INF")] * (n + 1)
        visited = 0
        while front:
            time, current = heapq.heappop(front)
            if best[current] != float("INF"):
                continue
            best[current] = time
            visited += 1
            if visited == n:
                return time
            for y, weight in tree[current]:
                if time + weight < best[y]:
                    heapq.heappush(front, (weight + time, y))
        
        return -1