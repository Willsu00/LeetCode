class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        a = sorted(s)
        b = sorted(t)

        for i in range(len(s)):
            if a[i] != b[i]:
                return b[i]
        return b[-1]