class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for idx, num in enumerate(nums):
            find = target-num
            if find in d:
                return [d[find], idx]
            
            d[num] = idx

            
        