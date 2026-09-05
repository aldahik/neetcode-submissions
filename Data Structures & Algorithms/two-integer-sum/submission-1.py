class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {n : i for i,n in enumerate(nums)}
        
        for i,n in enumerate(nums):
            if target - n in seen and i != seen[target - n]:
                return [i, seen[target - n]]