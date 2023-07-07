class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lp, rp = 0, 0
        current_profit = prices[rp]-prices[lp]
        max_profit = 0
        for i in range(len(prices)):
            # Если цены от текущего дня дают больший профит
            if prices[i]-prices[lp] > current_profit:
                rp = i  # смещаем указатель
                # пересчитываем текущий профит
                current_profit = prices[rp]-prices[lp]
            # Если тек. цены хуже чем цены от правого указателя, значит мы нашли локальный максимум
            elif prices[i] < prices[rp]:
                max_profit += current_profit  # увеличиваем макс профит
                current_profit = 0  # обнуляем тек. профит
                lp, rp = i, i  # смещаем указатели
            # Если цены от тек. дня меньше цен от левого указателя    
            if prices[i] < prices[lp]:
                lp, rp = i, i #смещаем указатели
                current_profit = 0

        max_profit += current_profit
        return max_profit


a = Solution()
print(a.maxProfit(prices=[7, 1, 4, 3, 2, 1]))
