class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        leftPointer = 0
        maxAverage = -inf
        currentSum = 0

        for rightPointer in range(len(nums)):
            currentSum += nums[rightPointer]

            if ((rightPointer-leftPointer)+1) == k:
                currentAverage = currentSum / k
                maxAverage = currentAverage if currentAverage > maxAverage else maxAverage
                currentSum -= nums[leftPointer]
                leftPointer += 1 

        return maxAverage