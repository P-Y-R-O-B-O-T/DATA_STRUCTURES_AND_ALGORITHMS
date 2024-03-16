class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0 : return s
        if len(s) == 2 and s[0] == s[1] : return s

        max_palindrome_len = 1
        max_palindrome = s[0]

        for _ in range(len(s)) :
            curr_longest_palindrome_len = 1
            temp1 = _-1
            temp2 = _+1

            while temp1 >= 0 and temp2 < len(s) and s[temp1] == s[temp2] :
                curr_longest_palindrome_len += 2
                if curr_longest_palindrome_len > max_palindrome_len :
                    max_palindrome = s[temp1:temp2+1]
                    max_palindrome_len = len(max_palindrome)
                temp1 -= 1
                temp2 += 1

        for _ in range(len(s)-1) :
            if s[_] == s[_+1] :
                temp1 = _
                temp2 = _+1
                curr_longest_palindrome_len = 0

                while temp1 >= 0 and temp2 < len(s) and s[temp1] == s[temp2] :
                    curr_longest_palindrome_len += 2
                    if curr_longest_palindrome_len > max_palindrome_len :
                        max_palindrome = s[temp1:temp2+1]
                        max_palindrome_len = len(max_palindrome)
                    temp1 -= 1
                    temp2 += 1

        return max_palindrome
