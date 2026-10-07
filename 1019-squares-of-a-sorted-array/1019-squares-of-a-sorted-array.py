class Solution:
    def sortedSquares(self, nums):
        n = len(nums)

        result = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:

            if nums[left] ** 2 > nums[right] ** 2:
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1

            pos -= 1

        return result