class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        current_max = 0
        end_max = 0
        for i in range(0, len(accounts)):
            for j in range(0, len(accounts[i])):
                current_max += accounts[i][j]
            if current_max > end_max:
                end_max = current_max
            current_max = 0
        return end_max


a = Solution()
print(a.maximumWealth([[1, 2, 3], [3, 2, 1]]))
