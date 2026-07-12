class Solution():
    def minSubArrayLen(self,target,nums):
        left = 0
        current_sum = 0
        answer = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                answer = min(answer, right - left + 1)
                current_sum -= nums[left]
                left += 1
        if answer == float('inf'):
            return 0
        return answer