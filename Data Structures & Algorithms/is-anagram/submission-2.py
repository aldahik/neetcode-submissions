class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {c: 0 for c in s}
        map2 = {c: 0 for c in t}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            map1[s[i]] += 1
            map2[t[i]] += 1

        return map1 == map2