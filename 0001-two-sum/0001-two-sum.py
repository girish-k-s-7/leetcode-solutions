class Solution(object):
    def twoSum(self, nums, target):
        h = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in h:
                return (h[compliment], i)
            h[nums[i]] = i      