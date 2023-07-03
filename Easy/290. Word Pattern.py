# разбить строку на подстрочки
# занести подстрочки в словарь в соответствии с паттерном
# у каждой буквы должно быть уникальное слово
# если мы пытаемся переписать какую-либо подстроку то False
# иначе True
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat = s.split()
        # Если количество символов не совпадает
        if len(pattern) != len(pat):
            return False
        hash = {}
        for i in range(len(pattern)):
            if pattern[i] in hash:  # если ключ в хэше
                # Если зн. ключа в хэше не совпадает с строкой
                if hash[pattern[i]] != pat[i]:
                    return False
            else:
                # Если подстрочка уже есть в словаре
                if pat[i] in hash.values():
                    return False
                hash[pattern[i]] = pat[i]
        return True


a = Solution()
print(a.wordPattern(pattern="abba", s="dog dog dog dog"))
