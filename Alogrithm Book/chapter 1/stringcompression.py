class Solution:
    def compress(self, chars):
        if len(chars) <= 1:
            return len(chars)

        write_index = 0
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                chars[write_index] = chars[i-1]
                write_index += 1
                if count > 1:
                    count_str = str(count)
                    for digit in count_str:
                        chars[write_index] = digit
                        write_index += 1
                count = 1

        chars[write_index] = chars[-1]
        write_index += 1
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write_index] = digit
                write_index += 1

        return write_index
"""Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3""""
