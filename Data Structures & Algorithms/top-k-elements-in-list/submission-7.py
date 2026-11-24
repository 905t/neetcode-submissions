class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        nums (Int): List of numbers
        k (int): k most frequent numbers to get from nums

        Returns List[int], which are the most frequent elements from nums




        count:
        {1: 1, 2:2, 3: 3}


        occ_to_nums:
        {1: [1]
        2: 2[]
        .,.
        
        6: []}

        count:
        {1: 1, 2:2, 3: 3}

        6
        5
        4
        3
        2
        1


        '''

        count = {}
        occ_to_nums = {}
        output = []

        # Establish count dictionary 
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1

            else:
                count[nums[i]] += 1


        # Establish occ_to_num dictionary 
        
        for i in range(1, len(nums) + 1):
            occ_to_nums[i] = []

        #populate occ_to_num with values
        for count, value in count.items():
            occ_to_nums[value].append(count)         


        # Loop in reverse order and pooulate the max output
        for i in range(len(nums), 0, -1):
            for num in occ_to_nums[i]:
                output.append(num)

                if len(output) == k:
                    return output