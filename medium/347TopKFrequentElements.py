def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = {}
    for i in nums:
        count[i] = 1 + count.get(i, 0)
    
    ans = [[] for i in range(len(nums))]
    for k2, v in count.items():
        ans[v - 1].append(k2)
    
    print(ans)
    result = []
    tmp = 0
    for i in ans[::-1]:
        while len(i) > 0 and tmp < k:
            result.append(i[0])
            i = i[1:]
            tmp += 1

    return result

print(topKFrequent([1,1,1,2,2,3], 2))