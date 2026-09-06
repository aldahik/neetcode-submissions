class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        vals = {}
        for i,n in enumerate(nums):
            for j,m in enumerate(nums):
                sum = n + m
                if i == j or 0 - sum not in vals:
                    continue
                if vals[0 - sum] == i or vals[0 - sum] == j:
                    continue
                triple = sorted([n, m, 0 - sum])
                if triple not in res:
                    res.append(triple)
            vals[n] = i
            vals[m] = j
        return res