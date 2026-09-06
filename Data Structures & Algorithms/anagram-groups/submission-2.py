class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}

        for s in strs:
            sorted_str = str(sorted(s))
            if sorted_str not in anas:
                anas[sorted_str] = [s]
            else:
                anas[sorted_str].append(s)
            
        return list(anas.values())