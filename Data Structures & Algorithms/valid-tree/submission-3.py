"""

Assume that there is only 1 valid tree possible

> There are multiple trees possible
-----------------------------------------------
undirected edges
> a pair of nodes

given
> list of undirected edges

n nodes

node
-- should be no cycles; otherwise graph
[1, 2], [2, 3], [1, 3]

[3,1] [1,2] [3,2]  ->  [1,3] [1,2] [2,3] Cycle!!!
                        SD    D     //

[1 2] [2 3] [3 4]  Valid!!!
 SD     /D    /D   

 [1 2] [3 4] Multiple trees!!!
  SD    SD

[1 2] [3 4] [2 3] Out of order; valid

[1 2] [3 4] [3 2] Out of order; valid

>>>> Find a pair where S and D have already been visited

-- should be only 1 tree
[1,2], [3,4]

-- a node can have multiple edges
[1,2] [1,3] [1,4]

-- no duplicate edges
[1,0] ~ [0,1]


DFS on list of pairings
- if found in visited, then not valid tree

1 Create tree / graph
2 Traverse to validate tree/graph
  > cycle detection
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        _s = set()
        
        for idx, val in enumerate(edges):
            if val[1] == val[0]:
                # node points to itself
                return False
            if val[1] > val[0]:
                edges[idx] = [val[1], val[0]]

        edges.sort()
        
        tree_ct = 0

        for n, m in edges:
            i, j = False, False

            if n in _s:
                i = True

            if m in _s:
                j = True

            print("----------")
            print(_s)
            print(n,m)
            print(i, j)
            if i is False and j is False:
                tree_ct += 1

            if i and j:
                print("END")
                return False
            else:
                _s.add(n)
                _s.add(m)

        if tree_ct > 1:
            return False
        else:
            return True
        