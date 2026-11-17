class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        s: String
        t: String

        Return True IFF s and t are anagrams of each other

        '''

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 1
            else:
                s_dict[ch] += 1

        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 1

            else:
                t_dict[ch] += 1

        for key, value in s_dict.items():
            if key not in t_dict:
                return False

            elif t_dict[key] != value:
                return False

        return True


