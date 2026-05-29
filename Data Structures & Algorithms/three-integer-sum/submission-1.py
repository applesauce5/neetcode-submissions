"""
All tripulets

sum is zero

return the values
----------------------
sort
left
right
bs

"""
def bs(l,r,li,find):

    if l > r:
        return None

    mid = l + ((r-l)//2)

    if li[mid] == find:
        return li[mid]
    else:
        if find < li[mid]:
            return bs(l, mid-1, li, find)

        else:
            return bs(mid+1, r, li, find)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)        

        ret = set()
        
        i = 0
        while i < len(snums) - 2:
            j = i+1
            left = snums[i]
            while j < len(snums) - 1:
                mid = snums[j]
                find = -left - mid
                right = bs(j+1, len(snums)-1,snums,find)
                if right is not None:
                    ret.add(tuple(sorted([left,right,mid])))
                j+=1
            i+=1

        return [list(i) for i in ret]

