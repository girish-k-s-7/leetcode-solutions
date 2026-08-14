class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        ds = []
        def generate(ind):
            ans.append(list(ds))
            for i in range(ind, len(nums)):
                
                if i > ind and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                generate(i+1)
                ds.pop()
        generate(0)
        return ans