class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res=0
        for i in nums:
            res=i^res

        return res
        