import heapq


def trapRainWater(heightMap):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    considering = set()
    ans = 0
    
    def assign(x, y, curr):
        
        if x < 0 or y < 0 or x >= len(heightMap) or y >= len(heightMap[0]):
            return
        if (x, y) not in considering:
            considering.add((x, y))
            tmp = max(curr, heightMap[x][y])
            heapq.heappush(todo, (tmp, x, y))

    for i in range(len(heightMap[0])):
        considering.add((0, i))
        considering.add((len(heightMap) - 1, i))
    for i in range(len(heightMap)):
        considering.add((i, 0))
        considering.add((i, len(heightMap[0]) - 1))
    todo = []
    for x, y in considering:
        heapq.heappush(todo, (heightMap[x][y], x, y))

    while todo:
        height, x, y = heapq.heappop(todo)
        
        if height > heightMap[x][y]:
            ans += height - heightMap[x][y]
            heightMap[x][y] = height
        assign(x + 1, y, heightMap[x][y])
        assign(x, y + 1, heightMap[x][y])
        assign(x - 1, y, heightMap[x][y])
        assign(x, y - 1, heightMap[x][y])

    
print(trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))

"""class Solution(object):
    def trapRainWater(self, heightMap):
        ans = 0
        maxHeight = 0
        considering = set()
        for i in range(len(heightMap[0])):
            considering.add((0, i))
            considering.add((len(heightMap) - 1, i))
        for i in range(len(heightMap)):
            considering.add((i, 0))
            considering.add((i, len(heightMap[0]) - 1))
        todo = []
        for x, y in considering:
            heapq.heappush(todo, (heightMap[x][y], x, y))
            heightMap[x][y] = -1

        while todo:
            height, x, y = heapq.heappop(todo)
            maxHeight = max(maxHeight, height)
            ans += (maxHeight - height)
            
            moves = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
            for r, c in moves:
                if r < 0 or r >= len(heightMap) or c < 0 or c >= len(heightMap[0]) or heightMap[r][c] == -1:
                    continue
                else:
                    heapq.heappush(todo, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        return ans      

"""