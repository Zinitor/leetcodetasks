class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            print(stack)
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False



a = Solution()
print(a.isValid("([{[()]}])"))
