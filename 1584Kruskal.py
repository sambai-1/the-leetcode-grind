import heapq


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        connect = [-1] * len(points)
        def parent(curr):
            if connect[curr] == -1:
                return curr
            return parent(connect[curr])
        
        ans = 0
        dist = []
        for i in range(len(points)):
            for j in range(len(points)):
                heapq.heappush(dist, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
            
        while dist:
            length, i, j = heapq.heappop(dist)
            if parent(i) != parent(j):
                ans+=length
                connect[parent(i)] = parent(j)

        return ans