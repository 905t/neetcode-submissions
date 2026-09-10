class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Use a dictionary for this solution

        Time: O(n)
        Space: O(n)

        '''
        result_dict = {}

        for num in nums:
            if num not in result_dict: 
                result_dict[num] = 1

            else:
                return True

        return False

        