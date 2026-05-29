"""
number of characters
type of characters

order does not matter
- ordering is at a worst case O(nlogn)

keep a map of a-z for both strings with counts as values
if the dictionaries are equivalent, then they are anagrams

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create the dictionary key pair value
        _s = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'r': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }
        _t = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'r': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }

        # count s
        for i in range(len(s)):
            _s[s[i]] += 1

        # count t
        for i in range(len(t)):
            _t[t[i]] += 1

        # compare
        if _s == _t:
            return True
        else:
            return False
        