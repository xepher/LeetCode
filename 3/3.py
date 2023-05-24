# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# string comparison


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        parameters = []
        parameters.append(0)    # start
        parameters.append(0)    # end
        curent_lenth = 0        # curent_lenth
        max_length = 0

        while(parameters[1] != len(s)):
            curent_lenth = self.getLengthOfSubstring(s, parameters)
            if(curent_lenth > max_length):
                max_length = curent_lenth
            parameters[0] += 1

        return max_length

    def getLengthOfSubstring(self, s: str, parameters: []) -> int:
        if(parameters[0] == parameters[1]):
            parameters[1] += 1
        while(parameters[1] < len(s) and s[parameters[1]] != s[parameters[0]]):
            start = parameters[0]
            while(s[start] != s[parameters[1]]):
                start += 1
            if(start != parameters[1]):
                break
            else:
                parameters[1] += 1
        return parameters[1] - parameters[0]


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
