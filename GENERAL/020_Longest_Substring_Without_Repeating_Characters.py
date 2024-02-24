"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution :
    def max_substring_len(self,
                          string: str) -> int :
        if len(string) == 0 : return 0
        if len(string) == 1 : return 1

        characters_present = {}
        characters_present[string[0]] = 1

        start = 0
        end = 1
        max_len = 1

        while start < end and end < len(string) :
            if string[end] not in characters_present :
                characters_present[string[end]] = 1
                end += 1
            else :
                del characters_present[string[end]]
                start += 1
            max_len = max(max_len, end-start+1)
        
        return max_len
