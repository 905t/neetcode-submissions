class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #O(n) Space
        num_set = set()

        #O(n)
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True

        return False 
