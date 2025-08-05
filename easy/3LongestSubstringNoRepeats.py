class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        inside = set()
        length = 0
        i, j = 0, 0
        while j < len(s):
            curr = s[j]
            if curr in inside:
                while i < j:
                    inside.remove(s[i])
                    i += 1
                    if s[i-1] == curr:
                        break
                inside.add(curr)
                
                j += 1

            else:
                j += 1  
                inside.add(curr)
                length = max(length, j - i)

        return length