class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 : return ""
        max_len = 0

        min_length_str = len(strs[0])

        for _ in range(len(strs)) :
            if len(strs[_]) < min_length_str :
                min_length_str = len(strs[_])

        for _ in range(min_length_str) :
            char = strs[0][_]
            status  = True
            for __ in range(len(strs)) :
                if strs[__][_] != char :
                    status = False
                    break
            if status :
                max_len += 1
            else : break
        return strs[0][0:max_len]
