# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        x = 0
        char = 0
        while char < len(s):
            if s[char] == 'I':
                if (char+1 < len(s) and s[char+1] == 'V'):
                    x += 4
                    char += 2
                elif (char+1 < len(s) and s[char+1] == "X"):
                    x += 9
                    char += 2
                else:
                    x += 1
                    char += 1
            elif s[char] == 'X':
                if (char+1 < len(s) and s[char+1] == 'L'):
                    x += 40
                    char += 2
                elif (char+1 < len(s) and s[char+1] == "C"):
                    x += 90
                    char += 2
                else:
                    x += 10
                    char += 1
            elif s[char] == 'C':
                if (char+1 < len(s) and s[char+1] == 'D'):
                    x += 400
                    char += 2
                elif (char+1 < len(s) and s[char+1] == "M"):
                    x += 900
                    char += 2
                else:
                    x += 100
                    char += 1
            elif s[char] == 'V':
                char += 1
                x += 5
            elif s[char] == 'L':
                char += 1
                x += 50
            elif s[char] == 'D':
                char += 1
                x += 500
            elif s[char] == 'M':
                char += 1
                x += 1000
        return x


print(Solution.romanToInt('1984', "MDCCCLXXXIV"))
