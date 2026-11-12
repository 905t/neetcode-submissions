class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        nums: Dict[int]
        target: int

        Returns: List[int], where the values are indexes that add up to target
        '''
        
        # [3,4,5,6], target = 7
        # {4:0, 3:1, 2:2, 1:3}
        
        #O(n) Space, where n is len(nums)
        difference_to_value_dict = {}

        #O(n) Runtime
        for i in range(len(nums)):
            if nums[i] in difference_to_value_dict:
                return [difference_to_value_dict[nums[i]], i]

            difference = target-nums[i]

            difference_to_value_dict[difference] = i 