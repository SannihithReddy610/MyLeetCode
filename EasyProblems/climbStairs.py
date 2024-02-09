#Top Down approach which involves recurssion and uses memoization to avoid repeated calculation
class Solution:
    def solve(self, n, dp):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.solve(n-1, dp) + self.solve(n-2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.solve(n, dp)


# #Bootom up approach which starts with base case uses tabulization
# class Solution:
#     def solve(self, i, n, dp):
#         if i == n:
#             return 1
#         if i > n:
#             return 0
#         if dp[i] != -1:
#             return dp[i]
#         dp[i] = self.solve(i + 1, n, dp) + self.solve(i + 2, n, dp)
#         return dp[i]
#
#     def climbStairs(self, n: int) -> int:
#         dp = [-1] * (n + 1)
#         return self.solve(0, n, dp)