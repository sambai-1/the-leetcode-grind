class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 10 ** 5 + 1
        has = contain = 0
        ansl = ansr = 0
        target = {}
        for i in t:
            target[i] = 1 + target.get(i, 0)
        has = len(set(t))
        
        curr = {}
        i = j = 0
        while j < len(s):
            if s[j] in target:
                curr[s[j]] = 1 + curr.get(s[j], 0)
                if curr[s[j]] == target[s[j]]:
                    contain += 1
            while has == contain:
                if j - i < ans:
                    ans = j - i
                    ansl = i
                    ansr = j
                remove = s[i]
                if remove in curr:
                    curr[remove] -= 1
                    if curr[remove] < target[remove]:
                        contain -= 1
                i += 1
            j += 1
        
        if ans == 10 ** 5 + 1:
            return ""
        else:
            return s[ansl : ansr + 1]