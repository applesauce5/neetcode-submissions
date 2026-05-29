"""
searching for two values could lead to an O(n^2) solution since you have to traverse twice

to get O(n)
- keep a running history of values you have already visited
- if the (target - current_value) is in the history, then you have found your pair

- return the indices
- use a dict 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = dict()

        for idx, value in enumerate(nums):
            if target - value in history:
                return [history[target-value][0], idx]
            else:
                if value in history:
                    history[value] = history[value] + [idx]
                else:
                    history[value] = [idx]
        
        return []
        