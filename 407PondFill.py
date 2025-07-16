import heapq


def trapRainWater(heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        

        todo = []
        visited = set()
        def get(x, y, curr):
            if x < 0 or y < 0 or x >= len(heightMap) or y >= len(heightMap[0]):
                return curr
            if (x, y) not in visited:
                heapq.heappush(todo, (heightMap[x][y], x, y))
            return heightMap[x][y]

        for i in range(len(heightMap[0])):
            heapq.heappush(todo, (heightMap[0][i], 0, i))
            visited.add((0, i))
            if (len(heightMap) - 1, i) not in visited:
                heapq.heappush(todo, (heightMap[len(heightMap) - 1][i], len(heightMap) - 1, i))
                visited.add((len(heightMap) - 1, i))
        
        for j in range(1, len(heightMap) - 1):
            if (j, 0) not in visited:
                heapq.heappush(todo, (heightMap[j][0], j, 0))
                visited.add((j, 0))
            if (j, len(heightMap[0]) - 1) not in visited:
                heapq.heappush(todo, (heightMap[j][len(heightMap[0]) - 1], j, len(heightMap[0]) - 1))
                visited.add((j, len(heightMap[0]) - 1))
        visited.clear()
        print(todo)
        ans = 0
        while todo:
            curr, x, y = heapq.heappop(todo)
        
            if (x, y) in visited:
                continue

            least = min(get(x, y + 1, curr), get(x, y - 1, curr), get(x + 1, y, curr), get(x - 1, y, curr))
            ans += (least - curr) if least > curr else 0
            print(x, y)
            heightMap[x][y] = max(least, curr)

            visited.add((x, y))
            
        return ans
    
    
print(trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))