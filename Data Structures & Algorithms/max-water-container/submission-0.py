class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        max_seen = 0
        while l<r:

            mh = min(heights[l], heights[r])

            dist = r - l

            max_seen = max(max_seen, mh*dist)

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            
        
        return max_seen