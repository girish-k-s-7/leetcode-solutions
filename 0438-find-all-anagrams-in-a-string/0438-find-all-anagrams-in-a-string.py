class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window = [0] * 26

        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            window[ord(s[i]) - ord('a')] += 1

        result = []

        if p_count == window:
            result.append(0)

        left = 0
        for right in range(len(p), len(s)):
            window[ord(s[right]) - ord('a')] += 1
            window[ord(s[left]) - ord('a')] -= 1
            left += 1

            if p_count == window:
                result.append(left)

        return result