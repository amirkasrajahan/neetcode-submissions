from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                res.extend(buckets[i])
            else:
                continue
        return res[:k]

        

            