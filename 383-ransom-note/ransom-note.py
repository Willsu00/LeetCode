class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        d = {}

        for ch in magazine:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        
        for ch in ransomNote:
            if ch in d and d[ch] > 0:
                d[ch] -= 1
            else:
                return False
        
        return True
        