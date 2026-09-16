class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm_s = s.lower()

        i = 0
        j = len(norm_s)-1
        while i<=j:
            while i<j and not norm_s[i].isalnum():
                i+=1 

            while i<j and not norm_s[j].isalnum():
                j-=1

            
            if norm_s[i]!=norm_s[j]:
                return False
            
            i+=1
            j-=1
            
        return True
