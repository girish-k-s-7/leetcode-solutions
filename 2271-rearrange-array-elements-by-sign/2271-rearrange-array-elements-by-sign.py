class Solution():
    def rearrangeArray(self, nums):
        n = len(nums)
        ans = [0] * n
        pos_index = 0
        neg_index = 1
        for i in range(n):
            if nums[i] < 0:
                ans[neg_index] = nums[i]
                neg_index += 2
            else:
                ans[pos_index] = nums[i]
                pos_index += 2
        return ans