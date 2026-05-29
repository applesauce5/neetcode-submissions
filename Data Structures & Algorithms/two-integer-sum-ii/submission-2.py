"""
Ordered list
O(1) space

1 valid solution

a + b = target

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for idx, num in enumerate(numbers):
            find = target - num
            j = idx - 1

            while j >= 0:
                # print(find, numbers[j])
                if find == numbers[j]:
                    return [j+1, idx+1] 
                j-=1
