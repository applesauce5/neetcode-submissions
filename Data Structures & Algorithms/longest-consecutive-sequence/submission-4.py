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
        
        d = dict()
        fin = 1
        for num in nums:
            # Check left
            # if (num - 1) in d:
            #     left = d[num-1]
            # else:
            #     left = 0 

            # # Check right
            # if (num + 1) in d:
            #     right = d[num+1]
            # else:
            #     right = 0

            # print(num-1, num+1, num)
            if num not in d:

                left = d.get(num-1, 0)
                right = d.get(num+1, 0)

                length =  1 + left + right
                fin = max(fin, length)

                d[num] = length

                print("DNUM:", d[num])
                print("FIN:", fin)
                
                # d[num-1] = length
                # Left boundary
                d[num - left] = length

                # d[num+1] = length

                d[num + right] = length

        return fin


