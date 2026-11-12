class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            li = [0] * 26
            for ch in w:
                li[ord(ch) - 97] += 1
            groups[tuple(li)].append(w)
        return list(groups.values())
            