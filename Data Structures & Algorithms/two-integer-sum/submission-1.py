class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        nums: Dict[int]
        target: int

        Returns: List[int], where the values are indexes that add up to target
        '''

        '''
        [3, 4, 5, 6]
        dict: {4: 0, 3:1, 2:2, 1: 3}
        '''

        #O(n) space
        diff_dict = {}

        #O(n) runtime
        for i in range(len(nums)):

            if nums[i] in diff_dict:
                return [diff_dict[nums[i]], i]

            difference = target - nums[i]
            diff_dict[difference] = i