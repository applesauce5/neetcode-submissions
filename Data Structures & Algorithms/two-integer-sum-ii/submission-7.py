"""
Ordered list
O(1) space

1 valid solution

a + b = target

0         5
1 2 3 4 5 6
m = 2


s ~ 3
r ~ 5

r-s // 2 = 5-3 // 2


"""

def bs(s,e,li,target):

    if s > e:
        return None

    mid = s + ((e-s) // 2) # floor

    if li[mid] == target:
        return mid
    else:
        if li[mid] > target:
            return bs(s, mid - 1, li, target)
        else:
            return bs(mid + 1, e, li, target)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for idx, num in enumerate(numbers):
            find = target - num

            # Binary search here
            res = bs(0, idx - 1, numbers, find)
            # print(">>>",res)
            if res is not None:
                return [res+1, idx+1]
            # while j >= 0:
            #     # print(find, numbers[j])
            #     if find == numbers[j]:
            #         return [j+1, idx+1] 
            #     j-=1
