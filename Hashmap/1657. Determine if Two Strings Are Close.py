from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch1, ch2 in zip(word1, word2):
            freq1[ord(ch1) - ord('a')] += 1
            freq2[ord(ch2) - ord('a')] += 1
        
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False
        
        freq1.sort()
        freq2.sort()

        return freq1 == freq2
    
#Time complexity O(nlogn)
    
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        counterOne = Counter(word1)
        counterTwo = Counter(word2)

        for key in  counterOne:
            if key not in counterTwo:
                return False
        
        tab1 = Counter(counterOne.values())
        tab2 = Counter(counterTwo.values())

        for i in tab1.keys():
            if (tab1[i] != tab2[i]):
                return False
        
        return True
    
#Time complexity O(n)