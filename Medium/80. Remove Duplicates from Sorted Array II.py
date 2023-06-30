# Начинаем со 2го элемента т.к 0 и 1 эл. не важны из условия
# f - указатель на 2й э

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        f = 2  # Начинаем со 2го эл. т.к 0 и 1 элемент - фиксированые и не важны
        for i in range(2, len(nums)):
            if nums[i] != nums[f-2]:  # если текущий элемент неравен f-2 элем
                nums[f] = nums[i] # Заменяем элемент f текущим элементом
                f += 1
        return f


a = Solution()
print(a.removeDuplicates(nums=[1,1,1,2,2,3]))
