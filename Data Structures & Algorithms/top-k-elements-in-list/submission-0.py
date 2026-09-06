from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_nums = sorted(nums, key= lambda n : freq[n], reverse= True)
        sorted_set = set(sorted_nums)
        res = []

        j = 0
        for n in sorted_nums:
            if n not in res and j<k:
                res.append(n)
                j += 1
            if j == k:
                break

        return res





            