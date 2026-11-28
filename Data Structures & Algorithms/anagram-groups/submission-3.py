from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        strs List[str]: Contains a list of a strings, which are words that can be grouped as anagrams

        Returns: list[list[str]] : A list of list of strings, where each item in the list are the anagrams
        '''

        #{(1, 0, 1, 0, 0, ..., 1, .. 0): ["act", "cat"], (1, ...., 1, 1, 0, 0): ['hat']}

        #Initialize a dictionary where the key is a tuple of indexes of numbers indicating position, value is the list of words
        
        tuple_to_words_dict = defaultdict(list)
        result = []
        
        for word in strs:
            cur_lst = [0] * 26
            for ch in word:
                cur_lst[ord('a') - ord(ch)] +=1 

            tuple_to_words_dict[tuple(cur_lst)].append(word)

        for lst in tuple_to_words_dict.values():
            result.append(lst)

        return result