class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(n):
            if n % 3 == 0 and n % 5 == 0:
                answer.append("FizzBuzz")
            elif n % 5 == 0:
                answer.append("Buzz")
            elif n % 3 == 0:
                answer.append("Fizz")
            else:
                answer.append(n)
        return answer


print(Solution.fizzBuzz("fizz", 3))
