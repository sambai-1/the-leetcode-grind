class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        def check(curr):
            curr = curr.lower()
            return ord('0') <= ord(curr) <= ord('9') or ord('a') <= ord(curr) <= ord('z')

        while i < j:
            left = s[i]
            right = s[j]
            if check(left) and check(right):
                if left.lower() != right.lower():
                    return False
                i += 1
                j -= 1
            if not check(left):
                i += 1
            if not check(right):
                j -= 1
        


        
        return True
