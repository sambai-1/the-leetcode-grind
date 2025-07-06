from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            x, y = intervals[i]
            if x < end:
                end = min(end, y)
                ans += 1
            else:
                end = y
            
        return ans