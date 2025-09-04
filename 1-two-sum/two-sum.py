class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i, n in enumerate(nums):
            d = target - n
            if d in map:
                return [map[d], i]
            map[n] = i


        