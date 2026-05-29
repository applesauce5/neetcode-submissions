"""
remove duplicates
return num of unique elements
first k elements of nums contain unique elements

[1 2 3 4]

[1 2 2 3 4]
[1 2 2/3 3/4 3 4]

[1 2 2]
[1 2 2/3 3] slow increments and takes the value of fast, increment fast


[1 2]
[2 2]

if fast != slow:
    # normal
    increment slow
    increment fast
if fast == slow:
    # increment fast until no more
    # swap

loop until fast is finished
k = number of times slow moved
slow + 1

[1 1/2 2 3 4]
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        else:
            slow = 0 
            fast = 1

            while fast < len(nums):
                if nums[fast] != nums[slow]:
                    fast_val = nums[fast]
                    fast += 1
                    slow += 1
                    nums[slow] = fast_val
                else:
                    while fast < len(nums) and nums[fast] == nums[slow]:
                        fast += 1
                    if fast < len(nums):
                        slow += 1
                        new_number = nums[fast]
                        nums[slow] = new_number
                        fast += 1
            return slow + 1

        