class Solution:
    def countSubstrings(self, s):
        count=0
        def expand(left, right):
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        ans = 0

        for i in range(len(s)):
                #for odd length
                ans += expand(i, i)
                # for even length
                ans += expand(i, i+1)
        return ans