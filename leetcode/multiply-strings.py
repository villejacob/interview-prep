'''
Given two non-negative integers num1 and num2 represented as strings, return the
product of num1 and num2.

Note: 
    The length of both num1 and num2 is < 110.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to
    integer directly.

'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if "0" in (num1, num2): return "0"

        sums = [0 for v in xrange(len(num1) + len(num2))]
        for i, s1 in enumerate(reversed(num1)):
            carry = 0
            for j, s2 in enumerate(reversed(num2)):
                n1, n2 = int(s1), int(s2)
                sum = n1*n2 + sums[i+j] + carry
                carry, sums[i+j] = divmod(sum, 10)
            if carry > 0:
                sums[i + len(num2)] += carry
        nonzero = len(sums)-1
        while(sums[nonzero] == 0): nonzero -= 1
        if nonzero < 0: return "0"
        return ''.join(map(str, reversed(sums[:nonzero+1])))




print Solution().multiply("93324520229641357693055447943264",
        "19381505489727486")
