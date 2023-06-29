class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i] #Ставим числа в конец списка вместо 0 и затем сортируем
        nums1.sort()


a = Solution()
print(a.merge(nums1=[0], m=0, nums2=[1], n=1))
