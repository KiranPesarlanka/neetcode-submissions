class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)

        overall_largest = 0

        for curr in nums_s:
            # Only start from the beginning of a sequence
            if curr - 1 not in nums_s:
                curr_largest = 1

                while curr + 1 in nums_s:
                    curr += 1
                    curr_largest += 1

                overall_largest = max(overall_largest, curr_largest)

        return overall_largest