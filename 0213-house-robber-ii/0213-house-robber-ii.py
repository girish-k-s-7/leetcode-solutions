class Solution:

    def helper(self, nums):

        prev2 = 0
        prev1 = 0

        for num in nums:

            pick = num + prev2

            notPick = prev1

            curr = max(pick, notPick)

            prev2 = prev1
            prev1 = curr

        return prev1

    def rob(self, nums):

        n = len(nums)

        if n == 1:
            return nums[0]

        case1 = self.helper(nums[:-1])

        case2 = self.helper(nums[1:])

        return max(case1, case2)