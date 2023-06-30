from itertools import permutations


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(permutations(nums))

a = Solution()
print(a.permute(nums = [1,2,3]))
