class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentString = ""
        currentNum = 0

        for char in s:
            if char.isdigit():
                currentNum = (currentNum * 10) + int(char)
            elif char == "[":
                stack.append((currentString, currentNum))
                currentString = ""
                currentNum = 0
            elif char == "]":
                lastString, multiplier = stack.pop()
                currentString = lastString + currentString * multiplier
            else:
                currentString += char
                
        return currentString