class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Use a dictionary for this solution

        Time: O(n)
        Space: O(n)

        '''
        result_dict = {}

        for num in nums:
            if num in result_dict:
                return True
            else:
                result_dict[num] = True

        return False