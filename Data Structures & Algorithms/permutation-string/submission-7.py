class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # h1, h2 = {}, {}
        # for ch in s1:
        #     h1[ch] = 1 + h1.get(ch, 0)
        # l = 0
        # r = len(s1)

        # while r < len(s2)+1:
        #     curr = s2[l:r]
        #     for ch in curr:
        #         h2[ch] = 1 + h2.get(ch, 0)

        #     if h2 != h1:
        #         h2 = {}
        #         r += 1
        #         l += 1
        #     else:
        #         return True

        # return False

    # better solution, what I originally thought, 
    # but included deleting key in dictionary
    # most common solution uses hash table of ascii values in alphabet
    # the idea is very similar, but we are recreating hash table everytime
    # instead of using same one
        if len(s1) > len(s2):
            return False

        h1, h2 = {}, {}
        
        # Populate initial window frequencies of size len(s1)
        for i in range(len(s1)):
            h1[s1[i]] = 1 + h1.get(s1[i], 0)
            h2[s2[i]] = 1 + h2.get(s2[i], 0)

        if h1 == h2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # Add new character entering the window
            h2[s2[r]] = 1 + h2.get(s2[r], 0)
            
            # Remove character leaving the window
            h2[s2[l]] -= 1
            if h2[s2[l]] == 0:
                del h2[s2[l]]
            l += 1

            if h1 == h2:
                return True

        return False