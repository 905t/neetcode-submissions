class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        s: String
        t: String

        Return True IFF s and t are anagrams of each other

        '''

        #If Two strings do not have the same length, then it's not an anagram 
        if len(s) != len(t):
            return False
        
        #Initliaze the dictionary
        s_occurence_dict = {}
        t_occurence_dict = {}

        #O(n) Space + O(n) Time Complexity
        #Loop through each letter in s, populate the dictionary with number of occurences
        for letter in s:
            if letter not in s_occurence_dict:
                s_occurence_dict[letter] = 1
            else:
                s_occurence_dict[letter] += 1

        #Loop through each letter in t, populate the dictionary with number of occurences
        for letter in t:
            if letter not in t_occurence_dict:
                t_occurence_dict[letter] = 1
            else:
                t_occurence_dict[letter] += 1

        #Compare s_occurence_dict values with t_occurence_dict values

        for letter in s_occurence_dict.keys():
            if letter not in t_occurence_dict:
                return False

            elif s_occurence_dict[letter] != t_occurence_dict[letter]:
                return False

        return True