class Solution:

    def permuteUnique(self, nums):

        nums.sort()

        ans = []
        used = [False] * len(nums)

        def generate(ds):

            if len(ds) == len(nums):
                ans.append(list(ds))
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                ds.append(nums[i])

                generate(ds)

                ds.pop()
                used[i] = False

        generate([])

        return ans