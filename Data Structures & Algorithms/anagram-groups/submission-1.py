class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for s in strs:
            ss = tuple(sorted(s))
            if ss in d:
                d[ss].append(s)
            else:
                d[ss] = [s]

        return [val for val in d.values()]


                
        