class Solution:
    def minDays(self, bloomDay, m, k):

        if m * k > len(bloomDay):
            return -1

        def countBouquets(day):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets

        low = min(bloomDay)
        high = max(bloomDay)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            bouquets = countBouquets(mid)

            if bouquets >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans