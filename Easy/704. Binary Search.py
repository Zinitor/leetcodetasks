# Если цель больше центра сместить левую границу до центра, найти новый центр
# Если цель меньше центра сместить правую границу до центра, найти новый центр


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            print(l, r)
            halfpoint = (l+r)//2
            if target == nums[halfpoint]:
                return halfpoint
            if target > nums[halfpoint]:
                l = halfpoint+1
            if target < nums[halfpoint]:
                r = halfpoint-1
        # Если точки не существует то рано или поздно 
        # l > r == 1
        return -1


a = Solution()
print(a.search(nums=[-1, 0, 3, 5, 9, 12], target=-2))
