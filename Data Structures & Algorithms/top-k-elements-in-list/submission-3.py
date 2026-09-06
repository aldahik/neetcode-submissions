from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        nums2 = [(f,n) for n,f in freq.items()]
        nums2.sort(key = lambda n : n[0])
        res = []
        for i in range(k):
            res.append(nums2.pop()[1])

        return res



