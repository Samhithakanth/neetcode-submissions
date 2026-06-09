class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_l = []
        i=0
        for i in range(len(nums)):
            prefix = 1
            suffix = 1
            j = i - 1
            k = i + 1
            while j >= 0:
                prefix = prefix * nums[j]
                j = j - 1
            while k < len(nums):
                suffix  = suffix * nums[k]
                k = k + 1
            product_l.append(suffix * prefix)
        return product_l