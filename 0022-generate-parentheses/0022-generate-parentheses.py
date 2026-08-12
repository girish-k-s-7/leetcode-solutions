class Solution:
    def generateParenthesis(self, n):
        result = []
        def generate(curr, openn, close):
            if len(curr) == 2 * n:
                result.append(curr)

            if openn < n:
                generate(curr + "(", openn + 1, close)
    
            if close < openn:
                generate(curr + ")", openn, close + 1)

        generate("", 0, 0)
        return result