class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pf = ""

        for i in range(len(strs[0])):
            for ch in strs:
                if i == len(ch) or ch[i] != strs[0][i]:
                    return pf
            pf += strs[0][i]
        return pf
