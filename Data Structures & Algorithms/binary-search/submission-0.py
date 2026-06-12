class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(nums, l, r, target):

            if l > r:
                return -1

            mid = l + ((r-l) // 2)

            if nums[mid] == target:
                return mid
            else:
                left = bs(nums, l, mid-1, target)
                right = bs(nums, mid+1, r, target)

                if left != -1:
                    return left
                elif right != -1:
                    return right
                else:
                    return -1
        return bs(nums, 0, len(nums)-1, target)
        