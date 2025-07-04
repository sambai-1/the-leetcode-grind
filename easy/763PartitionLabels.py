from typing import List


def partitionLabels(s: str) -> List[int]:
    letters = {}
    for i in range(len(s)):
        letters[s[i]] = i
    
    ans = []
    l = curr = r = 0
    while r < len(s):
        while curr <= r:
            r = max(r, letters[s[curr]])
            curr += 1
        ans.append(r - l + 1)
        l = r = curr
    return ans

s="xyxxyzbzbbisl"
print(partitionLabels(s))