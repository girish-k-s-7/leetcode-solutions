class Solution:
    def maxDepth(self, s):
        depth = 0
        max_depth = 0
        for ch in s:
            if ch == '(':
                depth += 1
                
            elif ch == ')':
                depth -= 1
            max_depth = max(max_depth, depth)
        return max_depth