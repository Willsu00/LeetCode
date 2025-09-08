class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # if len(t) != len(s):
        #     return False
        

        # return sorted(t) == sorted(s)

        return Counter(s) == Counter(t)
        