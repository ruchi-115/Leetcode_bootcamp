class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        dp[0] = 1
        for i in range(0, n):
            for j in range(i - forget + 1, i-delay + 1):
                if j >= 0:
                    dp[i] += dp[j]

        return sum(dp[-1 - forget + 1:]) % (10**9 + 7)
        