class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = dict()
        td = dict()

        if not s:
            return False

        if not t:
            return False

        if len(s) != len(t):
            return False


        i = 0

        while i < len(s):

            if s[i] in sd:
                sd[s[i]] += 1
            else:
                sd[s[i]] = 0

            if t[i] in td:
                td[t[i]] += 1
            else:
                td[t[i]] = 0

            i+= 1

        if sd != td:
            return False

        return True
        