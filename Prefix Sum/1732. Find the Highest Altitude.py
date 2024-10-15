#uisng prefix sum array | time complexity O(n) | space complexity 0(n)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        highestAltitude = 0

        prefixArray = [gain[0]]

        for i in range(1, n):
            prefixArray.append(prefixArray[i-1] + gain[i])
        
        for i in prefixArray:
            highestAltitude = i if i > highestAltitude else highestAltitude
        
        return highestAltitude
    

# time complexity O(n) | space complexity 0(1)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highestAltitude = 0
        prefixSum = 0

        for altitude in gain:
            prefixSum += altitude
            highestAltitude = prefixSum if prefixSum > highestAltitude else highestAltitude
        
        return highestAltitude