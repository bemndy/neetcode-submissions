class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = {}
        final_strs = []
        index = 0
        for word in strs:
            sorted_word = " ".join(sorted(word))
            if sorted_word not in new_strs:
                new_strs[sorted_word] = index
                final_strs.append([word])
                index += 1
            else:
                final_strs[new_strs[sorted_word]].append(word)
        return final_strs
                
            
                
            