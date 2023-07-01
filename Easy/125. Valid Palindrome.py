class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s.lower():
            if i.isalnum():
                ans += i
        return ans == ans[::-1]


a = Solution()
print(a.isPalindrome(s="{news}"))
