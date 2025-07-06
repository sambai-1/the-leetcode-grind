from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        ans = []
        start = newInterval[0]
        end = newInterval[1]
        added = False

        for i in range(len(intervals)):
            x, y = intervals[i]
            if (y >= newInterval[0] and y <= newInterval[1]) or (x >= newInterval[0] and x <= newInterval[1]) or (newInterval[0] >= x and newInterval[1] <= y):
                start = min(start, newInterval[0], x)
                end = max(end, newInterval[1], y)

            else:
                if x > end and not added:
                    ans.append([start, end])
                    added = True
                ans.append([x, y])
        
        if not added:
            ans.append([start, end])

        return ans