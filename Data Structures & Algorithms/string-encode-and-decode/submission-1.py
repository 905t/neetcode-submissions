class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        strs [List]: A list of strings

        Return: Return a single string
        
        ['hello', 'World]

        ->

        5*Hello5*World

        '''

        res = ''

        for s in strs:
            res += str(len(s)) + '*' + s

        return res


    def decode(self, s: str) -> List[str]:
        '''
        s [str]: A string of the length of word + * + word, all joined together

        Returns: List[str]: A list of words originally provided in the strs function

        "5*Hello5*World"
         i
           j
        '''

        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '*':
                j += 1

            word_len = int(s[i:j])
            word = s[j+1: j + 1 + word_len]
            res.append(word)
            i = j + 1 + word_len

        return res            