from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        window = deque()
        l, r = 0, 0
        while r < len(nums):
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)

            if l > window[0]:
                window.popleft()
            if r > k - 2:
                ans.append(nums[window[0]])
                l += 1
            r += 1

        return ans
        
        """or this
        class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windows = deque()
        for i in range(len(nums)):
            start, end = i - k + 1, i + 1
            start = 0 if start < 0 else start
            end = 0 if end < 0 else end
            while windows and windows[-1][0] < nums[i] and windows[-1][1] >= start:
                windows.pop()
            if windows:
                if windows[-1][0] < nums[i]:
                    windows[-1][2] = start
                else:
                    start = windows[-1][2]
            windows.append([nums[i], start, end])
        
        ans = []
        for i in windows:
            for j in range(i[1], i[2]):
                if len(ans) == (len(nums) - k + 1):
                    return ans
                ans.append(i[0])
        return ans
        """