# Нужно найти самый длинный префикс среди ВСЕХ строк
# В данном случае наиболее ЧАСТЫЙ префик - pre
# Но т.к. данный префикс не у ВСЕХ строк то вывод будет пустым

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref = ""
        str_list = sorted(strs)
        first = str_list[0]
        last = str_list[-1]
        for str in range(min(len(first), len(last))):
            if first[str] != last[str]:
                return pref
            pref += first[str]
        return pref


a = Solution()
print(a.longestCommonPrefix(strs=["preheat", "oven", "prehistoric"]))
