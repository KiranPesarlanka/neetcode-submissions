class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for ind, n in enumerate(numbers):
            if target-n in seen:
                return [1+seen[target-n], 1+ind]
            seen[n] = ind
        
        return []