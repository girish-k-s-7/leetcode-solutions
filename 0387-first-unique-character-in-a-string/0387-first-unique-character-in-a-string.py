class Solution(object):
    def firstUniqChar(self, s):
        h = {}
        for  i in s:
            # if i in h.keys():
                #count = h[i]
                #count += 1
               # h[i] = count
            #else:
                #h[i] = 1
                h[i] = h.get(i,0)+1
        for i in range(len(s)):
            if h[s[i]] == 1:
                return i
        return -1
        