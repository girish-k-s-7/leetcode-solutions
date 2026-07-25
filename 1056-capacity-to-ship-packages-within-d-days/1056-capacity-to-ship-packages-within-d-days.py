# Capacity to ship [ackages within D Days
class Solution:
    def daysNeeded(self, weights, capacity):
        days = 1
        currentLoad = 0
        for w in weights:
            if currentLoad + w > capacity:
                days += 1
                currentLoad = w
            else:
                currentLoad += w
        return days

    def shipWithinDays(self, weights, d):
        low = max(weights)
        high = sum(weights)
        while low< high:
            mid = (low + high) // 2
            needed = self.daysNeeded(weights, mid)
            if needed <= d:
                high = mid
            else:
                low = mid + 1
        return low
