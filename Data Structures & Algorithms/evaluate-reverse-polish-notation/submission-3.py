"""
2 numbers for expression
1 2 + 3 * 4 -

(3) 3 * 

(9) 4 -


123-  ~ X

1-23+ ~ X

123   ~ X

-+    ~ X

------------------------
stack length of 2

in the end - stack length of 1
------------------------
"10","6","9","3","+","-11","*","/","*","17","+","5","+"

10 6 12 -11 *
10 6 -132 /
10 0 *
0 17 +
17 5 +
22

Division:
-1 -1 : both are negative
-1  1 : either are negative
 1 -1 : 
 1  1 : both are positive
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        _s = []

        for i in tokens:
            

            if i not in ("+", "-", "*", "/"):
                _s.append(i)
            else:
                b = int(_s.pop())
                a = int(_s.pop())
                
                if i == "+":
                    e = a + b
                elif i == "-":
                    e = a - b
                elif i == "*":
                    e = a * b
                else:
                    if a < 0 and b < 0:
                        # both negative
                        e = a // b
                    elif a<0 or b<0:
                        e = ( abs(a) // abs(b) ) * (-1)
                    else:
                        e = a // b
                    # print("OUT", e)
                # print(a,b, i)
                _s.append(str(e))
        return int(_s[0])


