class Solution:
    def minEatingSpeed(self, piles, h):

        def findHours(speed):
            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            return hours

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            hours = findHours(mid)

            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans