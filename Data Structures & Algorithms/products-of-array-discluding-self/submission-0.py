class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product_list = [1]*len(nums)
        suffix_product_list = [1]*len(nums)
        result = []

        
        prefix_product = 1
        for i in range(len(nums)):
            prefix_product_list[i] = prefix_product
            prefix_product = prefix_product * nums[i]

        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix_product_list[i] = suffix_product 
            suffix_product = suffix_product * nums[i]

        for prefix, suffix in zip(prefix_product_list, suffix_product_list):
            result.append(prefix*suffix)
        return result
