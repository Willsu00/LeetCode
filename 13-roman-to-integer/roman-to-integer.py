class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        r_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = 0

        for i in range(len(s)):
            # check to make sure it isn't going out of bounds and compare i to i+1 in string s
            # values should go from largest to smallest so M -> D -> C -> ... -> I
            if i+1 < len(s) and r_num[s[i]] < r_num[s[i+1]]:
                # if value i is less than i+1, subtract i from n
                n -= r_num[s[i]]
            else:
                n += r_num[s[i]]
        return n

        