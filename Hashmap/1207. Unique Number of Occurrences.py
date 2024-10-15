class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
                
        occurenceSet = set()
        for key, value in hashMap.items():
            if value in occurenceSet:
                return False
            occurenceSet.add(value)
        return True
