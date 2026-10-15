class Solution:
    def canPlaceFlowers(self,nums, n):
        for i in range(len(nums)):
            if nums[i]==0:
                left = (i==0 or nums[i-1]==0)
                right = (i==len(nums)-1 or nums[i+1]==0)

                if left and right:
                    nums[i] = 1
                    n-=1

                    if n==0:
                        return True
        return n<=0