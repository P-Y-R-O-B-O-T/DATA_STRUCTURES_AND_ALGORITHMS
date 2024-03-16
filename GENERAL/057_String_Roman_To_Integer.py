class Solution:
    def romanToInt(self, s: str) -> int:
        nums = [1000,500,100,50,10,5,1]
        romans = ["M","D","C","L","X","V","I"]

        map_ = {}
        for _ in range(len(nums)) :
            map_[romans[_]] = nums[_]
        
        map_["IV"] = 4
        map_["IX"] = 9
        map_["XL"] = 40
        map_["XC"] = 90
        map_["CD"] = 400
        map_["CM"] = 900

        integer = 0

        _ = 0
        while _ < len(s)-1 :
            if s[_:_+2] in map_ :
                integer += map_[s[_:_+2]]
                _ += 2
            else :
                integer += map_[s[_]]
                _ += 1

        if _ < len(s) :
            integer += map_[s[_]]

        return integer
