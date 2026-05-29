class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True

        if not s.strip():
            return True

        i = 0
        j = len(s) - 1
        s = s.lower()
        while i <= j:
            # print(i,j)
            while i < len(s) and not s[i].isalnum():
                i+=1

            while j > 0 and not s[j].isalnum():
                j-=1
            if i <= j:
                if s[i] != s[j]:
                    return False

            i+=1
            j-=1

        return True
