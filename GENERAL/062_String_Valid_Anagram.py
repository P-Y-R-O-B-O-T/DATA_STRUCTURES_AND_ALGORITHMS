class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        s_map = {}
        t_map = {}

        for _ in s :
            if _ not in s_map :
                s_map[_] = 1
            else :
                s_map[_] += 1
        for _ in t :
            if _ not in t_map :
                t_map[_] = 1
            else :
                t_map[_] += 1
        
        for _ in t_map :
            if _ in s_map :
                if t_map[_] != s_map[_] :
                    return False
            else :
                return False
        return True
