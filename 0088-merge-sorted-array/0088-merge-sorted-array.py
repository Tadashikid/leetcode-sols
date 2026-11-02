class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
      
        
        nums1[:] = nums1[:m] 
        for i in nums2:
            nums1.append(i)
        nums1.sort()




