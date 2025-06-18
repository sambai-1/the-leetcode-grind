class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "0":
            return 0
        
        letters = set()
        for i in range(1, 27):
            letters.add(str(i))
        
        curr = 1 if s[-1] != "0" else 0
        prev = 1
        tmp = 0
        for i in range(len(s) - 2, -1, -1):
            single = s[i]
            double = s[i:i + 2]
            print(single, double)
            if single in letters:
                tmp += curr
            if double in letters:
                tmp += prev
            prev = curr
            curr = tmp
            tmp = 0
        return curr