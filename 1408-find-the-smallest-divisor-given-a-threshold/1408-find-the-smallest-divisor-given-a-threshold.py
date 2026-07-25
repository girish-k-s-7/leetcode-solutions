# FInd the smallest divisor
class Solution:
    def smallestDivisor(self, nums, threshold):
        def findSum(divisor):
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
            return total
        low = 1
        high = max(nums)
        ans = high
        while low <= high:
            mid = (low+high) // 2
            total = findSum(mid)
            if total <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans