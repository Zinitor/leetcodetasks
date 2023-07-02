class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums+nums

a = Solution()
print(a.getConcatenation(nums = [1,2,1]))