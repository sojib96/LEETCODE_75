class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = {}
        similarityCount = 0

        for row in grid:
            row_tuple = tuple(row)
            if row_tuple not in hashmap:
                hashmap[row_tuple] = 1
            else:
                hashmap[row_tuple] += 1
        
        for col in zip(*grid):
            similarityCount += hashmap.get(tuple(col), 0)
        
        return similarityCount