# search insert position
class Solution:
    def searchInsert(self, arr, target):
        low, high = 0, len(arr)-1
        ans = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
