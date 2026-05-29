"""
uniqueness

[ h e l l o ]


How would you decode?
> Any value is ASCII

> could add a character in front to determine how many characters is between each string

> when you decode you use this to determine the length of the encoded string

"""

class Solution:

    def _front(self, num:int):
        return str(num) + "_"

    def encode(self, strs: List[str]) -> str:
        
        ret = ""

        for s in strs:
            ret = ret + self._front(len(s)) + s    

        return ret

    def decode(self, s: str) -> List[str]:
        
        ret = list()
        j = 0

        while j < len(s):
            # determine length of string: ls
            n = ""
            while j < len(s) and s[j] != "_":
                n += s[j]
                j+=1

            j+=1 # Start on the first letter
            nnum = int(n)
            word = ""

            # read in the string; count < nnum
            while j < len(s) and nnum > 0:
                word += s[j]
                j+=1
                nnum -=1
            ret.append(word)
        return ret




