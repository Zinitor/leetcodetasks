class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict = {}
        n = len(nums)//2
        for i in nums:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1
            if dict[i] > (n):
                return i


a = Solution()
print(a.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
