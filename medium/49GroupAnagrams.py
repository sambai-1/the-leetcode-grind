def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    ans = {}
    for i in strs:
        tmp = {}
        for j in i:
            tmp[j] = tmp.get(j, 0) + 1
        ans[tmp] = tmp.get(tmp, []).append(i)
    
    return list(ans.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))