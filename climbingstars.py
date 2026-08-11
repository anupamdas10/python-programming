class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n + 1)

        def func(n):
            if n <= 2:
                return n

            if dp[n] != -1:
                return dp[n]

            dp[n] = func(n - 1) + func(n - 2)

            return dp[n]

        return func(n)
y=Solution()
r=y.climbStairs(2)
print(r)    