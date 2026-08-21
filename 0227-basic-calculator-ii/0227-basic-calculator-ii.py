class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        sign = "+"

        for i in range(len(s)):

            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:

                if sign == "+":
                    stack.append(num)

                elif sign == "-":
                    stack.append(-num)

                elif sign == "*":
                    stack.append(stack.pop() * num)

                elif sign == "/":
                    prev = stack.pop()

                    # truncate toward zero
                    if prev < 0:
                        stack.append(-(-prev // num))
                    else:
                        stack.append(prev // num)

                sign = s[i]
                num = 0

        return sum(stack)