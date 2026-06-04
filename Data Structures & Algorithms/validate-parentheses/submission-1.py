class Solution:
    def isValid(self, s: str) -> bool:
        e = list()

        mp = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for i in s:
            if i in ("(", "{","["):
                e.append(i)
            elif i in (")", "}", "]"):

                if not e:
                    return False

                j = e.pop()
                if mp[i] != j:
                    return False

        if len(e) > 0:
            return False
        return True
        