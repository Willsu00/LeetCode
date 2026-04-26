class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        r_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = 0

        for i in range(len(s)):
            if i+1 < len(s) and r_num[s[i]] < r_num[s[i+1]]:
                n -= r_num[s[i]]
            else:
                n += r_num[s[i]]
        return n

        