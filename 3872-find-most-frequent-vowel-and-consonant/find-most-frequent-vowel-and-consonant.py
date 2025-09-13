class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = set(s)
        v = 0
        c = 0
        
        for ch in n:
            if ch in "aeiou":
                v = max(v, s.count(ch))
            else:
                c = max(c, s.count(ch))
        return v+c