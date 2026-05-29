class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        # 1 pass through
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=0


        # key: number value: occurence
        t = [(val, key) for key, val in d.items()]
        t = sorted(t)

        print(t)
        ret = []
        while k > 0:
            idx = len(t) - k
            ret.append(t[idx][1])
            k-=1

        print(ret)
        return ret

        
        