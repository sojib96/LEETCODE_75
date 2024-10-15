#The logic is not correct for the input [20, 100, 10, 12, 5, 13]
#The problem statement is no also clear enough

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first , second = float('inf'), float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
