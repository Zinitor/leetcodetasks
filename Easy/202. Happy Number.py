class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # set чтобы знать какие числа мы прошли
        # как только мы находим уже пройденное число значит мы в цикле и должны вывести false

        while n != 1:  # Находимся в цикле пока не Happy или не поймем что в беск. цикле
            sum_of_squares = 0  # обнуляем сумму

            while n > 0:
                digit = n % 10  # Берем последнюю цифру числа
                # Квадрат цифры прибавляем к сумме
                sum_of_squares += digit ** 2
                n //= 10  # убираем последнюю цифру

            # Проверяем если уже была такая сумма
            if sum_of_squares in visited:
                return False  # Если да то мы в беск. цикле

            # Добавляем сумму в set посещенных сумм
            visited.add(sum_of_squares)

            # Устанавливаем n как сумму для следующей итерации
            n = sum_of_squares

        return True


a = Solution()
a.isHappy(19)
