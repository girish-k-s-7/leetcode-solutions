class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # skip spaces
        while i < n and s[i] == " ":
            i += 1

        # sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # nnumber formation
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1
        num *= sign

        # overflow handling
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN

        return num