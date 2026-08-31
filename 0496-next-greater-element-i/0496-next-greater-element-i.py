class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        nge = {}

        for num in reversed(nums2):

            while stack and stack[-1] <= num:
                stack.pop()

            nge[num] = stack[-1] if stack else -1

            stack.append(num)

        return [nge[num] for num in nums1]