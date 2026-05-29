"""
appears more than n/2 times

brute force:
iterate and hashtable value vs occurrences
return the value with the highest occurence
---------------------------------------------

Boyer-Moore Majority Voting Algorithm
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        obs = 1
        curr = nums[0]

        for idx, val in enumerate(nums[1:]):
            if val == curr:
                obs+=1
            else:
                obs-=1
                if obs == 0:
                    curr = val 
                    obs = 1
        return curr
        