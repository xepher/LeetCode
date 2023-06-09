# https://leetcode.com/problems/roman-to-integer/

# Symbol       Value
# I             1
# IV            4
# V             5
# IX            9
# X             10
# XL            40
# L             50
# XC            90
# C             100
# CD            400
# D             500
# CM            900
# M             1000

# 时间复杂度O(n), 空间复杂度O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        first = ""
        result = 0
        for c in s:
            # I
            if c == "I":
                if first != "":
                    result = result + romanDict[first]
                first = c
            # V, L, D, M
            elif c == "V":
                if first == "I":
                    result = result + romanDict[first + c]
                    first = ""
                elif first != "":
                    result = result + romanDict[first]
                    first = c
                else:
                    result = result + romanDict[c]
                    first = ""
            elif c == "L":
                if first == "X":
                    result = result + romanDict[first + c]
                    first = ""
                elif first != "":
                    result = result + romanDict[first]
                    first = c
                else:
                    result = result + romanDict[c]
                    first = ""
            elif c == "D" or c == "M":
                if first == "C":
                    result = result + romanDict[first + c]
                    first = ""
                elif first != "":
                    result = result + romanDict[first]
                    first = c
                else:
                    result = result + romanDict[c]
                    first = ""
            # X, C
            elif c == "X":
                if first == "I":
                    result = result + romanDict[first + c]
                    first = ""
                elif first != "":
                    result = result + romanDict[first]
                    first = c
                else:
                    first = c
            elif c == "C":
                if first == "X":
                    result = result + romanDict[first + c]
                    first = ""
                elif first != "":
                    result = result + romanDict[first]
                    first = c
                else:
                    first = c

        if first != "":
            result = result + romanDict[first]

        return result


if __name__ == "__main__":
    print(Solution().romanToInt("III"))  # 3
    print(Solution().romanToInt("LVIII"))  # 58
    print(Solution().romanToInt("MCMXCIV"))  # 1994
    print(Solution().romanToInt("DCXXI"))  # 621
    print(Solution().romanToInt("MDCCCLXXXIV"))  # 1884
