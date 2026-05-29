class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ret = [0 for _ in range(len(nums) * 2)]

        i = 0

        while i < len(nums):
            ret[i] = nums[i]
            ret[i + len(nums)] = nums[i]
            i+=1

        return ret