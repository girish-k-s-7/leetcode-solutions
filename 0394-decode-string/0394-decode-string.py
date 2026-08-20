class Solution:
    def decodeString(self, s):
        stack = []
        currstr = ""
        currnum = 0

        for ch in s:
            if ch.isdigit():
                currnum = currnum * 10 + int(ch)
            elif ch == '[':
                stack.append((currstr, currnum))
                currstr = ""
                currnum = 0
            elif ch == ']':
                prevstr, num = stack.pop()
                currstr = prevstr + currstr * num
            else:
                currstr += ch
        return currstr