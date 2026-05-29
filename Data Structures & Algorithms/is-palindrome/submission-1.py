class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""
        for char in s:
            if ("a" <= char <= "z") or ("A" <= char <= "Z"):
                k += char.lower()

            elif ("0" <= char <= "9"):
                k += char

        i = 0
        j = len(k) - 1

        while i < j:
            if k[i] != k[j]:
                return False
            i+=1
            j-=1

        return True
