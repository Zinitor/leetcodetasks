class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return (len(s.split()[-1]))


a = Solution()
a.lengthOfLastWord(s="Hello World")
