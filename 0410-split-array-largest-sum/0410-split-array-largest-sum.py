# Split the array - largest Sum
class Solution:
    def count_partitions(self, a, max_sum):
        partitions = 1
        subarray_sum = 0

        for num in a:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        return partitions

    def splitArray(self, a, k):
        low = max(a)
        high = sum(a)
        while low <= high:
            mid = (low + high) // 2
            partitions = self.count_partitions(a, mid)
            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low