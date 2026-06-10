"""

Area of the largest rectangle
Order is not changed
-------
-
-------
-- 
--
----
8 


-
---
-------
1 3 7

min height of the groupings

worst case, O(n^2) find the area of each possible rectangle
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        _m = -math.inf
        for i in range(len(heights)):
            j = i
            mh = heights[j]
            while j < len(heights):
                mh = min(heights[j], mh)
                w = 1 + (j-i)
                _m = max(_m,mh * w)
                j+=1
        
        return _m