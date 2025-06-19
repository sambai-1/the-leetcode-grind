class Solution:
    def countSubstrings(self, s: str) -> int:
        palendromes = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            palendromes[i][i] = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                palendromes[i][i + 1] = 1

        for i in range(2, len(s)):
            for j in range(len(s) - i):
                l = j
                r = j + i
                print(l, r)
                if s[l] == s[r] and palendromes[l + 1][r - 1] == 1:
                    palendromes[l][r] = 1
        
        ans = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if palendromes[i][j] == 1:
                    ans += 1
        
        return ans
