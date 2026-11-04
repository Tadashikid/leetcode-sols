class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n=len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]

    
        zero=0
        one=0
        two=0

        for i in nums:
            if i==0:
                zero+=1
            elif i==1:
                one+=1
            else:
                two+=1

        for i in range(0,zero):
            nums[i]=0
        
        for i in range(zero,zero+one):
            nums[i]=1
        for i in range(zero+one,zero+one+two):
            nums[i]=2

                


