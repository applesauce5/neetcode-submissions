"""
Merge Sort
[1], [1,2]

--------------

1 [5,4,3,2,1]

2 [5,4,3]-[2,1]

3 [5,4]-[3]  [1]-[2]

4 [4]-[5]
--------------------

merge>>
[3,5,6] [4,6,7]
1. create a list of len(l1) + len(l2)
2. iterate through both and insert into list
3. return final list
"""

def merge(l1, l2) -> list:
    l3 = []

    i,j = 0,0

    while i < len(l1) or j < len(l2):
        if i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                l3.append(l1[i])
                i+=1
            else:
                l3.append(l2[j])
                j+=1
        elif i < len(l1):
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    print(l3)
    return l3


def mergeSort(inp) -> list:
    if len(inp) <= 1:
        return inp
    else:
        # Typical case
        l = mergeSort(inp[:len(inp) // 2]) 
        r = mergeSort(inp[len(inp) // 2:])
 
        return merge(l, r)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return mergeSort(nums)

