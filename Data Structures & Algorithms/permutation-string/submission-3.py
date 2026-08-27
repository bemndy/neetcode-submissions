class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1, h2 = {}, {}
        for ch in s1:
            h1[ch] = 1 + h1.get(ch, 0)
        l = 0
        r = len(s1)
        
        while r < len(s2)+1:
            curr = s2[l:r]
            for ch in curr:
                h2[ch] = 1 + h2.get(ch, 0)

            if h2 != h1:
                h2 = {}
                r += 1
                l += 1
            else:
                return True

        return False
            

