class Solution:
    def q3_lengthOfLongestSubstring(self, s: str) -> int:
        win_length = 1
        cursor = 0
        max_len = 0
        max_substr = ''
        str_len = len(s)

        while (cursor + win_length <= str_len):
            if (self.is_uniq_str(s[cursor:cursor+win_length])):
                max_len = max(max_len, len(s[cursor:cursor+win_length]))
                # max_substr = s[cursor:cursor+win_length]
                win_length += 1
            else:
                cursor += 1

        return max_len

    def is_uniq_str(self, s):
        uniq_c_set = set(c for c in s)
        if len(uniq_c_set) == len(s):
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.q3_lengthOfLongestSubstring('abbcd'))

# s = '1s1'
# char_arr = [c for c in s]
# cc = list(s)
# print(char_arr)
# print(cc)
