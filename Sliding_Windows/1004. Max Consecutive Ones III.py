class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        start = 0
        maxWindow = 0
        numOfZeros = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                numOfZeros += 1
            
            while numOfZeros > k:
                if nums[start]==0:
                    numOfZeros -= 1
                start += 1

            window = i - start + 1
            maxWindow = max(maxWindow , window)
        
        return maxWindow

# time complexity O(n) | space complexity 0(1)