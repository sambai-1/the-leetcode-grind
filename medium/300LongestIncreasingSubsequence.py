from bisect import bisect_left
from typing import List


'''def lengthOfLIS(nums):
    sub = []
    for num in nums:
        i = bisect_left(sub,num)

        #If index is greater than any element in the current sub array
        if i == len(sub):
            sub.append(num)

        #Otherwise, replace the first element in the current sub array
        #greater than or equal to num
        else:
            sub[i] = num
    return len(sub)

print(lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))

huhr???? how would i come up with this solution
'''