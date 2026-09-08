class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output, pref, suff, = [1]*n, [1]*n, [1]*n

        pref[0] = 1
        suff[n - 1] = 1
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            pref[i] = prod
        prod = 1
        for j in range(len(nums) - 2, -1, -1):
            prod *= nums[j+1]
            suff[j] = prod
        for k in range(len(nums)):
            output[k] = pref[k] * suff[k]

        return output

