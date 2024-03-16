class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        greater_than_b = False
        count = 1
        while True :
            print(count)
            temp = a*count
            if b in temp :
                return count
            count +=1
            if len(temp) > len(a) + len(b) : break
        
        return -1
