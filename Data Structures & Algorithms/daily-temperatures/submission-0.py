"""
array

forcasting the next warmer day

if none 0

stack left

if val > top:
    append
pop until val < top

30 29 28 27 only appends 

27 28 29 30 pop until top of stack < curr 
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]

        _s = []

        i = 0

        while i < len(temperatures):
            temp = temperatures[i]

            while _s and temp > _s[-1][0]:
                p = _s.pop()
                pidx = p[1]
                res[pidx] = i - pidx
            _s.append((temp, i))
            i+=1
        return res
        
        