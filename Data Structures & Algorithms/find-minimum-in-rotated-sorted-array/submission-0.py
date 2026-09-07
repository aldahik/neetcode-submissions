class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval = nums[0]
        l, r = 0, len(nums) - 1
        while (l <= r):
            if nums[l] < nums[r]:
                minval = min(minval, nums[l])
                break
            m = (l + r) // 2
            minval = min(minval, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minval
