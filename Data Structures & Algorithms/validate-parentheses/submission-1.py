class Solution:
    def isValid(self, s: str) -> bool:
        paras = {']' : '[', ')':'(', '}':'{'}
        read = []
        for char in s:
            if char in paras:
                if read and read[-1] == paras[char]:
                    read.pop()
                else:
                    return False
                
            else:
                read.append(char)

        return True if not read else False
            