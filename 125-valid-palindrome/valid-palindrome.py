class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        nStr = ""
        for i in s:
            if i.isalnum():
                nStr += i.lower()
        return nStr == nStr[::-1]
        