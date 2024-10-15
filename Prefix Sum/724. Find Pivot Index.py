class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = 0
        subSum = 0
        
        for num in nums:
            totalSum += num
        
        for i in range(len(nums)):
            diff = totalSum - subSum
            subSum += nums[i]
            if subSum == diff:
                return i
        return -1

# time complexity O(n) | space complexity 0(1)