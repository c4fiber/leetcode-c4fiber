class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, c1 = sum(nums1), nums1.count(0)
        s2, c2 = sum(nums2), nums2.count(0)
        
        if s1 + c1 > s2 + c2:
            if s1 + c1 >= s2 + c2 and c2:
                return s1 + c1
            else:
                return -1
        elif s2 + c2 > s1 + c1:
            if s2 + c2 >= s1 + c1 and c1:
                return s2 + c2
            else:
                return -1
        else:
            return s1 + c1
                
            
        
        