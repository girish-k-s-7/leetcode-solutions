class Solution:
    def subsets(self, nums):
        ans = []
        ds = []
        def generate(ind):
            if ind == len(nums):
                ans.append(list(ds))
                return
            ds.append(nums[ind])
            generate(ind+1)
            ds.pop()
            generate(ind+1)
        generate(0)
        return ans