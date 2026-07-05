class Solution(object):
    def singleNumber(self, nums):
        xorr = 0
        for num in nums:
            xorr ^= num
        return xorr
        