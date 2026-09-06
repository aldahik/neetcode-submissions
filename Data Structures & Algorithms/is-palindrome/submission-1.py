
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = s.strip().lower().replace(" ", "")
        for c in stripped_s:
            if not c.isalpha() and not c.isnumeric():
                stripped_s = stripped_s.replace(c, '')
        i = 0
        j = len(stripped_s) - 1
        while(i < j):
            if stripped_s[i] != stripped_s[j]:
                return False
            i += 1
            j -= 1

        return True

