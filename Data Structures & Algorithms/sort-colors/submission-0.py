class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        0,1,2 only exist
        1 pass algorithm
        constant space
        """
        visited = {
            0:0,
            1:0,
            2:0
        }

        for i in nums:
            visited[i] += 1

        idx = 0
        for key,val in visited.items():
            while val > 0:
                nums[idx] = key
                val -= 1
                idx += 1
        