"""

h = heights

dist = j-i

vol = dist * (min(h[j] - h[i]))

if one side is smaller move that side
otherwise move the other side

O(n)

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        ret = -math.inf

        while i < j:
            dist = j-i
            print(i,j,"|",heights[i], heights[j])
            vol = dist * (min(heights[j], heights[i]))
            ret = max(vol, ret)

            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return ret