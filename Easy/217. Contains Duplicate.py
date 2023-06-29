class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict = set(nums)
        if len(dict) < len(nums):  # Если в словаре меньше значений
            return True
        return False


a = Solution()
print(a.containsDuplicate([1, 2, 3, 4]))
