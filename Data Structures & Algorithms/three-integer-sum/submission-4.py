class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for ind, n in enumerate(nums):
            if ind>0 and n == nums[ind-1]:
                continue
            t = n

            l = ind+1
            r = len(nums)-1

            while l<r:
                s = nums[l]+nums[r]+t
                if s==0:
                    ans.append([t, nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l+=1
                    r-=1

                elif s>0:
                    r-=1
                elif s<0:
                    l+=1


        return ans