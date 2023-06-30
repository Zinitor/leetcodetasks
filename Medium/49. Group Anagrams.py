from collections import defaultdict

# O (M*N), где M - количество строк, N-среднее к-во символов в строке


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = defaultdict(list)

        for string in strs:  # Для каждой строки
            count = [0] * 26  # Создание массива для a-z
            for char in string:  # Для каждого символа в строке
                # Найти ASCII значение символа,
                # а затем в массиве сосчитать количество его вхождений,
                # это и будет ключ
                count[ord(char)-ord("a")] += 1
            # Добавить ключ (массив посчитаных букв) к ответу.
            dict[tuple(count)].append(string)
        return (dict.values())


a = Solution()
print(a.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
