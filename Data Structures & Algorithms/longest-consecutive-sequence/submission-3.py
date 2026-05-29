"""

element is exactly 1 greater

maintain a heap

push into heap (maintains order)
then pop from heap
- if the elements coming out is consecutive, then increment

"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        s = set()

        for num in nums:
            s.add(num)

        ret = 1
        for num in nums:
            prev = num - 1

            # Beginning of sequence
            if prev not in s:
                i = 0
                curr = num
                while curr in s:
                    i+=1
                    curr+=1
                ret = max(ret, i)

        return ret
        