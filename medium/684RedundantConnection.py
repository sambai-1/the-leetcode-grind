class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        edge = [-1] * len(edges)
        def parent(curr):
            if edge[curr] == -1:
                return curr
            return parent(edge[curr])
        
        for x, y in edges:
            x = x - 1
            y = y - 1
            if parent(x) == parent(y):
                return [x + 1, y + 1]
            x = parent(x)
            y = parent(y)
            edge[min(x, y)] = max(x, y)
        