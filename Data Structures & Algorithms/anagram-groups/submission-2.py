class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        strs List[str]: Contains a list of a strings, which are words that can be grouped as anagrams

        Returns: list[list[str]] : A list of list of strings, where each item in the list are the anagrams
        '''

        #{(1, 0, 1, 0, 0, ..., 1, .. 0): ["act", "cat"], (1, ...., 1, 1, 0, 0): ['hat']}

        #Initialize a dictionary where the key is a tuple of indexes of 1s and 0s indicating position, value is the list of words
        
        #O(mn)
        ind_to_word_dict = {}
        result = []

        #O(mn)
        for word in strs:
            letter_indices = [0] * 26
            for ch in word:
                letter_indices[ord(ch) - ord('a')] += 1

            if tuple(letter_indices) not in ind_to_word_dict:
                ind_to_word_dict[tuple(letter_indices)] = [word]

            else:
                ind_to_word_dict[tuple(letter_indices)].append(word)

        for value in ind_to_word_dict.values():
            result.append(value)

        return result