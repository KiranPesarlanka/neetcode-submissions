class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        if not nums:return 0
        snums = sorted(list(set(nums)))
        largest = 0
        prev = snums[0]
        t = [prev]
     
        for n in snums[1:]:
  
            if prev+1==n:
                t.append(n)
                
            else:
                if len(t) not in d:  
                    d[len(t)] = []
                    if len(t)>largest:
                        largest = len(t)
                d[len(t)].append(t)
                t = [n]
            prev = n
        
        if len(t)>largest:
            largest = len(t)

        return largest

