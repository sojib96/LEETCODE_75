class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashsetOne = set(nums1)
        hashsetTwo = set(nums2)
        subResult =[]
        result = []

        for num in hashsetOne:
            if num not in hashsetTwo:
               subResult.append(num)
        result.append(subResult)
        
        subResult = []
        for num in hashsetTwo:
            if num not in hashsetOne:
               subResult.append(num)
        result.append(subResult)

        return result
