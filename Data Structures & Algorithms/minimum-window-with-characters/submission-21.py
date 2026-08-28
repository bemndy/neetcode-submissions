class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t1, s1 = {}, {}
        for c in t:
            t1[c] = 1 + t1.get(c, 0)

        have, need = 0, len(t1)
        res = [-1, -1]
        res_len = float('infinity')
        l = 0

        for r in range(len(s)):
            c = s[r]
            s1[c] = 1 + s1.get(c, 0)

            if c in t1 and s1[c] == t1[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = [l, r]
                c = s[l]
                s1[c] -= 1
                if c in t1 and s1[c] < t1[c]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l:r+1] if res_len != float('infinity') else ""
            

            
        

                
                

