class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointerIdx = 0
        rightPointerIdx = len(height) - 1
        maxValue = 0

        while leftPointerIdx <= rightPointerIdx:
            if height[leftPointerIdx] > height[rightPointerIdx]:
                subMax = height[rightPointerIdx] * (rightPointerIdx - leftPointerIdx)
                rightPointerIdx -= 1
            else:
                subMax = height[leftPointerIdx] * (rightPointerIdx - leftPointerIdx)
                leftPointerIdx += 1
            
            maxValue = max(maxValue, subMax)
        
        return maxValue
