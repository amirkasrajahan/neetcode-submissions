class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:  # smallest of the three is positive, so no sum can reach 0
                break
            if i > 0 and nums[i] == nums[i - 1]:  # skip a repeated first number
                continue

            lo, hi = i + 1, n - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:  # skip a repeated second number
                        lo += 1

        return res