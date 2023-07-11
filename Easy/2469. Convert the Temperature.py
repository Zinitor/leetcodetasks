class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, round(celsius * 1.8 + 32.00, 5)]
    
a = Solution()
a.convertTemperature(celsius = 122.11)