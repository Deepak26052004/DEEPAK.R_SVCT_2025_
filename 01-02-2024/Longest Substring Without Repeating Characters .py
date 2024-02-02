'''Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        char_index_map = {}  # To store the index of each character in the current substring
        max_length = 0
        start = 0

        for end in range(n):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1  # Move the start pointer to the next index of the repeating character

            char_index_map[s[end]] = end
            current_length = end - start + 1
            max_length = max(max_length, current_length)

        return max_length

# Example usage:
solution = Solution()

s1 = "abcabcbb"
print(solution.lengthOfLongestSubstring(s1))  # Output: 3

s2 = "bbbbb"
print(solution.lengthOfLongestSubstring(s2))  # Output: 1

s3 = "pwwkew"
print(solution.lengthOfLongestSubstring(s3))  # Output: 3
