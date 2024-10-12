
#approach: 1
class Solution:
    def reverseVowels(self, s: str) -> str:
        setOfVowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        stack  = []
        resultList = []

        for i in range(len(s)):
            if s[i] in setOfVowels:
                stack.append(s[i])
            resultList.append(s[i])
        
        for i in range(len(s)):
            if s[i] in setOfVowels:
                resultList[i] = stack.pop()
        
        return "".join(resultList)
    
#approach: 2

class Solution:
    def reverseVowels(self, s: str) -> str:
        setOfVowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        resultList = list(s)
        
        i = 0
        r = len(resultList) - 1

        while i<=r:
            if resultList[i] in setOfVowels and resultList[r] in setOfVowels:
                resultList[i], resultList[r] = resultList[r], resultList[i]
                resultList[i]
                i += 1
                r -= 1
            else:
                if resultList[i] not in setOfVowels:
                    i += 1
                elif resultList[r] not in setOfVowels:
                    r -= 1
        return "".join(resultList)