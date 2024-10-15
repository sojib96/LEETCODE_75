class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        leftPointer, zeroCount, maxWindowLength = 0, 0, 0

        for rightPointer in range(len(nums)):
            zeroCount += 1 if nums[rightPointer] == 0 else 0

            while zeroCount > 1:
                zeroCount -= 1 if nums[leftPointer] == 0 else 0
                leftPointer += 1
                    
            maxWindowLength = max(maxWindowLength, rightPointer - leftPointer)
        
        return maxWindowLength
    
# time complexity O(n) | space complexity 0(1)