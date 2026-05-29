"""

element is exactly 1 greater

maintain a heap

push into heap (maintains order)
then pop from heap
- if the elements coming out is consecutive, then increment

"""
import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        l = []
        for i in nums:
            heapq.heappush(l,i)

        curr = heapq.heappop(l)
        ct = 1
        mct = ct

        while l:
            next = heapq.heappop(l)
            print(">>>",next)
            if (next - curr) <= 1:
                if (next - curr) == 1:
                    print(next, curr)
                    ct+=1
                    mct = max(ct, mct)
            else:
                ct = 1
            curr = next

        return mct
        