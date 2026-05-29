"""
> OPTIMIZATIONS
- sort (reduces duplication)
    > recurse on (arr[:i] + arr[i+1:]) while traversing array
    > add to a set - maintains a list of unique immutable obj when = 8

1 2 2 4 5 6 9

- NO duplicate combinations

"""

def recurse(_sum: int, _sum_parts: list, arr:list, target:int, fin:set):
    if _sum == target:
        if _sum_parts:
            _sum_parts.sort()
        fin.add(tuple(_sum_parts))
    if _sum > target:
        return
    for idx, val in enumerate(arr):
        recurse(_sum + val, _sum_parts + [val], arr[:idx] + arr[idx+1:], target, fin)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        fin = set()
        candidates.sort()
        print(candidates)
        
        recurse(0, [], candidates, target, fin)

        fin = list(fin)
        for idx, val in enumerate(fin):
            fin[idx] = list(val)

        return fin

