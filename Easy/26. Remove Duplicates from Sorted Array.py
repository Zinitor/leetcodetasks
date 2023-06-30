class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        flag_unq = 0
        for i in range(1,len(nums)):
            if nums[flag_unq] != nums[i]:
                flag_unq += 1
                nums[flag_unq] = nums[i]
        return flag_unq+1


a = Solution()
print(a.removeDuplicates(nums=[1, 1, 2]))
