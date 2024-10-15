class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxValue = 0
        for i in candies:
            if i > maxValue:
                maxValue = i

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxValue:
                candies[i]  = True
            else:
                candies[i]  = False
        return candies