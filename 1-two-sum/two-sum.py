class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n) Solution

        map = {}

        for i, n in enumerate(nums):
            d = target - n
            if d in map:
                return [map[d], i]
            map[n] = i

        # O(n^2) initial solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         x = nums[i] + nums[j]
        #         if x == target:
        #             return i, j


        