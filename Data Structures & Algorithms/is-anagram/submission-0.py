class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        s_keys = 0
        t_keys = 0

        for c in s:
            if c not in s_count:
                s_count[c] = 0
                s_keys += 1

            s_count[c] += 1

        for c in t:
            if c not in t_count:
                t_count[c] = 0
                t_keys += 1

            t_count[c] += 1

        if s_keys!=t_keys:
            return False
        
        for k in s_count:
            if k not in t_count or t_count[k]!=s_count[k]:
                return False

        return True
        
        
        