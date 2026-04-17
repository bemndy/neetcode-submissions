class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 0
        h = set(nums)
        seqs = []

        for num in nums:
            if num - 1 not in h:
                count = 0
                seq = 0
                while num + count in h:
                    seq += 1
                    count += 1
                seqs.append(seq)
        
        return 0 if not seqs else max(seqs)
                
            
            


            
        