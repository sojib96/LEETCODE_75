class Solution:
    def reverseWords(self, s: str) -> str:
        stringList = s.split()

        l = 0
        r = len(stringList) - 1
        if len(stringList) > 1:
            while l <= r:
                stringList[l], stringList[r] = stringList[r], stringList[l]
                l += 1
                r -= 1
        return (" ").join(stringList)