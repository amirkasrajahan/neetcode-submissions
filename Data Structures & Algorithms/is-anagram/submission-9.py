class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0] * 26
        for ch in s:
            res[ord(ch) - 97] += 1
        for ch in t:
            res[ord(ch) - 97] -= 1
            if res[ord(ch) - 97] < 0:
                return False
        
        for n in res:
            if n != 0:
                return False
        return True