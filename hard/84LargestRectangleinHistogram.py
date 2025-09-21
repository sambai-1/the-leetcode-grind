from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        bars = deque()

        for i in range(len(heights)):
            curr = heights[i]
            prev = i
            while bars and curr <= bars[-1][0]:
                prev = bars[-1][1]
                x, y = bars.pop()
                ans = max(ans, x * (i - y))
            bars.append((curr, prev))
        
        return max(ans, max([(len(heights) - y) * x for x, y in bars]))