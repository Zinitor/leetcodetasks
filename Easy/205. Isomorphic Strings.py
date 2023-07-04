class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        substr = ''
        for i in range(len(s)):
            if s[i] not in dict and t[i] not in dict.values():
                dict[s[i]] = t[i]
        for i in range(len(s)):
            if s[i] in dict.keys():
                substr += dict[s[i]]
        return substr == t


a = Solution()
print(a.isIsomorphic(s="cobo", t="baba"))
