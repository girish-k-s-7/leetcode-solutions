class Solution:
    def myPow(self, x, n):
        def power(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            half = power(x, n // 2)
            if n % 2 == 0:
                return half * half 
            return x * half * half
        if n < 0:
            return 1 / power(x, -n)
        return power(x,n)