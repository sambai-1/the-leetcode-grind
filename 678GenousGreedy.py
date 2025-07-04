class Solution:
    def checkValidString(self, s: str) -> bool:
        ansL = ansR = 0
        for i in s:
            if i == ")":
                ansL -= 1
                ansR -= 1
            if i == "(":
                ansL += 1
                ansR += 1
            if i == "*":
                ansL -= 1
                ansR += 1
            if ansL < 0:
                ansL = 0
            if ansR < 0:
                return False
        
        return ansL <= 0 and ansR >= 0