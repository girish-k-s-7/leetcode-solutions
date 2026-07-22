class Solution:
    def searchRange(self, nums, target):

        def firstOccurrence():
            low = 0
            high = len(nums) - 1
            ans = -1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    ans = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        def lastOccurrence():
            low = 0
            high = len(nums) - 1
            ans = -1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    ans = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        return [firstOccurrence(), lastOccurrence()]