"""
nums1
nums2

alternating
[1 3 5 7 0 0 0 0] [2 4 6 8]

Create an external data structure
O(n+m)

Start inserting by descending order first
decrement both until both are finished
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        main = (m + n) - 1
        m,n = m-1, n-1
        while m >= 0 or n >= 0:
            if m >= 0 and n >= 0:
                if nums1[m] > nums2[n]:
                    nums1[main] = nums1[m]
                    main -= 1
                    m -= 1
                else:
                    nums1[main] = nums2[n]
                    main -= 1
                    n -= 1
            elif m >= 0:
                nums1[main] = nums1[m]
                main -= 1
                m -= 1
            else:
                # n > 0
                nums1[main] = nums2[n]
                main -= 1
                n -= 1
            

        return nums1
        