class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointerIdx = 0
        tPointerIdx = 0

        while sPointerIdx < len(s) and tPointerIdx < len(t):
            if s[sPointerIdx] == t[tPointerIdx]:
                sPointerIdx += 1
            tPointerIdx += 1
            
        return sPointerIdx == len(s)