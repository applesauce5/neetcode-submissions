class Solution:
    def isPalindrome(self, s: str) -> bool:

        k = ""

        for n in s:
            if n.isalnum():
                if n.isalpha():
                    k += n.lower()
                else:
                    k += n

        if k == k[::-1]:
            return True
        else:
            return False
