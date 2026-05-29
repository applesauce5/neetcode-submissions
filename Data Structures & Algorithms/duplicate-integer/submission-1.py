"""
keep a dict of values it has seen before
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _d = dict()

        # go through inputs and index into the created array
        # if it appears twice in the created array, then False
        for i in nums:
            if i in _d:
                if _d[i] + 1 == 2:
                    return True
                else:
                    _d[i] += 1
            else:
                _d[i] = 1

        # True if we hash all the values
        return False