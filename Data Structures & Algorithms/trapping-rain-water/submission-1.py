"""
left to right

traverse until you find a height == or < the left height
take the min of the two heights
sum up _min_height - heights of the previous observations

---------------------

identify the peaks (either left or right side is less than or equal than the neighbor)
a. left is equal and right is smaller
b. right is smaller and right is equal

between each peak, calculate the volume
min of either peak - height at i
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        rightMax = [0 for _ in range(len(height))]
        leftMax = [0 for _ in range(len(height))]

        _max = -math.inf
        _rmax = -math.inf
        for i in range(len(height)):
            _max = max(_max, height[i])
            _rmax = max(_rmax, height[len(height) - 1 - i])
            leftMax[i] = _max
            rightMax[len(height) - 1 - i] = _rmax

        vol = 0
        # print(leftMax, rightMax)
        for idx, val in enumerate(height):
            if leftMax[idx] > val and rightMax[idx] > val:
                _mh = min(leftMax[idx], rightMax[idx])

                vol += _mh - val
                # print(idx, leftMax[idx], rightMax[idx], val, curr_vol)
        return vol
            


