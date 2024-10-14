# Two pointer with O(nLogn) time complexity, space complexity O(1)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums)
        leftPointer = 0
        rightPointer = len(nums) - 1
        count = 0

        while leftPointer < rightPointer:
            if sortedNums[leftPointer] + sortedNums[rightPointer] == k:
                count += 1
                leftPointer += 1
                rightPointer -= 1
            
            elif sortedNums[leftPointer] + sortedNums[rightPointer] < k:
                leftPointer += 1
            else:
                rightPointer -= 1
        
        return count

# HashMap with O(n) time complexity, space complexity O(n)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashset = {}
        count = 0 

        for num in nums:
            diff = k - num
            if diff in hashset and hashset[diff] > 0:
                count += 1
                hashset[diff] -= 1
            
            else:
                if num in hashset:
                    hashset[num] += 1
                else:
                    hashset[num] = 1
        
        return count