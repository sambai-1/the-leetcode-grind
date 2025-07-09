class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        
        carry = 1
        digits[-1] = 0
        for i in range(len(digits) - 2, -1, -1):
            tmp = digits[i]
            digits[i] = (digits[i] + carry) % 10
            carry = (tmp + carry) // 10
        if carry == 1:
            return [1] + digits[:]
        else:
            return digits