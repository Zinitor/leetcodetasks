class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = {}
        for a in nums:
            if a not in hash:
                hash[a] = 0
            hash[a] += 1
        f_order = dict(sorted(hash.items(), key=lambda x: x[1])) #Сортировка по возрастанию значений

        return list(f_order.keys())[-k:] #возвращение k ключей с конца


a = Solution()
print(a.topKFrequent([1, 1, 1, 2, 2, 3], k=2))
