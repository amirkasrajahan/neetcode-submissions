class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left ,right = 0, len(heights) - 1
        best = 0
        while left < right:
            current = min(heights[left],heights[right]) * (right - left)
            if current > best:
                best = current
            if heights[right] < heights[left]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:    #in case the are equal
                if heights[right - 1] > heights[left + 1]:
                    right -= 1
                else:
                    left += 1
        return best



