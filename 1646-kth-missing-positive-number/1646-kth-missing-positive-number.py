class Solution:
    def findKthPositive(self, nums, k):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            missing = nums[mid] - (mid + 1)
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return k + high + 1