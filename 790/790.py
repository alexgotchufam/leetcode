class Solution:
    MOD = 10 ** 9 + 7
    def __init__(self):
        self.dp = []

    def numTilings(self, N: int) -> int:
        if N == 0:
            return 1
        elif N < 3:
            return N

        if len(self.dp) < N:
            self.dp = [None] * (N + 1)
            self.dp[0] = 1

        total = 0
        for i in range(1, 4):
            n_i = self.dp[N - i]
            if n_i is None:
                n_i = self.numTilings(N - i)
                self.dp[N - i] = n_i
            total += n_i % Solution.MOD

        return 1 + total


if __name__ == "__main__":
    solution = Solution()
    for i in range(1, 100):
        print(solution.numTilings(i))
