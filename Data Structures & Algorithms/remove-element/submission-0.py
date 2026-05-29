"""
end of list pointer
traverse pointer

if tp != value:
    swap with eolp
    increment eolp

nums = nums[:eolp+1]

return eolp+1
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        eolp = 0
        for idx, val2 in enumerate(nums):
            if val2 != val:
                nums[eolp] = val2
                eolp += 1
        nums = nums[:eolp]
        return eolp
        