class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        dp = [False] * len(candies)
        maxCandies = max(candies)
        for j, i in enumerate(candies):
            if (i + extraCandies) >= maxCandies:
                dp[j] = True
        return dp

