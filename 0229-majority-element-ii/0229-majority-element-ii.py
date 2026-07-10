class Solution:
    def majorityElement(self, nums):
        count1 = count2 = 0
        cand1 = cand2 = None

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        ans = []

        if nums.count(cand1) > len(nums) // 3:
            ans.append(cand1)

        if cand2 != cand1 and nums.count(cand2) > len(nums) // 3:
            ans.append(cand2)

        return ans