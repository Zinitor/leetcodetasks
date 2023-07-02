
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        sol = [1]*length
        pre = 1
        post = 1
        for i in range(length):
            # Т.к. в умножении порядок не важен
            # Умножаем число на произведение пред. чисел до него
            sol[i] *= pre
            # Перемножаем числа слева направо в отдельную переменную до текущего
            pre = pre*nums[i]
            # Умножаем число на произв. чисел после него
            sol[length-i-1] *= post
            # Перемножаем числа справа налево в отдельную переменную до текущего
            post = post*nums[length-i-1]
            print(sol)
        return (sol)


a = Solution()
print(a.productExceptSelf(nums=[1, 2, 3, 4, 1]))
