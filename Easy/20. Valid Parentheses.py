class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif (i == ")" and stack[0] == "("):
                stack.pop(0)
            elif (i == "}" and stack[0] == "{") :
                stack.pop(0)
            elif (i == "]" and stack[0] == "["):
                stack.pop(0)
            print(stack)  
            # or i == "}" or i == "]":
            #     stack.append(i)
        
        # while stack[0] == stack[-1]:
        #     stack.pop(0)
        #     stack.pop()
        #     if stack:
        #         return True
        # return False
        print(stack)


a = Solution()
print(a.isValid("([])"))
