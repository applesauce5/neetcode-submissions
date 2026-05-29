"""
if the sum is too big, move the right
if the sum is too small, move the left
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
  
        i = 0
        j = len(numbers) - 1

        while i < j:

            left = numbers[i]
            right = numbers[j]

            if left + right == target:
                return [i+1,j+1]
            elif left+right > target:
                j-=1
            else:
                i+=1

