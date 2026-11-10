class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cur_nums = {}

        #O(n)
        for num in nums:
            if num not in cur_nums:
                cur_nums[num] = 1

            else:
                return True

        return False