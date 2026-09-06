class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {n:i for i,n in enumerate(nums)}
        for i,n in enumerate(nums):
            if target - n in vals and i != vals[target - n]:
                return [i, vals[target - n]]
        return []