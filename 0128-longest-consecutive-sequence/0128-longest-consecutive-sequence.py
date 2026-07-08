class Solution():
    def longestConsecutive(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        longest = 1
        st = set()
        for i in range(n):
            st.add(nums[i])
        for it in st:
            if it-1 not in st:
                count = 1
                x = it

                while x+1 in st:
                    x = x+1
                    count = count+1
                longest = max(longest, count)
        return longest