class Solution:
    def reverseWords(self, s: str) -> str:
        words = [""]

        for _ in range(len(s)) :
            if s[_] == " " :
                if words[-1] != "" :
                    words.append("")
            else :
                words[-1] = words[-1]+s[_]
        
        final = ""
        for _ in range(len(words)-1, -1, -1) :
            if words[_] != "" :
                final += words[_]+" "
        return final[:-1]
