"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()

        ans = 0
        curr = 0
        i = j = 0
        while i < len(intervals):
            if start[i] < end[j]:
                curr += 1
                i += 1
            else:
                curr -= 1
                j += 1
            ans = max(ans, curr)

        return ans