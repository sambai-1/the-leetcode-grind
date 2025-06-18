class Solution:
    def longestPalindrome(self, s: str) -> str:
        palendromes = [[0] * len(s) for _ in range(len(s))]
        ans = ""
        for i in range(len(s)):
            palendromes[i][i] = 1
            ans = s[i]
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                palendromes[i][i + 1] = 1
                ans = s[i:i + 2]

        for i in range(2, len(s)):
            for j in range(len(s) - i):
                l = j
                r = j + i
                print(l, r)
                if s[l] == s[r] and palendromes[l + 1][r - 1] == 1:
                    if (r - l) > len(ans) - 1:
                        ans = s[l:r + 1]
                    palendromes[l][r] = 1
                else:
                    palendromes[l][r] = 0
        
        return ans
