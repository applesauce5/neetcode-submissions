"""
abc
abbda
adbba
aab

"""
def vp(s, ct, start, end):
    if s == "":
        return True
    elif len(s) == 1:
        return True
    else:
        while start <= end:
            if s[start] != s[end]:
                if ct == 0:
                    return False
                else:
                    a = vp(s, ct - 1, start, end-1)
                    b = vp(s, ct - 1, start + 1, end)
                    return a or b
            start+=1
            end-=1

        return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        ct = 1
        return vp(s, ct, start, end)
        
        