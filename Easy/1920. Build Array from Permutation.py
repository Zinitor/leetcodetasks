class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]
a = Solution()
print(a.buildArray (nums = [5,0,1,2,3,4]))