# https://leetcode.com/problems/integer-to-roman/

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

import math


class Solution:
    def intToRoman(self, num: int) -> str:
        romanDict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        result = ""

        for i in range(0, 13):
            popd = romanDict.popitem()
            times = math.floor(num / popd[0])
            for j in range(0, times):
                result = result + popd[1]
            num = num - times * popd[0]

        return result


if __name__ == "__main__":
    print(Solution().intToRoman(3))  # III
    print(Solution().intToRoman(58))  # LVIII
    print(Solution().intToRoman(1994))  # MCMXCIV
