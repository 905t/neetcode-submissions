class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        nums (Int): List of numbers
        k (int): k most frequent numbers to get from nums

        Returns List[int], which are the most frequent elements from nums
        '''

        '''
        {1: 1, 2:2, 3:3}

        {0: [], 1:[], 2: [], ..,., 7: []}

        i up to the len(nums)
        {0: [], 1: [1], 2: [2], 3: [3] ...,. 6:}

        {7:2}
        {0: [], 1:[], 2:[7]}

        Loop through values of the dictionary above in reverse order:
        [3, 2]
        '''

        num_to_val = {}
        occ_dict = {}
        return_lst = []

        #Populate the num_to_val dictionary
        for num in nums:
            if num not in num_to_val:
                num_to_val[num] = 1

            else:
                num_to_val[num] += 1

        #Initialize empty array within occ_dic value
        for i in range(len(nums)+1):
            occ_dict[i] = []

        #Populate occ_dicc with the occurence, where the key is the number of occurence and the value is the number/element itself
        for num, val in num_to_val.items():
            occ_dict[val].append(num)

        for i in range(len(nums), -1, -1):
            if len(occ_dict[i]) > 0:
                for num in occ_dict[i]:
                    if len(return_lst) < k:
                        return_lst.append(num)

        return return_lst


