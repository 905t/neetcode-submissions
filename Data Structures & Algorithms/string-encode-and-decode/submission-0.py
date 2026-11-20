class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        strs [List]: A list of strings

        Return: Return a single string

        ["Hello","World"] -?
        
        "5*Hello5*World"
         i
         j

          [i:j] = 5

           str[j+1:j+1+5]

        ["Hello", "World"]

        Len(word) + '*" + word -> result str

        '''
        result_str = ''

        #O(n), where is the number of words 
        for word in strs:
            result_str += str(len(word)) + "*" + word

        return result_str


    def decode(self, s: str) -> List[str]:
        '''
        s [str]: A string of the length of word + * + word, all joined together

        Returns: List[str]: A list of words originally provided in the strs function

        "5*Hello5*World"
                i
                 j

        
        '''
        result = []
        i = 0   
        
        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1

            cur_length = int(s[i:j])
            cur_word = s[j+1: j+1+cur_length]
            result.append(cur_word)
            i = j + 1 + cur_length

        return result