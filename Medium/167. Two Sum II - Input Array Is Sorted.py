class Solution:
    def twoSum(self, numbers: list[int],target: int) -> list[int]:
        lp,rp = 0, len(numbers)-1
        while numbers[lp]+numbers[rp] !=target:
            #Если сумма больше необходимой то смещаем правый указатель
            if numbers[lp]+numbers[rp] > target: 
                rp-=1
            #Если сумма меньше необходимой то смещаем левый указатель
            elif numbers[lp]+numbers[rp] < target:
                lp+=1
            else:
            #Если ни тот ни другой случай значит мы нашли сумму
                return [lp+1,rp+1]
        #Если while не выполнился значит необходимые индексы находятся по краям и мы уже нашли сумму
        return [lp+1,rp+1]

a = Solution()
print(a.twoSum(numbers = [-1,0,1], target = -1))            