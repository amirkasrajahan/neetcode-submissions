class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)                      # num -> frequency
        buckets = [[] for _ in range(len(nums) + 1)]  # index = frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):   # highest frequency first
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res