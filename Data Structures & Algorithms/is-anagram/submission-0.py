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
        