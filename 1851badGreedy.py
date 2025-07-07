class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        todo = queries.copy()
        todo.sort()
        ans = {}
        heap = []
        j = 0
        for i in todo:
            while j < len(intervals) and intervals[j][0] <= i:
                heapq.heappush(heap, [intervals[j][1] - intervals[j][0] + 1, intervals[j][1]])
                j += 1
            while True:
                if len(heap) == 0:
                    ans[i] = -1
                    break
                else:
                    curr = heap[0]
                    if curr[1] >= i:
                        ans[i] = curr[0]
                        break
                    else:
                        heapq.heappop(heap)
        
        for i in range(len(queries)):
            queries[i] = ans[queries[i]]
        
        return queries