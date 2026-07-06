class Solution():
    def majorityElement(self, nums):
        n = len(nums)
        count = 0
        element = 0
        for num in nums:
            if count == 0:
                count = 1
                element = num
            elif element == num:
                count += 1
            else:
                count -= 1

        count1 = nums.count(element)
        if count1 > (n // 2):
            return element
        retun -1