class Solution:
    def countGoodNumbers(self, n):
        MOD = 10 ** 9 + 7
        def power(x,n):
            if n == 0:
                return 1
            half = power(x, n // 2)
            if n % 2 == 0:
                return (half * half) % MOD
            return (x * half * half) % MOD
        even = (n + 1) // 2
        odd = n // 2
        return ( power(5, even) * power(4, odd)) % MOD