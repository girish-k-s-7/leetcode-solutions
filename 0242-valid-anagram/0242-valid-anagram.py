# Valid Anagram
class Solution:
    def isAnagram(self,str1, str2):
        if  len(str1) != len(str2):
            return False
        freq = [0] * 26
        for cha in str1:
            freq[ord(cha) - ord('a')] += 1
        for cha in str2:
            freq[ord(cha) - ord('a')] -= 1
        for count in freq:
            if count != 0:
                return False
        return True