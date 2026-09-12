class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [1] * n
        p = 1

        for i in range(1, n):
            p *= nums[i - 1]
            pre[i] = p

        su = [1] * n
        s = 1

        for i in range(n - 2, -1, -1):
            s *= nums[i + 1]
            su[i] = s

        f = []

        for i in range(n):
            f.append(pre[i] * su[i])

        return f