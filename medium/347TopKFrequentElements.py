
def topKFrequent( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    ans = {}
    most = 0
    for i in nums:
        ans[i] = 1 + ans.get(i, 0)
        most = max(most, ans[i])
    result = [[] for _ in range(most)]
    for key, value in ans.items():
        result[value - 1].append(key)
    actual = []
    for i in range(most - 1, -1, -1):
        if k <= 0:
            return actual
        k-=len(result[i])
        actual.extend(result[i])
    return actual

print(topKFrequent([1,1,1,2,2,3], 2))