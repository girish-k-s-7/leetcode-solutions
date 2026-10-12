
class Solution:
    def canConstruct(self, ransomNote, magazine):
        h = {}

        # Count characters in magazine
        for ch in magazine:
            h[ch] = h.get(ch, 0) + 1

        # Check characters required by ransomNote
        for ch in ransomNote:
            if ch not in h or h[ch] == 0:
                return False

            h[ch] -= 1

        return True


obj = Solution()
print(obj.canConstruct("aa", "aab"))  # True
print(obj.canConstruct("aa", "ab"))   # False
