class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fin = ""

        i = 0
        j = 0

        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                
                fin = fin + word1[i]
                i+=1
                
                fin = fin + word2[j]
                j+=1
            elif i < len(word1):
                fin = fin + word1[i]
                i+=1
            else:
                fin = fin + word2[j]
                j+=1
        return fin
        