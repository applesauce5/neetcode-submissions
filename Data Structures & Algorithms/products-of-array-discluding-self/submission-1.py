"""

have 2 arrays that store...
- all products going right
- all products going left

1 pass, using the 2 ds's above, find the product of arr[i]
- all arrays initialized with 1
- store product, then multiply, repeat

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1 for _ in range(len(nums))]
        backward = [1 for _ in range(len(nums))]

        p_f = 1
        p_b = 1

        for idx, val in enumerate(nums):
            forward[idx] = p_f
            backward[len(nums) - 1 - idx] = p_b
            p_f = p_f * nums[idx]
            p_b = p_b * nums[len(nums) - 1 - idx]    

        # print(forward)
        # print(backward)
        fin = []

        for i in range(len(nums)):
            v1 = forward[i]
            v2 = backward[i]
            fin.append(v1 * v2)
        return fin
