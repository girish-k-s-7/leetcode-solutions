class Solution:
    def findCombination(self, ind, target, arr, ans, ds):
        if target == 0:
            ans.append(list(ds))
            return

        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i-1]:
                continue

            if arr[i] > target:
                break

            ds.append(arr[i])

            self.findCombination(i+1, target - arr[i], arr, ans, ds)

            ds.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        ds = []
        self.findCombination(0, target, candidates, ans, ds)
        return ans