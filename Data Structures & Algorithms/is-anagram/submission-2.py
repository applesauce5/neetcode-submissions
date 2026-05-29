class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = dict()
        tdict = dict()

        i = 0

        while i < len(s):
            if s[i] in sdict:
                sdict[s[i]] += 1
            else:
                sdict[s[i]] = 1

            if t[i] in tdict:
                tdict[t[i]] += 1
            else:
                tdict[t[i]] = 1
            i+=1

        if sdict == tdict:
            return True
        else:
            return False        