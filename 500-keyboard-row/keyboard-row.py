class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")
        res = []

        for i in words:
            word = i.lower()
            ch = set(word)
            if ch.issubset(r1) or ch.issubset(r2) or ch.issubset(r3):
                res.append(i)
        return res