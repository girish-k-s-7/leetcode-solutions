class Solution:
    def permute(self, nums):
        ans = []
        used = [False] * len(nums)

        def generate(ds):
            if len(ds) == len(nums):
                ans.append(list(ds))
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                ds.append(nums[i])
                generate(ds)
                ds.pop()
                used[i] = False
        generate([])
        return ans