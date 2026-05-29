"""
group the anagrams together
> serialize an anagram into a hash
> values are the anagrams

return a list of lists of the grouped anagrams

serialize
> dict of occurrences of a letter

"""


def cad(anagram: str):

    ser = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    for letter in anagram:
        ser[letter] += 1
        
    return tuple(ser.items())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ga = dict()


        for name in strs:
            ser_name = cad(name)
 
            if ser_name not in ga:
                ga[ser_name] = list()

            ga[ser_name].append(name)

        return [name_list for name_list in ga.values()]