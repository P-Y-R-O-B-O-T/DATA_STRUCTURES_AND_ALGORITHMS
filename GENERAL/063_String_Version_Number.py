class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        for _ in range(len(v1)) : v1[_] = int(v1[_])
        for _ in range(len(v2)) : v2[_] = int(v2[_])

        for  _ in range(min(len(v1), len(v2))) :
            if v1[_] > v2[_] : return 1
            if v1[_] < v2[_] : return -1

        if len(v1) > len(v2) :
            for _ in range(len(v2), len(v1)) :
                if v1[_] != 0 : return 1
        if len(v2) > len(v1) :
            for _ in range(len(v1), len(v2)) :
                if v2[_] != 0 : return -1

        return 0
