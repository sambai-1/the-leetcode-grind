class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        d1 = {}
        d2 = {}
        for i in range(26):
            curr = chr(ord("a") + i)
            d1[curr] = 0
            d2[curr] = 0

        for i in range(len(s1)):
            d1[s1[i]] += 1
            d2[s2[i]] += 1
        
        if d1 == d2:
            return True


        i, j = 0, len(s1)
        while j < len(s2):
            d2[s2[j]] = 1 + d2.get(s2[j], 0)
            d2[s2[i]] -= 1
            if d1 == d2:
                return True
            i, j = i + 1, j + 1
        return False