"""
1234+--

operand: pop pop
a. operation
b. push

other wise push
9 3 4 + 9 - :: Not valid
stack - preserve the order of rpn
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        _s = [] 
        
        for token in tokens:
            if token == "+":
                _s.append(int(_s.pop()) + int(_s.pop()))
            elif token == "-": 
                a = int(_s.pop())
                b = int(_s.pop())
                _s.append(b-a)
            elif token == "*":
                a = int(_s.pop())
                b = int(_s.pop())
                _s.append(b*a)
            elif token == "/":
                a = int(_s.pop())
                b = int(_s.pop())
                if (a < 0 and b > 0) or (b < 0 and a > 0):
                    e = (abs(b) // abs(a)) * -1
                else:
                    e = abs(b) // abs(a)
                _s.append(e)
            else:
                _s.append(token)

        return int(_s[0])