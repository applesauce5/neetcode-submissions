"""

"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [ 0 for i in range(len(nums)*2)]

        i = 0

        while i < len(nums):
            arr[i], arr[i+len(nums)] = nums[i], nums[i]
            i+=1

        return arr
