class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        st1 = {}
        st2 = {}
        for i in range(len(s)):
            if s[i] not in st1:
                st1[s[i]] = 1
            else:
                st1[s[i]] += 1
            if t[i] not in st2:
                st2[t[i]] = 1
            else:
                st2[t[i]] += 1
        if st2 == st1:
            return True
        else:
            return False

        '''
        #way shorter
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

        #really pythonic 
        countS, countT = {}, {}
        for i in range(lens)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        '''
        