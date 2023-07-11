class Solution:
    def canJump(self, nums: list[int]) -> bool:
        index = 0
        while index != len(nums):
            power = nums[index]
            canJumpTo = nums[index:power+1]
            print (canJumpTo)
            target = nums.index(max(canJumpTo))
            index = target
            
        return True
        # i = nums[i:nums[i]]
        
a = Solution()
a.canJump(nums = [2,3,1,1,4])