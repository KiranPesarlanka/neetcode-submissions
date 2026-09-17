class Solution:
    def trap(self, height: List[int]) -> int:
        
        lmax = [0]*len(height)
        rmax = [0]*len(height)

        water = 0
        

        for ind, n in enumerate(height):
            if ind==0:
                continue
            lmax[ind]=max(lmax[ind-1], height[ind-1])

        for ind, n in enumerate(height[::-1]):
            ind = len(height) -1 -ind
            if ind==len(height)-1:
                continue

            rmax[ind]=max(rmax[ind+1], height[ind+1])

        for ind,n in enumerate(height):
            
            mnh = min(lmax[ind],rmax[ind])

            trp = mnh - height[ind] if mnh>height[ind] else 0 
            water += trp

        return water