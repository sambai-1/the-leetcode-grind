from collections import defaultdict
from typing import List


def foreignDictionary(words: List[str]) -> str:
    rels = {i: set() for word in words for i in word}
        
    for i in range(len(words) - 1):
        a = words[i]
        b = words[i + 1]
        if len(a) > len(b) and a.find(b) == 0:
            return ""
        for j in range(min(len(a), len(b))):
            if a[j] != b[j]:
                rels[b[j]].add(a[j])
                break
    
    print(rels)
    ans = ""
    visited = set()
    completed = set()

    def dfs(curr):
        if curr in completed:
            return True
        if curr in visited:
            return False
        
        visited.add(curr)
        for i in rels[curr]:
            if not dfs(i):
                return False
        visited.remove(curr)
        completed.add(curr)
        nonlocal ans
        ans = ans + curr
        return True

    for k, v, in rels.items():
        if not dfs(k):
            return ""
    
    return ans
    
words = ["hrn","hrf","er","enn","rfnn"]
print(foreignDictionary(words))