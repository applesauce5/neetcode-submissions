class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            _min = row[0]
            _max = row[-1]

            if _min <= target <= _max:
                l = 0
                r = len(row) - 1

                while l <= r:

                    m = l + ((r-l)//2)

                    if row[m] == target:
                        return True
                    else:
                        if row[m] > target:
                            # left
                            r = m - 1
                        else:
                            l = m + 1

            
        return False

        