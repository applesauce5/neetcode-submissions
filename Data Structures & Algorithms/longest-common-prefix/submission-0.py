"""
to find the longest common prefix
- scan of all the letters from left to right
- min length of the array
"""

import math
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _min = math.inf
        for _string in strs:
            _min = min(len(_string), _min)

        i = 0
        fin = ""

        while i < _min:
            letter = strs[0][i]
            for pref in strs:
                if letter != pref[i]:
                    # done
                    return fin
            fin += letter
            i+=1
        return fin