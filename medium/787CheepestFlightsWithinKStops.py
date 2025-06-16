from collections import defaultdict
import heapq


def findCheapestPrice(n, flights, src, dst, k):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type k: int
    :rtype: int
    """
    flight = defaultdict(list)
    for i in flights:
        print(i)
        x, y, d = i[0], i[1], i[2]
        flight[x].append((y, d))
    
    todo = [(0, src, k + 1)]
    ans = 100000001
    while todo:
        currd, x, left = heapq.heappop(todo)
        if x == dst:
            ans = min(ans, currd)


        if left > 0:
        
                
            for y, newd in flight[x]:
                heapq.heappush(todo, (newd + currd, y, left - 1))
    
    if ans == 100000001:
        return -1
    return ans


print(findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))