class Solution:
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.dp = None

    def numTilings(self, N: int, remain: int = 0) -> int:
        if self.dp is None:
            self.dp = [[None] * 2 for _ in range(N + 1)]

        if self.dp[N][remain] is not None:
            return self.dp[N][remain]

        total = 0

        if N == 1:
            total = 1
        elif N == 2:
            total = 2
        elif remain == 0:
            total += (
                self.numTilings(N - 1, 0)
                + self.numTilings(N - 2, 0)
                + 2 * self.numTilings(N - 2, 1)
            )
        else:
            total += self.numTilings(N - 1, 0) + self.numTilings(N - 1, 1)

        total %= Solution.MOD
        self.dp[N][remain] = total
        return total


if __name__ == "__main__":
    for i in range(1, 6):
        solution = Solution()
        print(i, solution.numTilings(i))
