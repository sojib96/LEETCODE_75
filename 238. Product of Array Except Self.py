class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultArray = [1]*len(nums)
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            resultArray[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            resultArray[i] *= suffix
            suffix *= nums[i]
        
        return resultArray
