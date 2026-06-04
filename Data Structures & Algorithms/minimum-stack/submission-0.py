"""
1 2 0
1 x2 0

stack that maintains min

smaller larger smaller 1 2 0
larger smaller smaller 2 1 0
smaller smaller larger 0 1 2

when you pop, there is a new min
what if you pop 1- 0 is still min

you only pop from the top
if the new element is smaller than the top, then push
when popping, if the top of the minstack is ==, then pop min stakc


"""


class MinStack:

    def __init__(self):
        self._s = []
        self._min = []
        

    def push(self, val: int) -> None:
        self._s.append(val)
        if not self._min:
            self._min.append(val)
        elif self._min[-1] >= val:
            self._min.append(val)

    def pop(self) -> None:
        j = self._s.pop()
        if j == self._min[-1]:
            self._min.pop()
        

    def top(self) -> int:
        return self._s[-1]
        

    def getMin(self) -> int:
        return self._min[-1]

        
