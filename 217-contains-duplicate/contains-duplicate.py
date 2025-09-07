class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Set = set()
        for i in nums:
            if i in Set:
                return True
            Set.add(i)
        return False

        