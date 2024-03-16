class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_ = len(needle)
        len_h = len(haystack)
        diff = len_h-len_
        for _ in range(len_h) :
            if _ <= diff :
                if haystack[_:_+len_] == needle :
                    return _
        return -1
