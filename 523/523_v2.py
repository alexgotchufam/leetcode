from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        curr_total = 0
        compliment = {0}

        for i in range(N):
            if k != 0:
                curr_total += nums[i]
                remainder = curr_total % k

                if remainder in compliment:
                    return True

                compliment.add(remainder)
                
            elif nums[i] == 0:
                return True

        return False


if __name__ == "__main__":
    k = int(input().strip())
    nums = list(map(int, input().split()))

    s = Solution()
    print(s.checkSubarraySum(nums, k))