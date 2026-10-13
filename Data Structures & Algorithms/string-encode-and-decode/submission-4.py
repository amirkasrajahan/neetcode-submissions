class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result = result + str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        while i < len(s):
            delimiter = s.find("#", i)
            length = int(s[i:delimiter])
            word = s[delimiter + 1 : delimiter + 1 + length]
            result.append(word)
            i = delimiter + 1 + length
        
        return result