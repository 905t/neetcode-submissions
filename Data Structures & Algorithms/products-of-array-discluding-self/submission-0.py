class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums: List [int] A list of numbers

        Returns: A list of integer where output[i] is the product of all elements except 
        nums[i]

        [1, 2, 4, 6]

        left_arr: [1, 1, 2, 8]

        right_arr: [48, 24, 6, 1]

        [48, 24, 12, 8]

        '''

        # O(1) space
        res = [1] * len(nums)


        # O(n) runtime
        left_product = 1
        for i in range(len(nums)):
            res[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res
