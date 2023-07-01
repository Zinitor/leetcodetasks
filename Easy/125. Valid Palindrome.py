class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s.lower():
            if i.isalnum():
                ans += i
        if ans == ans[::-1]:
            return 1
        return 0


a = Solution()
print(a.isPalindrome(s="{news}"))
