"""
stack - ordering
> the future warmer day is strictly greater than the temp at day i
> absolute: the next immediate day there is a warmer day

push when empty or curr <= top of stack
pop when curr > top of stack
a. compute distance and update
b. loop

for each element in array
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        results = [0 for _ in range(len(temperatures))]
        _s = []
        for idx, temp in enumerate(temperatures):
            if len(_s) == 0:
                _s.append((temp, idx))
            else:
                if temp <= _s[-1][0]:
                    _s.append((temp, idx))
                else:
                    print(_s)
                    while _s and _s[-1][0] < temp:
                        # Compute and update the results
                        top = _s[-1]
                        topval = top[0]
                        topidx = top[1]
                        d = idx - topidx
                        results[topidx] = d
                        _s.pop()
                    _s.append((temp, idx))
            
        return results