def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    ans = {}
    for i in strs:
        tmp = [0] * 26
        for j in i:
            tmp[ord(j) - ord('i')] += 1
        if tuple(tmp) in ans:
            ans[tuple(tmp)].append(i)
        else:
            ans[tuple(tmp)] = [i]
    
    return list(ans.values())

#next time use defaultdict(list) to initialize ans
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))