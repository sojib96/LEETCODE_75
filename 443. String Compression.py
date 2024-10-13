class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0,0
        while read < len(chars):
            currentChar = chars[read]
            count = 0

            while read< len(chars) and currentChar == chars[read]:
                read +=1 
                count += 1
            
            chars[write] = currentChar
            write += 1

            if count > 1:
                for degits in str(count):
                    chars[write] = degits
                    write += 1
        
        return write

