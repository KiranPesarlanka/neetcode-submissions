class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_s = set(nums)

        curr_largest = 0
        overall_largest = 0
        i = 0
        while i<len(nums):
            curr =  nums[i]
            if curr-1 not in nums_s:
                curr_largest += 1

                while curr+1 in nums_s:
                    curr_largest += 1
                    curr = curr+1

                overall_largest = max(overall_largest, curr_largest)

            curr_largest = 0
            i+=1

        return overall_largest