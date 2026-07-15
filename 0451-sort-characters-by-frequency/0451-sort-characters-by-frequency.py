from collections import Counter

class Solution:
    def frequencySort(self, s):
        freq = Counter(s)

        result = ""

        for ch, count in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
            result += ch * count

        return result