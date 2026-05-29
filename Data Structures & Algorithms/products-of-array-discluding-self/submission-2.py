"""
1 pass left
1 pass right

multiply each element = current product at i

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        retl = [1 for _ in range(len(nums))]

        curr = 1

        for idx, val in enumerate(nums):
            curr = curr*val
            retl[idx] = curr

        retr = [1 for _ in range(len(nums))]
        curr = 1
        for idx, val in reversed(list(enumerate(nums))):
            curr = curr*val
            retr[idx] = curr

        ret = [1 for _ in range(len(nums))]

        i = 0

        while i < len(nums):
            l = 1
            r = 1
            if i - 1 >= 0:
                l = retl[i-1]

            if i + 1 < len(nums):
                r = retr[i+1]

            ret[i] = l * r
            i+=1 

        return ret