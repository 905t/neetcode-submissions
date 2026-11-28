from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        s (str): String 
        t (str): String

        Return True if and only if s is an anagram of t
        
        Idea:
            s_letter_to_count: {'r': 2, 'a': 2, 'c': 2, 'e': 1}
            t_letter_to_count: {'c': 2, 'a': 2, 'r': 2,, 'e': 1}
        
        '''

        if len(s) != len(t):
            return False

        s_letter_to_count = defaultdict(int)
        t_letter_to_count = defaultdict(int)

        for ch in s:
            s_letter_to_count[ch] += 1

        for ch in t:
            t_letter_to_count[ch] += 1

        for letter, count in s_letter_to_count.items():
            if letter not in t_letter_to_count:
                return False
            
            if t_letter_to_count[letter] != count:
                return False

        return True