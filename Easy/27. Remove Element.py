class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
        
a = Solution()
print(a.removeElement(nums = [3,2,2,3], val = 3))