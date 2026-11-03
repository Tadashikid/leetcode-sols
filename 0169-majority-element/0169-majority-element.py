'''class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count=0
        carr={}
        n=len(nums)
        h=n//2
        for i in nums:
            if i in carr:
                carr[i]+=1
            else:
                carr[i]=1

        for k,v in carr.items():
            if v>h:
                return k '''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cand=None
        count=0

        for i in nums:
            if count==0:
                cand=i
            
            if i==cand:
                count+=1

            else:
                count-=1

        return cand