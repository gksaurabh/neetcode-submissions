class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result = [1] * len(nums) # num : product of other members in the list

        prefix_product = 1
        postfix_product = 1
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = (prefix_product)
            else:
                prefix_product = prefix_product * nums[i-1]
                prefix[i] = (prefix_product)

        for i in range(len(nums) -1 , -1, -1):
            if i == (len(nums) -1):
                postfix[i] = (postfix_product)
            else:
                postfix_product = postfix_product * nums[i+1]
                postfix[i] = (postfix_product)

        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]
        return result