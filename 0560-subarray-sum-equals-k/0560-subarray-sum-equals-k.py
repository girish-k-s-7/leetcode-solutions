class Solution:
    def  subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        h = {0:1}
        for num in nums:
            prefix_sum += num
            needed = prefix_sum - k
            if needed in h:
                count+=h[needed]
            h[prefix_sum] = h.get(prefix_sum, 0)+1
        return count