from typing import List


class RangeSum:
    def __init__(self, nums: List[int]):
        N = len(nums)
        self.arr = [0] * N
        self.arr[0] = nums[0]
        for i in range(1, N):
            self.arr[i] = nums[i] + self.arr[i - 1]

    def take_sum(self, start: int, end: int) -> int:
        if start == 0:
            return self.arr[end]
        return self.arr[end] - self.arr[start - 1]


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:            
        rs = RangeSum(nums)
        N = len(nums)
        for size in range(2, N + 1):
            for start in range(N - size + 1):
                end = start + size - 1
                sub_sum = rs.take_sum(start, end)
                if k != 0 :
                    if sub_sum % k == 0:
                        return True
                else:
                    if sub_sum == 0:
                        return True
        return False


if __name__ == "__main__":
    k = int(input().strip())
    nums = list(map(int, input().split()))

    s = Solution()
    print(s.checkSubarraySum(nums, k))