class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # p1 = 0
        # p2 = 0
        # res = 0
        # st = set()

        # while p2 < len(s):
        #     # Shrink p1 until the duplicate character s[p2] is removed from set
        #     while s[p2] in st:
        #         st.remove(s[p1])
        #         p1 += 1

        #     # Add current character to set and update max length
        #     st.add(s[p2])
        #     res = max(res, p2 - p1 + 1)
        #     p2 += 1
        # return res
        # another version
        st = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            res = max(res, r - l + 1)
        return res
