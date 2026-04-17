class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = d.get(num, 1)

        d = sorted(d.items(), reverse=True, key=lambda d: d[1])
        d = [ i[0] for i in d ]
        return d[:k]
        

        