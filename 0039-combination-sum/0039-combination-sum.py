class Solution:
    def findCombination(self, ind, target, arr, ans, ds):

        if ind == len(arr):
            if target == 0:
                ans.append(list(ds))
            return 

        if arr[ind] <= target:
            ds.append(arr[ind])
            self.findCombination(ind, target - arr[ind], arr, ans, ds)
            ds.pop()

        self.findCombination(ind+1, target, arr, ans, ds)
    def combinationSum(self, candidates, target):
        ans = []
        ds = []
        self.findCombination(0, target, candidates, ans, ds)
        return ans