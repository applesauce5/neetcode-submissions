class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()

        for idx, num in enumerate(nums):
            find = target - num
            if find in visited:
                return [visited[find], idx]
            else:
                visited[num] = idx

        return []  
        