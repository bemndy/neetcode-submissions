class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for num in nums:
            if num in s:
                s[num] += 1
            else: 
                s[num] = 1
        print(s)
        r = []
        for i in (range(k)):
            key = max(s.keys(), key=lambda k: s[k])
            r.append(key)
            del s[key]
        return r[::-1]

        