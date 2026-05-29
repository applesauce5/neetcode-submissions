"""
lr -> 1  2  8  48
rl <- 48 48 24 6 

product[i] = lr[i-1] * rl[i+1]

O(n) run time
O(n) space
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lr = [0 for _ in range(len(nums))]
        rl = [0 for _ in range(len(nums))]

        s1 = 1
        s2 = 1
        for i in range(len(nums)):
            s1 = s1 * nums[i]
            s2 = s2 * nums[len(nums) - 1 - i]
            lr[i] = s1
            rl[len(nums) - 1 - i] = s2

        output = []

        for i in range(len(nums)):
            _s1 = 1
            _s2 = 1
            if i > 0:
                _s1 = lr[i-1]

            if i < len(nums) - 1:
                _s2 = rl[i + 1]

            output.append(_s1 * _s2)

        return output
            

