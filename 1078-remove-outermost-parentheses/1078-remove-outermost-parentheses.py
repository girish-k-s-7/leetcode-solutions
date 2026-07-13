class Solution():
    def removeOuterParentheses(self, s):
        result = ""
        level = 0
        for cha in s:
            if cha == "(":
                if level > 0:
                    result += cha
                level += 1
            elif cha == ")":
                level -= 1
                if level > 0:
                    result += cha
        return result