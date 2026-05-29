"""
All tripulets

sum is zero

return the values
----------------------
sort
left
right
bs

0 = left + mid + right
- left = mid + right
"""



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)        
        ret = []
        i = 0
        # seen = set()
        while i < len(snums) - 2:
            j = i+1
            k = len(snums) - 1

            if i > 0 and snums[i] == snums[i-1]:
                i+=1
                continue
            left = snums[i]
            # if left in seen:
            #     i+=1
            #     continue
            # else:
            #     seen.add(left)

            while j<k:
                mid = snums[j]
                right = snums[k]

                if mid + right == -left:
                    ret.append([left,mid,right])
                    while k > j and k > 0 and snums[k] == snums[k-1]:
                        k-=1

                    while k > j and j < len(snums) - 1 and snums[j] == snums[j+1]:
                        j+=1   

                    j+=1
                    k-=1 

                elif mid + right > -left:
                    k-=1
                else:
                    j+=1
            i+=1

        return ret

