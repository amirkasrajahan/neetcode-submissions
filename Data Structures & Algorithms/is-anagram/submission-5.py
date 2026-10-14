class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        li = [0] * 26
        for ch in s:
            li[ord(ch) - 97] += 1
        for ch in t:
            li[ord(ch) - 97 ] -= 1
        
        for num in li:
            if num != 0:
                return False
        
        return True
            
        