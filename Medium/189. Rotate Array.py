class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()  # Переворачиваем массив
        # Переворачиваем первые k чисел
        nums[:k] = reversed(nums[:k])
        # Переворачиваем оставшиеся числа
        nums[k:] = reversed(nums[k:])


a = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
a.rotate(nums, k=3)
