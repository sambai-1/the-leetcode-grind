from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans = ans + str(len(i)) + "#" + i
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        count = 0
        i = 0
        currNum = ""
        currString = ""
        while i < len(s):
            if count == 0:
                if s[i] == "#":
                    count = int(currNum)
                    currNum = ""
                else:
                    currNum = currNum + s[i]
            else:
                currString = currString + s[i]
                count -= 1
            if count == 0 and currNum == "":
                ans.append(currString)
                currString = ""
            i += 1
        return ans