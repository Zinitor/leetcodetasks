class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        x = str(x)
        for i in range(len(x)):
            if(x[i] != x1[len(x)-i-1]):
                return 0
        return 1