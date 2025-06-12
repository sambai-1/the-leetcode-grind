class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        n = len(grid)
        ans = -1


        while heap:
            curr, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            ans = max(ans, curr)
            if x == n - 1 and y == n - 1:
                break
            
            if x > 0 and (x - 1, y) not in visited:
                heapq.heappush(heap, (grid[x-1][y], x-1, y))
            if y > 0 and (x, y - 1) not in visited:
                heapq.heappush(heap, (grid[x][y-1], x, y-1))
            if x < n - 1 and (x + 1, y) not in visited:
                heapq.heappush(heap, (grid[x+1][y], x+1, y))
            if y < n - 1 and (x, y + 1) not in visited:
                heapq.heappush(heap, (grid[x][y+1], x, y+1))
        
        return ans