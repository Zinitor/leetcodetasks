class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            lp, rp = i+1, len(nums)-1
            while lp < rp:
                threeSum = a + nums[lp] + nums[rp]
                if threeSum > 0:
                    rp -= 1
                elif threeSum < 0:
                    lp += 1
                else:
                    ans.append([a, nums[lp], nums[rp]])
                    lp += 1
                    while nums[lp] == nums[lp-1] and lp < rp:
                        lp += 1
        return ans


a = Solution()
print(a.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
