class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lp, rp = 0, 1
        max_profit = 0
        for rp in range(rp,len(prices)):
            if prices[lp] < prices[rp]:
                profit = prices[rp] - prices[lp]
                max_profit = max(max_profit,profit)
            else:
                lp = rp
            print (lp,rp)
        return max_profit


a = Solution()
print(a.maxProfit(prices=[1, 7, 6, 4, 3, 1]))
