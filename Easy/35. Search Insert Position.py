class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            halfpoint = (l+r)//2
            if target > nums[halfpoint]:
                l = halfpoint+1
            elif target < nums[halfpoint]:
                r = halfpoint-1
            else:
                return halfpoint
        return l
        # for i in range(size):
        #     if target<nums[round()]:
        #         r//=2


a = Solution()
print(a.searchInsert(nums=[1,3,5,6], target=2))
