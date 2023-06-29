class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            if num % 2 == 0:
                return 1 + self.numberOfSteps(num/2)
            else:
                return 1 + self.numberOfSteps(num-1)


b = Solution()
print(b.numberOfSteps(14))
