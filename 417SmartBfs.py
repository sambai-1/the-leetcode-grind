#maybe try dfs next time
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = deque()
        for i in range(len(heights)): #0 for pacific 1 for atlantic
            queue.append((i, 0, 0, -1))
            queue.append((i, len(heights[0]) - 1, 1, -1))
        
        for i in range(len(heights[0])):
            queue.append((0, i, 0, -1))
            queue.append((len(heights) - 1, i, 1, -1))
        
        ans = [[[False, False] for j in range(len(heights[0]))] for i in range(len(heights))]
        
        while queue:
            x, y, ocean, prev = queue.popleft()
            if x < 0 or y < 0 or x >= len(heights) or y >= len(heights[0]) or heights[x][y] < prev or ans[x][y][ocean]:
                continue
            ans[x][y][ocean] = True

            queue.append((x + 1, y, ocean, heights[x][y]))
            queue.append((x - 1, y, ocean, heights[x][y]))
            queue.append((x, y - 1, ocean, heights[x][y]))
            queue.append((x, y + 1, ocean, heights[x][y]))      

          
        real = []
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                print(ans[i][j])
                if all (ans[i][j]):
                    real.append([i, j])
        return real    