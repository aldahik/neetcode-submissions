class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        pref[0] = 1
        suff[len(nums) - 1] = 1
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            pref[i] = prod

        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i+1]
            suff[i] = prod

        for i in range(len(nums)):
            output[i] = suff[i] * pref[i]
        
        return output