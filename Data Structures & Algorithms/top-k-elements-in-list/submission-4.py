class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        nums (Int): List of numbers
        k (int): k most frequent numbers to get from nums

        Returns List[int], which are the most frequent elements from nums
        '''

        '''
        count_dict
        {1: 1, 2:2, 3:3}

        occ_to_num_dict:
        {1: [1], 2: [2], 3: [3], 4: [], 5: [], 6: []} -> Bucket sort

        [3, 2] = 2 elements = k

        '''
        count_dict = {}
        occ_to_num_dict = {}
        result_lst = []

        #O(n) runtime and space
        #Populate the count_dict
        for i in range(len(nums)):
            if nums[i] not in count_dict:
                count_dict[nums[i]] = 1

            else:
                count_dict[nums[i]] += 1

        #O(n) runtime and sapce
        #Populate the occ_to_num_dict with key = 1 to len(nums) and initialize with the empty list
        for i in range(1, len(nums)+1):
            occ_to_num_dict[i] = []

        #Add the elements to occ_to_num_dict dictionary
        for num, count in count_dict.items():
            occ_to_num_dict[count].append(num)

        #We want to append to result_list up to len(k)
        for i in range(len(nums), 0, -1):

            for num in occ_to_num_dict[i]:
                result_lst.append(num)

            if len(result_lst) == k:
                return result_lst

          
