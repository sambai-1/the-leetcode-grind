from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    ans = float("inf")
    while l <= r:
        left, right = nums[l], nums[r]
        m = (l + r) // 2
        mid = nums[m]
        ans = min(ans, mid)
        if left < right:
            ans = min(ans, left)
            return ans
        elif right < left:
            if mid < right:
                r = m - 1
            else:
                l = m + 1
        else:
            return ans

    return ans

nums=[4,5,0,1,2,3]
print(findMin(nums))