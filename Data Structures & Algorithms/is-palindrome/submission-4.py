class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm_s = s.lower()

        i = 0
        j = len(norm_s)-1
        while i<=j:
            while not norm_s[i].isalnum() and i<j:
                i+=1 

            while not norm_s[j].isalnum() and i<j:
                j-=1

            
            if norm_s[i]!=norm_s[j]:
                return False
            
            i+=1
            j-=1
            
        return True
