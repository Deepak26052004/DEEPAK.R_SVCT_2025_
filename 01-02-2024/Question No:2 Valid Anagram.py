'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if the lengths of both strings are equal
        if len(s) != len(t):
            return False

        # Create dictionaries to store character frequencies for each string
        s_freq = {}
        t_freq = {}

        # Populate the frequency dictionaries for string s
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        # Populate the frequency dictionaries for string t
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        # Compare the frequency dictionaries
        return s_freq == t_freq

# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False
