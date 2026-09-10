from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
        d = defaultdict(list)
        for c in strs:
            sc = ''.join(sorted(c))
            d[sc].append(c)

        return [v for k,v in d.items()]