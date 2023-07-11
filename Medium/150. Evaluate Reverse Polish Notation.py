class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        val1 = 0
        for i in tokens:
            if i.isnumeric() or (i.startswith('-') and i[1:].isnumeric()):
                stack.append(int(i))
            else:
                match i:
                    case '*':
                        val1 = stack.pop()
                        val1 *= stack.pop()
                        stack.append(val1)
                    case '/':
                        val1 = stack.pop()
                        val1 = int(stack.pop() / val1)
                        stack.append(val1)
                    case '+':
                        val1 = stack.pop()
                        val1 += stack.pop()
                        stack.append(val1)
                    case '-':
                        val1 = stack.pop()
                        val1 = stack.pop() - val1
                        stack.append(val1)
        return stack.pop()


a = Solution()
print(a.evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
